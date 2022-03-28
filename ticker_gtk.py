import os
import gi
import sys
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
args = sys.argv

with open("ticker_setup.json", "r") as f:
    setup = json.load(f)
pos = setup["position_static_ticker"]
print(setup)
font_and_size = setup['static_ticker_font'] + " " + str(setup['static_ticker_font_size'])

class Splash(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="splashtitle")
        Gtk.Window.set_keep_above()
        maingrid = Gtk.Grid()
        self.add(maingrid)
        maingrid.set_border_width(40)
        # set text for the spash window
        label = Gtk.Label(setup['static_ticker_message'])
        label.modify_font(Pango.FontDescription(font_and_size))
        maingrid.attach(label, 255, 255, 255, 1)

def splashwindow():
    window = Splash()
    window.set_decorated(False)
    window.set_resizable(False)
    window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(setup['static_ticker_bgcolor'][0],setup['static_ticker_bgcolor'][1],setup['static_ticker_bgcolor'][2]))
    window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse(setup['static_ticker_font_color']))
    if pos == "center":
        window.set_position(Gtk.WindowPosition.CENTER)
    else:
        window.set_position(Gtk.WindowPosition.MOUSE)
    window.show_all()
    Gtk.Window.set_keep_above()
    Gtk.main()

class SplashImage(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="splashtitle")
        maingrid = Gtk.Grid()
        self.add(maingrid)

        image = Gtk.Image()
        # set the path to the image below
        image.set_from_file("media/res_logo_gtk.png")
        maingrid.attach(image, 1, 0, 1, 1)

        maingrid.set_border_width(20)
        # set text for the spash window
        label = Gtk.Label(setup['static_ticker_message'])
        label.modify_font(Pango.FontDescription(font_and_size))
        maingrid.attach(label, 0, 0, 1, 1)

def splashwindowimage():
    window = SplashImage()
    window.set_decorated(False)
    window.set_resizable(False)
    window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(setup['static_ticker_bgcolor'][0],setup['static_ticker_bgcolor'][1],setup['static_ticker_bgcolor'][2]))
    window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse(setup['static_ticker_font_color']))
    window.set_opacity(0.8)
    if pos == "center":
        window.set_position(Gtk.WindowPosition.CENTER)
    else:
        window.set_position(Gtk.WindowPosition.MOUSE)
    window.show_all()

    Gtk.main()

if pos != "center":
    os.system(f"xdotool mousemove {setup['gtk_ticker_pos_x']} {setup['gtk_ticker_pos_y']}")
if setup['static_ticker_logo'] == True:
    splashwindowimage()
else:
    splashwindow()