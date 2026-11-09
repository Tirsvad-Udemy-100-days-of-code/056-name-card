"""Use cases.

@file use_cases.py
@brief Application use cases of the name card.
"""

from name_card.application.ports import ProfileRepository
from name_card.domain.profile import Profile


class GetCardUseCase:
    """Fetch the profile for the card."""

    def __init__(self, repository: ProfileRepository) -> None:
        """Create the use case.

        @param repository Source of the profile.
        """
        self._repository = repository

    def execute(self) -> Profile:
        """Return the profile to show.

        @return The profile.
        """
        return self._repository.get_profile()
