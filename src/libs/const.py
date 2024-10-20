# feh image reader keybindings
KEYS = {
    "up": ("ctrl", "up"),
    "down": ("ctrl", "down"),
    "left": ("ctrl", "left"),
    "right": ("ctrl", "right"),
    "zoom_in": ("", "up"),
    "zoom_out": ("", "down"),
    "next": ("", "right"),
    "previous": ("", "left"),
}


CMDS = {
    "stop": "utils.setKeepPressing(False)",
    "close": "utils.kill(imageProgram.pid)",
}
