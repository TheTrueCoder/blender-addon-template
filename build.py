import vendorize.cli as vendorize
from shutil import make_archive, copytree, rmtree

ADDON_NAME: str = "cool-addon"
CODE_DIR: str = "src"

# Download packages into the _vendor folder to be used in the addon.
# Configure the downloaded packages in vendorize.toml.
vendorize.main()

# Make temporary folder copy with the project name so that
# the addon is identifiable when installed.
copytree(CODE_DIR, ADDON_NAME)
# Zip addon for easy distribution
make_archive(ADDON_NAME, "zip", ".", ADDON_NAME)
rmtree(ADDON_NAME)
