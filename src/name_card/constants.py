"""Application constants.

@file constants.py
@brief Module-level constants for the name card application.
"""

from typing import Final

## @brief Application name.
APP_NAME: Final[str] = "name_card"

## @brief Name shown on the card.
CARD_NAME: Final[str] = "Jens Tirsvad Nielsen"

## @brief Template file rendered for the card page.
TEMPLATE_INDEX: Final[str] = "index.html"

## @brief URL path of the card page.
ROOT_ROUTE: Final[str] = "/"

## @brief Host address the server binds to.
HOST: Final[str] = "127.0.0.1"

## @brief TCP port the server listens on.
PORT: Final[int] = 5000
