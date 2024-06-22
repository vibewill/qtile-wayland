

from typing import List  # noqa: F401
import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.nett(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Meus apps
    Key([mod],  "g"    , lazy.spawn("google-chrome"), desc="Navegador"),
    Key([mod],  "d"    , lazy.spawn("wofi --show drun"), desc="Menu"),
    Key([mod],  "f"    , lazy.spawn("nemo"), desc="Arquivos"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [ Group(str(i)) for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)]





for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Tile(margin = 15),
    layout.Columns(border_focus_stack='#d75f5f',
        margin = 2,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(margin = 2),
    layout.Matrix(margin = 2),
    layout.MonadTall(margin = 2),
    layout.MonadWide(margin = 2),
    layout.RatioTile(margin = 2),
    layout.TreeTab(),
    layout.VerticalTile(margin = 2),
    layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(
                    foreground = "#3b3eeb",
                    font = 'fontawesome',
                    fontsize = 13,
                    format = '{state}{name}',
                    for_current_screen = False,
                    empty_group_string = ' ',
                    padding = None,
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(),
                widget.TextBox(),
                widget.Cmus(
                    font = 'fontawesome',
                    fontsize = 13,
                    fontshadow = None,
                    foreground = 'ffffff',
                    markup = True,
                    max_chars = 0,
                    mouse_callbacks = {},
                    noplay_color = 'cecece',
                    padding = None,
                    play_color = '00ff00',
                    update_interval = 0.5,
                ),

                widget.KeyboardLayout(
                    configured_keyboards = ['br'],
                    display_map = {},
                    fmt = '{}',
                    font = 'fontawesome',
                    fontsize = 13,
                    foreground = "#f0ec0a",
                    mouse_callbacks = {},
                    option = None,
                    update_interval = 1,

                ),
                widget.Net(
                    format = ' {down} ↓↑ {up}',
                    interface = None,
                    font = 'fontawesome',
                    fontsize = 13,
                    foreground = '#4feb44',
                    update_interval = 1,

                ),

                widget.Memory(
                    
                    font = 'fontawesome',
                    format = ' {MemUsed}M/{MemTotal}M',
                    update_interval = 0.1,
                    fontsize = 13,
                    foreground = '#f0280a',
                    background = None,
                ),
                

                widget.CPU(
                    format = ' {freq_current}GHz {load_percent}%',
                    font = 'fontawesome',
                    fontsize = 13,
                    foreground = '#0af0e4',
                    background = None,
                    fmt = '{}',
                    update_interval = 3,

                ),
            
                widget.Clock(
                    foreground = "#f00aec",
                    format='%Y-%m-%d %a %I:%M %p',
                    font = 'fontawesome',
                    fontsize = 13,
                ),
                

                widget.Volume(
                    cardid = None,
                    channel = 'Master',
                    device = 'default',
                    emoji = True,
                    get_volume_command = None,
                    mouse_callbacks = {},
                    mute_command = None,
                    step = 2,
                    update_interval = 0.1,
                    volume_app = None,
                    font = 'fontawesome',
                    fontsize = 13,
                ),

                widget.Systray(), 
                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Start com linux
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

wmname = "qtile"
