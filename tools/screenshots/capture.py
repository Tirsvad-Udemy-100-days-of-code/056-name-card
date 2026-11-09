"""Take one screenshot per lecture step of the name card project.

@file capture.py
@brief Runs inside the Playwright Docker container (see run.sh); never on the host desktop.

The four steps are:
  1. the Identity template as downloaded (opened as plain files),
  2. Flask serving the untouched template at "/" (asset paths broken),
  3. the asset paths fixed to "static/" (template renders),
  4. the personalised name card served by the real application.
"""

from __future__ import annotations

import http.server
import os
import re
import shutil
import subprocess
import threading
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

REPO = Path("/repo")
OUT = Path("/out")
STATIC = REPO / "src/name_card/presentation/static"
ORIGINAL = REPO / "tools/screenshots/original"
VIEWPORT = {"width": 1280, "height": 800}


def serve(directory: Path, port: int, routes: dict[str, Path] | None = None) -> None:
    """Serve a directory (and optional exact routes) on localhost."""
    routes = routes or {}

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args: object, **kwargs: object) -> None:
            super().__init__(*args, directory=str(directory), **kwargs)  # type: ignore[arg-type]

        def do_GET(self) -> None:
            path = self.path.split("?")[0]
            if path in routes:
                body = routes[path].read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            super().do_GET()

        def log_message(self, *args: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()


def main() -> int:
    work = Path("/tmp/steps")
    shutil.rmtree(work, ignore_errors=True)
    # Step 1: the template as downloaded: index.html next to assets/ and images/.
    s1 = work / "s1"
    shutil.copytree(STATIC / "assets", s1 / "assets")
    shutil.copytree(ORIGINAL / "images", s1 / "images")
    shutil.copy(ORIGINAL / "index.html", s1 / "index.html")
    # Steps 2 and 3: the server only knows "/" (like the first Flask route) and /static.
    s2 = work / "s2"
    s2.mkdir(parents=True)
    (s2 / "static").mkdir()
    shutil.copytree(STATIC / "assets", s2 / "static/assets")
    shutil.copytree(ORIGINAL / "images", s2 / "static/images")
    shutil.copy(ORIGINAL / "index.html", s2 / "index-unfixed.html")
    fixed = (ORIGINAL / "index.html").read_text(encoding="utf-8")
    fixed = re.sub(r'(href|src)="(assets|images)/', r'\1="static/\2/', fixed)
    (s2 / "index-fixed.html").write_text(fixed, encoding="utf-8")
    serve(s1, 8101)
    serve(s2, 8102, {"/": s2 / "index-unfixed.html"})
    serve(s2, 8103, {"/": s2 / "index-fixed.html"})
    # The fixed-path server must resolve "static/..." relative to "/", i.e. /static/....

    # Step 4: the real application.
    os.environ["PYTHONPATH"] = str(REPO / "src")
    app = subprocess.Popen(["python3", "-m", "name_card"], cwd=REPO)
    pause = threading.Event()
    for _ in range(40):
        try:
            urllib.request.urlopen("http://127.0.0.1:5000/", timeout=1)
            break
        except OSError:
            pause.wait(0.5)

    shots = [
        ("step-1-template-download.png", "http://127.0.0.1:8101/index.html"),
        ("step-2-flask-unfixed-paths.png", "http://127.0.0.1:8102/"),
        ("step-3-static-paths-fixed.png", "http://127.0.0.1:8103/"),
        ("step-4-personalised-card.png", "http://127.0.0.1:5000/"),
    ]
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for name, url in shots:
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(1200)
            page.screenshot(path=str(OUT / name))
            print("saved", name)
        browser.close()
    app.terminate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
