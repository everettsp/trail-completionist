"""Tests for trail_completionist package."""

import trail_completionist


def test_version():
    """Test that the package version is defined."""
    assert hasattr(trail_completionist, "__version__")
    assert isinstance(trail_completionist.__version__, str)
    assert trail_completionist.__version__ == "0.1.0"


def test_author():
    """Test that the package author is defined."""
    assert hasattr(trail_completionist, "__author__")
    assert isinstance(trail_completionist.__author__, str)


def test_description():
    """Test that the package description is defined."""
    assert hasattr(trail_completionist, "__description__")
    assert isinstance(trail_completionist.__description__, str)
