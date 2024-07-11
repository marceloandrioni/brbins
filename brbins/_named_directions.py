#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Named directions."""

__all__ = [
    "CardinalNamedDirections",
    "VesselNamedDirections",
]

import numpy as np


class NamedDirections:

    def _named_dirs(self) -> dict[float, tuple[str, str]]:
        step = 360 / len(self._names_and_long_names)
        return dict(zip(np.arange(0, 360, step), self._names_and_long_names))

    @property
    def names(self) -> dict[float, str]:
        return {k: v[0] for k, v in self._named_dirs().items()}

    @property
    def long_names(self) -> dict[float, str]:
        return {k: v[1] for k, v in self._named_dirs().items()}


class CardinalNamedDirections(NamedDirections):

    _names_and_long_names: list[tuple[str, str]] = [
        ("N", "North"),
        ("NbE", "North by East"),
        ("NNE", "North-Northeast"),
        ("NEbN", "Northeast by North"),
        ("NE", "Northeast"),
        ("NEbE", "Northeast by East"),
        ("ENE", "East-Northeast"),
        ("EbN", "East by North"),
        ("E", "East"),
        ("EbS", "East by South"),
        ("ESE", "East-Southeast"),
        ("SEbE", "Southeast by East"),
        ("SE", "Southeast"),
        ("SEbS", "Southeast by South"),
        ("SSE", "South-Southeast"),
        ("SbE", "South by East"),
        ("S", "South"),
        ("SbW", "South by West"),
        ("SSW", "South-Southwest"),
        ("SWbS", "Southwest by South"),
        ("SW", "Southwest"),
        ("SWbW", "Southwest by West"),
        ("WSW", "West-Southwest"),
        ("WbS", "West by South"),
        ("W", "West"),
        ("WbN", "West by North"),
        ("WNW", "West-Northwest"),
        ("NWbW", "Northwest by West"),
        ("NW", "Northwest"),
        ("NWbN", "Northwest by North"),
        ("NNW", "North-Northwest"),
        ("NbW", "North by West"),
    ]


class VesselNamedDirections(NamedDirections):

    _names_and_long_names: list[tuple[str, str]] = [
        ("Bow", "Bow"),
        ("Stbd-Bow", "Starboard-Bow"),
        ("Stbd", "Starboard"),
        ("Stbd-Quarter", "Starboard-Quarter"),
        ("Stern", "Stern"),
        ("Port-Quarter", "Port-Quarter"),
        ("Port", "Port"),
        ("Port-Bow", "Port-Bow"),
    ]
