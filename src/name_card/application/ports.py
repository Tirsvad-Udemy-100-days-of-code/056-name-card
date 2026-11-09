"""Ports of the application layer.

@file ports.py
@brief Interfaces the use cases need from outside.
"""

from typing import Protocol

from name_card.domain.profile import Profile


class ProfileRepository(Protocol):
    """Source of the profile shown on the card."""

    def get_profile(self) -> Profile:
        """Return the profile.

        @return The profile.
        """
        ...
