"""Unit tests for the background generator under tools/background."""

import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path
from types import ModuleType

GENERATOR = Path(__file__).parents[2] / "tools" / "background" / "generate.py"


def load_generator() -> ModuleType:
    spec = importlib.util.spec_from_file_location("generate_background", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_svg_is_well_formed_when_built() -> None:
    root = ET.fromstring(load_generator().build_svg())
    assert root.tag.endswith("svg")


def test_svg_is_repeatable_when_built_twice() -> None:
    generator = load_generator()
    assert generator.build_svg() == generator.build_svg()


def test_svg_shows_code_network_and_binary_when_built() -> None:
    svg = load_generator().build_svg()
    assert "backward" in svg
    assert "<circle" in svg
    assert "0101" in svg or "1010" in svg or "0110" in svg or "1001" in svg


def test_committed_background_matches_generator_when_compared() -> None:
    committed = GENERATOR.parents[2] / load_generator().OUTPUT
    assert committed.read_text(encoding="utf-8") == load_generator().build_svg()
