#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Miscellaneous."""

__all__ = [
    "validate_in_out_types",
    "property_and_validate_in_out_types",
]

from typing import Callable
from pydantic import validate_call


def validate_in_out_types(func: Callable) -> Callable:
    """Decorator that validates the types of input and output arguments of a
    function using Pydantic.

    This decorator ensures that:
    - Input arguments are strictly validated against their type annotations.
    - Arbitrary types are allowed in the type annotations.
    - Default values for arguments are validated.
    - The return value of the function is validated.

    Parameters
    ----------
    func : Callable
        The function to be wrapped and validated.

    Returns
    -------
    wrapped_func : Callable
        The wrapped function with input and output type validation.

    Examples
    --------
    @validate_in_out_types
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)  # This will pass type validation
    add(1, '2')  # This will raise a validation error
    """

    @validate_call(config=dict(strict=True,
                               arbitrary_types_allowed=True,
                               validate_default=True),
                   validate_return=True)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def property_and_validate_in_out_types(func: Callable) -> Callable:
    """Implements the property decorator above the validate_in_out_types
    decorator.
    """

    @property   # type: ignore
    @validate_in_out_types
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
