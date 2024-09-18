import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings.theme import colors

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # PROGRAM
    # Browser
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Launch firefox"),
    # Code
    Key([mod, "shift"], "c", lazy.spawn("code"), desc="Launch code"),
    # Thunar
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch thunar"),
    # Menu
    Key([mod], "m", lazy.spawn("rofi -show-icons -show drun")),
    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),
    # Brightness Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),
    # Volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Screenshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
]
main = None
# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group(i)
    for i in [
        "   ",
        " 󰌠  ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
    ]
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        ]
    )

layout_conf = {
    # "border_focus": "#39FF14",
    "border_focus": "#39FF14",
    "border_width": 1,
    "margin": 6,
    # 'margin_y' : 10
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(**layout_conf),
    layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="victor-mono-nerd",
    fontsize=20,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg="text", bg="dark", fontsize=16, text="?"):
    return widget.TextBox(**base(fg, bg), fontsize=fontsize, text=text, padding=3)


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        # text="", # Icon: nf-oct-triangle_left
        text="",
        fontsize=35,
        padding=-1,
    )


screens = [
    Screen(
        top=bar.Bar(
            [
                separator(),
                widget.GroupBox(
                    **base(fg="light"),
                    font="victor-mono-nerd",
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=colors["active"],
                    inactive=colors["inactive"],
                    rounded=False,
                    highlight_method="block",
                    urgent_alert_method="block",
                    urgent_border=colors["urgent"],
                    this_current_screen_border=colors["focus"],
                    this_screen_border=colors["grey"],
                    other_current_screen_border=colors["dark"],
                    other_screen_border=colors["dark"],
                    disable_drag=True,
                ),
                separator(),
                widget.WindowName(**base(fg="focus"), fontsize=14, padding=5),
                separator(),
                powerline("color3", "dark"),
                icon(bg="color3", text=" "),  # Icon: nf-fa-feed
                widget.Net(**base(bg="color3"), interface="wlp2s0"),
                powerline("color2", "color3"),
                widget.CurrentLayoutIcon(**base(bg="color2"), scale=0.65),
                widget.CurrentLayout(**base(bg="color2"), padding=1),
                powerline("color1", "color2"),
                icon(
                    bg="color1", fontsize=17, text=" "
                ),  # Icon: nf-mdi-calendar_clock
                widget.Clock(**base(bg="color1"), format="%d/%m/%Y %a %H:%M "),
                powerline("dark", "color1"),
                widget.Systray(background=colors["dark"], padding=5),
                separator(),
            ],
            24,
            opacity=0.75,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                separator(),
                widget.GroupBox(
                    **base(fg='light'),
                        font='victor-mono-nerd',
                        fontsize=19,
                        margin_y=3,
                        margin_x=0,
                        padding_y=8,
                        padding_x=5,
                        borderwidth=1,
                        active=colors['active'],
                        inactive=colors['inactive'],
                        rounded=False,
                        highlight_method='block',
                        urgent_alert_method='block',
                        urgent_border=colors['urgent'],
                        this_current_screen_border=colors['focus'],
                        this_screen_border=colors['grey'],
                        other_current_screen_border=colors['dark'],
                        other_screen_border=colors['dark'],
                        disable_drag=True
                ),
                separator(),
                widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
                separator(),
                powerline('color2', 'dark'),
                widget.CurrentLayout(**base(bg='color2'), padding=1),
                # powerline('color1', 'color2'),
                # icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
                # widget.Clock(**base(bg='color1'), format="%d/%m/%Y %a %H:%M "),
                # powerline('dark', 'color1'),
            ],
            24,
            opacity = 0.75,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

