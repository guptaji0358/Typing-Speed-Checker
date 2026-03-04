import customtkinter as ctk


def build_keyboard(test_frame):
    main_keyboard_layout = [
        ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"],
        ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BackSpace"],
        ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
        ["CapsLock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"],
        ["Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Shift"],
        ["Ctrl", "Win", "Alt", "Space", "Alt", "Menu", "Ctrl"],
    ]

    numpad_layout = [
        ["NumLock", "Num/", "Num*", "Num-"],
        ["Num7", "Num8", "Num9", "Num+"],
        ["Num4", "Num5", "Num6", "Num+"],
        ["Num1", "Num2", "Num3", "NumEnter"],
        ["Num0", "Num.", "NumEnter"],
    ]

    key_buttons = {}

    keyboard_container = ctk.CTkFrame(test_frame)
    keyboard_container.pack(pady=6)
    keyboard_container.pack_configure(anchor="center")

    keyboard_frame = ctk.CTkFrame(keyboard_container)
    keyboard_frame.pack(side="left", padx=8, pady=6)

    numpad_frame = ctk.CTkFrame(keyboard_container)
    numpad_frame.pack(side="left", padx=8, pady=6)

    for row in main_keyboard_layout:
        row_frame = ctk.CTkFrame(keyboard_frame)
        row_frame.pack(pady=2)

        for key in row:
            width = 30
            if key == "Space":
                width = 230
            elif key in ["BackSpace", "Shift", "Enter", "CapsLock"]:
                width = 62
            elif key == "Tab":
                width = 50
            elif key in ["Ctrl", "Win", "Alt", "Menu"]:
                width = 44

            btn = ctk.CTkButton(
                row_frame,
                text=key,
                width=width,
                height=30,
                fg_color="#232A39",
                border_width=1,
                border_color="#2E3750",
                corner_radius=8,
                text_color="#E8F2FF",
                hover=False,
            )

            btn.pack(side="left", padx=2)
            lookup_name = key.lower()
            if key == "CapsLock":
                lookup_name = "capslock"
            key_buttons[lookup_name] = btn

    for row in numpad_layout:
        row_frame = ctk.CTkFrame(numpad_frame)
        row_frame.pack(pady=2)

        for key in row:
            width = 42
            if key == "Num0":
                width = 86

            btn = ctk.CTkButton(
                row_frame,
                text=key,
                width=width,
                height=30,
                fg_color="#232A39",
                border_width=1,
                border_color="#2E3750",
                corner_radius=8,
                text_color="#E8F2FF",
                hover=False,
            )

            btn.pack(side="left", padx=2)
            key_buttons[key.lower()] = btn

    return {
        "keyboard_container": keyboard_container,
        "keyboard_frame": keyboard_frame,
        "numpad_frame": numpad_frame,
        "key_buttons": key_buttons,
    }
