#
#       Copyright (C) 2014-
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc

def openMenu():
    if xbmc.getCondVisibility('Window.IsActive(ContextMenu)') == 1:
        return

    xbmc.executebuiltin('Action(ContextMenu)') 
    import resources.lib.Globals
    import os
    path   = Globals.ADDON_PATH
    script = os.path.join(path, sys.argv[0])
    cmd    = 'AlarmClock(%s,RunScript(%s),%d,True)' % ('menu', script, 0)

    xbmc.executebuiltin(cmd)  


openMenu()