"""Flask application factory.

@file app.py
@brief Builds the Flask app; composition root of the application.
"""

from pathlib import Path

from flask import Flask, render_template

from name_card import constants
from name_card.application.ports import ProfileRepository
from name_card.application.use_cases import GetCardUseCase

# Composition root: the only place presentation imports infrastructure.
from name_card.infrastructure.constant_profile_repository import (
    ConstantProfileRepository,
)


def create_app(repository: ProfileRepository | None = None) -> Flask:
    """Create the Flask application.

    @param repository Profile source; defaults to the constant repository.
    @return The configured Flask app.
    """
    base = Path(__file__).parent
    app = Flask(
        __name__,
        template_folder=str(base / constants.TEMPLATE_FOLDER),
        static_folder=str(base / constants.STATIC_FOLDER),
    )
    source = repository if repository is not None else ConstantProfileRepository()
    use_case = GetCardUseCase(source)

    @app.route(constants.ROOT_ROUTE)
    def home() -> str:
        """Render the name card.

        @return The rendered page.
        """
        return render_template(
            constants.TEMPLATE_INDEX,
            profile=use_case.execute(),
            attribution_url=constants.ATTRIBUTION_URL,
            attribution_text=constants.ATTRIBUTION_TEXT,
        )

    return app
