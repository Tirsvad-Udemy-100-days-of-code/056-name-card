"""Entry point.

@file __main__.py
@brief Runs the name card server.
"""

from name_card import constants
from name_card.presentation.app import create_app


def main() -> None:
    """Create the app and serve it on the configured host and port.

    @return None
    """
    create_app().run(host=constants.HOST, port=constants.PORT, debug=False)


if __name__ == "__main__":
    main()
