BUTTON_FUNCS = ["switch_mode", "capture", "reset", "power"]
BUTTON_PINS = [18, 19, 20, 21]

MODES = ["Active", "Monitoring"]

COMPONENTS_FUNCS = [{"preview": True, "spy":True, "oled": True, "recog": False}, {"preview": False, "spy": False, "oled": False, "recog": True}]

RECORD_DUR = 30