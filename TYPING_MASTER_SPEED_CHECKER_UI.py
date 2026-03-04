import customtkinter as ctk


def build_ui(start_test_cb, check_typing_cb):
    window = ctk.CTk()
    window.geometry("1280x820")
    window.title("Typing Master")
    window.withdraw()

    menu_popup = ctk.CTkToplevel(window)
    menu_popup.title("Typing Master - Menu")
    menu_popup.geometry("520x420")
    menu_popup.resizable(False, False)
    menu_popup.attributes("-topmost", True)
    menu_popup.grab_set()
    menu_popup.focus_force()

    screen_w = menu_popup.winfo_screenwidth()
    screen_h = menu_popup.winfo_screenheight()
    popup_x = (screen_w // 2) - 260
    popup_y = (screen_h // 2) - 210
    menu_popup.geometry(f"520x420+{popup_x}+{popup_y}")

    menu_frame = ctk.CTkFrame(menu_popup)
    menu_frame.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        menu_frame,
        text="Typing Master",
        font=("Arial Black", 30, "italic"),
    )
    title.pack(pady=20)

    settings_frame = ctk.CTkFrame(menu_frame)
    settings_frame.pack(pady=20)

    level_frame = ctk.CTkFrame(settings_frame)
    level_frame.pack(pady=10)
    ctk.CTkLabel(level_frame, text="Select Level").pack(side="left", padx=10)

    level_dropdown = ctk.CTkOptionMenu(level_frame, values=["Easy", "Medium", "Hard"])
    level_dropdown.set("Easy")
    level_dropdown.pack(side="left", padx=10)

    time_frame = ctk.CTkFrame(settings_frame)
    time_frame.pack(pady=10)
    ctk.CTkLabel(time_frame, text="Select Time").pack(side="left", padx=10)

    time_entry = ctk.CTkEntry(time_frame, width=80)
    time_entry.pack(side="left", padx=10)
    time_entry.insert(0, "60")

    time_unit_dropdown = ctk.CTkOptionMenu(
        time_frame,
        values=["Seconds", "Minutes", "Hours", "Days"],
    )
    time_unit_dropdown.set("Seconds")
    time_unit_dropdown.pack(side="left", padx=10)

    start_test = ctk.CTkButton(
        menu_frame,
        text="Start Test",
        command=start_test_cb,
        width=200,
        height=40,
    )
    start_test.pack(pady=20)

    test_frame = ctk.CTkFrame(window)

    test_label = ctk.CTkLabel(test_frame, text="TEST MODE", font=("Arial Black", 30))
    test_label.pack(pady=10)

    timmer_label = ctk.CTkLabel(
        test_frame,
        text="00:00:00",
        font=("Arial", 36),
        text_color="#3B8ED0",
    )
    timmer_label.pack(pady=6)

    result_label = ctk.CTkLabel(
        test_frame,
        text="",
        font=("Arial", 20),
        text_color="#00FFAA",
    )
    result_label.pack(pady=4)

    text_display = ctk.CTkTextbox(
        test_frame,
        width=1040,
        height=170,
        corner_radius=24,
        border_width=3,
        border_color="#00C2FF",
        fg_color="#141822",
        font=("Cascadia Code", 20, "bold"),
        wrap="word",
    )

    def focus_textbox_on_click(event):
        text_display._textbox.focus_force()
        return "break"

    text_display.bind("<Button-1>", focus_textbox_on_click)

    real_textbox = text_display._textbox
    real_textbox.config(
        insertwidth=4,
        insertbackground="#00FFFF",
        insertofftime=400,
        insertontime=600,
    )

    text_display.pack(pady=8, padx=24)
    text_display.bind("<KeyPress>", check_typing_cb)
    text_display._textbox.bind("<KeyPress>", check_typing_cb)
    text_display.tag_config("current_char", background="#26384E", foreground="#FFFFFF")

    window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

    return {
        "window": window,
        "menu_popup": menu_popup,
        "menu_frame": menu_frame,
        "test_frame": test_frame,
        "level_dropdown": level_dropdown,
        "time_entry": time_entry,
        "time_unit_dropdown": time_unit_dropdown,
        "timmer_label": timmer_label,
        "result_label": result_label,
        "text_display": text_display,
        "real_textbox": real_textbox,
        "start_test_button": start_test,
    }
