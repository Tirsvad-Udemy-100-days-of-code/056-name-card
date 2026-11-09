"""Constant-backed profile repository.

@file constant_profile_repository.py
@brief Profile repository reading from application constants.
"""

from name_card import constants
from name_card.domain.profile import Profile, SocialLink


class ConstantProfileRepository:
    """Profile repository that builds the profile from constants."""

    def get_profile(self) -> Profile:
        """Return the profile built from constants.

        @return The profile.
        """
        links = tuple(
            SocialLink(label=label, url=url, icon_class=icon_class)
            for label, url, icon_class in constants.SOCIAL_LINKS
        )
        return Profile(
            name=constants.CARD_NAME,
            headline=constants.HEADLINE,
            avatar=constants.AVATAR_FILE,
            links=links,
        )
