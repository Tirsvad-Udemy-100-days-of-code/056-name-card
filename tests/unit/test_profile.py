"""Tests for the domain, use case and constant repository."""

import dataclasses

import pytest

from name_card import constants
from name_card.application.use_cases import GetCardUseCase
from name_card.domain.profile import Profile, SocialLink
from name_card.infrastructure.constant_profile_repository import (
    ConstantProfileRepository,
)


class FakeRepository:
    def __init__(self, profile: Profile) -> None:
        self._profile = profile

    def get_profile(self) -> Profile:
        return self._profile


def test_social_link_is_immutable_when_assigned() -> None:
    link = SocialLink("a", "b", "c")
    with pytest.raises(dataclasses.FrozenInstanceError):
        link.label = "x"  # type: ignore[misc]


def test_use_case_returns_profile_when_repository_has_one() -> None:
    profile = Profile("N", "H", "a.jpg", (SocialLink("l", "u", "i"),))
    assert GetCardUseCase(FakeRepository(profile)).execute() == profile


def test_repository_returns_constants_when_called() -> None:
    profile = ConstantProfileRepository().get_profile()
    assert profile.name == constants.CARD_NAME
    assert profile.headline == constants.HEADLINE
    assert profile.avatar == constants.AVATAR_FILE


def test_repository_maps_all_links_when_called() -> None:
    links = ConstantProfileRepository().get_profile().links
    assert [(x.label, x.url, x.icon_class) for x in links] == list(
        constants.SOCIAL_LINKS
    )
