# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
        "name": "My Awesome Add-on",
        "description": "Single line describing my awesome add-on.",
        "author": "Aaron Powell",
        "version": (1, 0),
        "blender": (2, 80, 0),
        "location": "Properties > Render > My Awesome Panel",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        "category": "Render"
        }

import bpy

# SAMPLE: Import sample hello world package from _vendor folder.
from ._vendor import hello_world

# Import your own packages with below line.
# This package must be in vendorize.toml and had the build script run.
# from ._vendor import <Package name>

#
# Add additional functions here
#

def register():
    from . import properties
    from . import ui
    properties.register()
    ui.register()

    # SAMPLE: Run hello function from hello world package 
    hello_world.hello()

def unregister():
    from . import properties
    from . import ui
    properties.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()
