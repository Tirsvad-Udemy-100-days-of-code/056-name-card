"""Integration tests for the Flask app."""

import re

import pytest
from flask.testing import FlaskClient

from name_card import constants
from name_card.presentation.app import create_app

STATIC_URL = re.compile(r'(?:href|src)="(/static/[^"]+)"')
CSS_URL = "/static/assets/css/main.css"


@pytest.fixture
def client() -> FlaskClient:
    return create_app().test_client()


def test_home_returns_card_when_requested(client: FlaskClient) -> None:
    response = client.get(constants.ROOT_ROUTE)
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert constants.CARD_NAME in body
    assert constants.ATTRIBUTION_TEXT in body
    assert "html5up.net" in body


def test_static_urls_resolve_when_page_rendered(client: FlaskClient) -> None:
    body = client.get(constants.ROOT_ROUTE).get_data(as_text=True)
    urls = STATIC_URL.findall(body)
    assert urls
    for url in urls:
        assert client.get(url).status_code == 200, url


def test_css_is_referenced_and_served_when_page_rendered(client: FlaskClient) -> None:
    body = client.get(constants.ROOT_ROUTE).get_data(as_text=True)
    assert CSS_URL in body
    assert client.get(CSS_URL).status_code == 200


def test_unknown_route_returns_404_when_requested(client: FlaskClient) -> None:
    assert client.get("/does-not-exist").status_code == 404


def test_card_stylesheet_follows_template_stylesheet_when_page_rendered(
    client: FlaskClient,
) -> None:
    body = client.get(constants.ROOT_ROUTE).get_data(as_text=True)
    assert body.index("assets/css/main.css") < body.index("assets/css/card.css")


def test_portrait_fits_card_when_card_stylesheet_served(client: FlaskClient) -> None:
    css = client.get("/static/assets/css/card.css").get_data(as_text=True)
    rule = css.split("#main .avatar img", 1)[1].split("}", 1)[0]
    assert "width: 10em" in rule
    assert "object-fit: cover" in rule


def test_background_image_is_served_when_card_stylesheet_names_it(
    client: FlaskClient,
) -> None:
    css = client.get("/static/assets/css/card.css").get_data(as_text=True)
    response = client.get("/static/images/bg.svg")
    assert "images/bg.svg" in css
    assert response.status_code == 200
    assert response.mimetype == "image/svg+xml"
