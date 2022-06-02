import vendorize.cli as vendorize
from shutil import make_archive

ADDON_NAME: str = "addon"
CODE_DIR: str = "src"

# Download packages into the _vendor folder to be used in the addon.
# Configure the downloaded packages in vendorize.toml.
vendorize.main()

# Zip addon for easy distribution
make_archive(ADDON_NAME, "zip", CODE_DIR)
