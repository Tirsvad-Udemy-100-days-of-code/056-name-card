"""Tests for the name_card constants."""

import importlib

from name_card import constants


def test_package_imports_when_on_pythonpath() -> None:
    assert importlib.import_module("name_card") is not None


def test_app_name_has_value_when_defined() -> None:
    assert constants.APP_NAME == "name_card"


def test_app_name_is_str_when_defined() -> None:
    assert isinstance(constants.APP_NAME, str)


def test_card_name_has_value_when_defined() -> None:
    assert constants.CARD_NAME == "Jens Tirsvad Nielsen"


def test_card_name_is_str_when_defined() -> None:
    assert isinstance(constants.CARD_NAME, str)


def test_template_index_has_value_when_defined() -> None:
    assert constants.TEMPLATE_INDEX == "index.html"


def test_template_index_is_str_when_defined() -> None:
    assert isinstance(constants.TEMPLATE_INDEX, str)


def test_root_route_has_value_when_defined() -> None:
    assert constants.ROOT_ROUTE == "/"


def test_root_route_starts_with_slash_when_defined() -> None:
    assert constants.ROOT_ROUTE.startswith("/")


def test_host_has_value_when_defined() -> None:
    assert constants.HOST == "127.0.0.1"


def test_host_is_str_when_defined() -> None:
    assert isinstance(constants.HOST, str)


def test_port_has_value_when_defined() -> None:
    assert constants.PORT == 5000


def test_port_is_int_when_defined() -> None:
    assert isinstance(constants.PORT, int)


def test_port_in_valid_range_when_defined() -> None:
    assert 1 <= constants.PORT <= 65535
