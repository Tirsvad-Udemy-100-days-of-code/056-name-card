"""Profile value objects.

@file profile.py
@brief Immutable domain model of the name card.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SocialLink:
    """A link to an external profile.

    @param label Text shown for the link.
    @param url Target address.
    @param icon_class CSS classes of the icon.
    """

    label: str
    url: str
    icon_class: str


@dataclass(frozen=True, slots=True)
class Profile:
    """The person shown on the card.

    @param name Full name.
    @param headline Short description.
    @param avatar Avatar image path relative to the static folder.
    @param links Social links in display order.
    """

    name: str
    headline: str
    avatar: str
    links: tuple[SocialLink, ...]
