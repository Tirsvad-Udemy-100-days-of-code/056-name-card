**English** · [Dansk](Run-and-Test-da) · [Bahasa Malaysia](Run-and-Test-ms)

# Run and test

Create and use a local `.venv`, upgrade pip, install the project with the test extra, run it, test it and build the Doxygen documentation. The screenshots are taken in a Docker container with a headless browser, so no window opens on your desktop.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m name_card              # open http://127.0.0.1:5000/
python -m pytest
doxygen Doxyfile
bash tools/screenshots/run.sh    # screenshots, in Docker
```

## What we gained

- A repeatable setup that any course participant can follow.
- Tests for the route and for the static assets.
- API documentation from Doxygen comments.
