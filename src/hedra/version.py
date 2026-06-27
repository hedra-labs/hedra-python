from importlib import metadata

# The import package is `hedra` but the PyPI distribution is `hedra-python`,
# so the metadata must be looked up under the distribution name.
try:
    __version__ = metadata.version("hedra-python")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"
