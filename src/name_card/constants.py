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

## @brief Headline shown under the name on the card.
HEADLINE: Final[str] = (
    "Software architect and SQA/QC specialist · Datamatiker student at UCL Odense · Linux fan"
)

## @brief Avatar image path relative to the static folder.
AVATAR_FILE: Final[str] = "images/avatar.jpg"

## @brief Template folder name next to the presentation module.
TEMPLATE_FOLDER: Final[str] = "templates"

## @brief Static folder name next to the presentation module.
STATIC_FOLDER: Final[str] = "static"

## @brief Text of the design attribution link.
ATTRIBUTION_TEXT: Final[str] = "HTML5 UP"

## @brief URL of the design attribution link.
ATTRIBUTION_URL: Final[str] = "https://html5up.net"

## @brief Social links as (label, url, icon_class) tuples.
SOCIAL_LINKS: Final[tuple[tuple[str, str, str], ...]] = (
    (
        "Repositories",
        "https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code",
        "brands fa-git-alt",
    ),
    ("Linux", "https://www.kernel.org", "brands fa-linux"),
    ("UCL Odense", "https://www.ucl.dk", "solid fa-graduation-cap"),
)
