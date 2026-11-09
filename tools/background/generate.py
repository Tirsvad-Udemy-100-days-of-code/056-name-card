"""Generate the name card background: software development, AI and machine learning.

@file generate.py
@brief Writes static/images/bg.svg with the Python standard library only.

Run from the repository root:  python tools/background/generate.py
The picture has code on the left, a small neural network on the right and rows of
binary digits at the top and bottom. The seed is fixed, so the output is repeatable.
"""

from __future__ import annotations

import itertools
import random
from pathlib import Path

## @brief Output file, relative to the repository root.
OUTPUT = Path("src/name_card/presentation/static/images/bg.svg")

## @brief Canvas size in pixels (the CSS scales it with background-size: cover).
WIDTH, HEIGHT = 1920, 1080

## @brief Fixed seed so that the picture is the same on every run.
SEED = 56

## @brief Number of nodes in each layer of the neural network.
LAYERS = (4, 7, 7, 3)

## @brief Code lines as (indent, [(colour, text), ...]) tokens, in syntax colours.
CODE = (
    (0, (("#c792ea", "class "), ("#ffcb6b", "Neuron"), ("#89ddff", ":"))),
    (1, (("#c792ea", "def "), ("#82aaff", "forward"), ("#89ddff", "(self, x):"))),
    (2, (("#eeffff", "z = "), ("#82aaff", "dot"), ("#89ddff", "(self.w, x) + self.b"))),
    (2, (("#c792ea", "return "), ("#82aaff", "max"), ("#89ddff", "(0, z)"))),
    (0, (("#546e7a", "# train the model"),)),
    (
        0,
        (
            ("#c792ea", "for "),
            ("#eeffff", "epoch "),
            ("#c792ea", "in "),
            ("#82aaff", "range"),
            ("#89ddff", "(100):"),
        ),
    ),
    (1, (("#eeffff", "loss = "), ("#82aaff", "mse"), ("#89ddff", "(model(x), y)"))),
    (
        1,
        (
            ("#eeffff", "loss"),
            ("#89ddff", "."),
            ("#82aaff", "backward"),
            ("#89ddff", "()"),
        ),
    ),
    (
        1,
        (
            ("#eeffff", "optimizer"),
            ("#89ddff", "."),
            ("#82aaff", "step"),
            ("#89ddff", "()"),
        ),
    ),
    (
        0,
        (
            ("#c792ea", "assert "),
            ("#eeffff", "accuracy "),
            ("#89ddff", "> "),
            ("#f78c6c", "0.9"),
        ),
    ),
    (0, (("#546e7a", "$ git commit -m "), ("#c3e88d", '"feat: add model"'))),
    (0, (("#546e7a", "$ pytest -q  "), ("#c3e88d", "22 passed"))),
)


## @brief Opening tag of the SVG document.
SVG_OPEN = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
    f'width="{WIDTH}" height="{HEIGHT}" preserveAspectRatio="xMidYMid slice">'
)

## @brief Gradient and glow definitions used by the picture.
SVG_DEFS = (
    "<defs>"
    '<linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#0a1128"/><stop offset="1" stop-color="#16325c"/>'
    "</linearGradient>"
    '<filter id="glow" x="-200%" y="-200%" width="500%" height="500%">'
    '<feGaussianBlur stdDeviation="6" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
    "</filter></defs>"
)


def escape_text(text: str) -> str:
    """Return text that is safe inside SVG element content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def code_block(x: int, y: int, size: int, opacity: float) -> str:
    """Return an SVG group with the code lines, one text row per line."""
    rows = []
    for n, (indent, tokens) in enumerate(CODE):
        spans = "".join(
            f'<tspan fill="{colour}">{escape_text(text)}</tspan>'
            for colour, text in tokens
        )
        rows.append(
            f'<text x="{x + indent * size * 2}" y="{y + n * size * 1.7:.0f}" '
            f'xml:space="preserve">{spans}</text>'
        )
    return (
        f'<g font-family="DejaVu Sans Mono, Consolas, monospace" font-size="{size}" '
        f'opacity="{opacity}">{"".join(rows)}</g>'
    )


def binary_rows(
    rng: random.Random, y: int, count: int, size: int, opacity: float
) -> str:
    """Return rows of binary digits that run across the canvas."""
    chars = WIDTH // (size * 6 // 10)
    rows = []
    for n in range(count):
        bits = "".join(rng.choice("01") for _ in range(chars))
        rows.append(
            f'<text x="0" y="{y + n * size * 1.6:.0f}" textLength="{WIDTH}" '
            f'lengthAdjust="spacing">{bits}</text>'
        )
    return (
        f'<g font-family="DejaVu Sans Mono, Consolas, monospace" font-size="{size}" '
        f'fill="#7fdbff" opacity="{opacity}">{"".join(rows)}</g>'
    )


def network(rng: random.Random, x0: int, x1: int, y0: int, y1: int) -> str:
    """Return a fully connected neural network, a few edges and nodes lit."""
    points: list[list[tuple[float, float]]] = []
    for i, count in enumerate(LAYERS):
        x = x0 + (x1 - x0) * i / (len(LAYERS) - 1)
        step = (y1 - y0) / max(count - 1, 1)
        points.append(
            [
                (x, y0 + j * step + (y1 - y0 - step * (count - 1)) / 2)
                for j in range(count)
            ]
        )
    edges = []
    for left, right in itertools.pairwise(points):
        for ax, ay in left:
            for bx, by in right:
                lit = rng.random() < 0.12
                colour, width, opacity = (
                    ("#7fffd4", 1.6, 0.8) if lit else ("#7fdbff", 1, 0.22)
                )
                edges.append(
                    f'<line x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}" '
                    f'stroke="{colour}" stroke-width="{width}" opacity="{opacity}"/>'
                )
    nodes = []
    for layer in points:
        for x, y in layer:
            lit = rng.random() < 0.35
            fill = "#7fffd4" if lit else "#7fdbff"
            glow = ' filter="url(#glow)"' if lit else ""
            nodes.append(
                f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{11 if lit else 8}" fill="{fill}" '
                f'opacity="{0.95 if lit else 0.6}"{glow}/>'
            )
    return f"<g>{''.join(edges)}{''.join(nodes)}</g>"


def build_svg() -> str:
    """Return the complete SVG document as text."""
    rng = random.Random(SEED)
    parts = [
        SVG_OPEN,
        SVG_DEFS,
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#sky)"/>',
        binary_rows(rng, 40, 5, 22, 0.14),
        binary_rows(rng, HEIGHT - 150, 5, 22, 0.14),
        code_block(170, 250, 24, 0.75),
        network(rng, 1290, 1790, 250, 830),
        "</svg>",
    ]
    return "\n".join(parts) + "\n"


def main() -> int:
    """Write the background file and report its path."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_svg(), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
