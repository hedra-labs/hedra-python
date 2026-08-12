"""The distribution name is hand-carried in version.py, so it can silently rot.

`version.py` looks the version up by *distribution* name (`hedra-sdk`) while the
import package is `hedra`. The lookup is wrapped in
`except PackageNotFoundError: __version__ = "0.0.0"`, so if the two ever
disagree — as they did when the distribution was renamed from `hedra-python` —
nothing raises and every install reports 0.0.0. This pins them together.
"""

from importlib import metadata

import hedra

DISTRIBUTION = "hedra-sdk"


def test_version_matches_the_installed_distribution():
    assert hedra.__version__ == metadata.version(DISTRIBUTION)


def test_version_is_not_the_not_found_sentinel():
    assert hedra.__version__ != "0.0.0", (
        f"__version__ fell back to the PackageNotFoundError sentinel: version.py is not looking up {DISTRIBUTION!r}"
    )
