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

# To be called inside MAIN(DIM) so always use self to call its methods
# NOT DIM.
CMDS = {
    "open": "self.open_image()",
    "stop": "utils.setKeepPressing(False)",
    "close": "utils.kill(self.imageProgram.pid)",
}
