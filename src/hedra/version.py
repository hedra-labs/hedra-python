from importlib import metadata

# The import package is `hedra` but the PyPI distribution is `hedra-sdk`,
# so the metadata must be looked up under the distribution name.
#
# Renaming the distribution and forgetting this file does NOT raise: the
# fallback below makes every install report 0.0.0 instead. tests/custom/
# test_version.py pins the two together for exactly that reason.
try:
    __version__ = metadata.version("hedra-sdk")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"
