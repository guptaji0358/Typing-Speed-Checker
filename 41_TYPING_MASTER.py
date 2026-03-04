import sys
import customtkinter as ctk

module_path = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpy"
if module_path not in sys.path:
    sys.path.append(module_path)

from TYPING_MASTER_SPEED_CHECKER_API_WORDS import (
    Build_a_Paragraph,
    Filter_as_words,
    Get_Online_API_Words,
)
from TYPING_MASTER_SPEED_CHECKER_UI import build_ui
from TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI import build_keyboard
from TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC import build_typing_logic

ctk.set_appearance_mode("Dark")

state = {
    "remaining_time": 0,
    "current_index": 0,
    "correct_chars": 0,
    "wrong_chars": 0,
    "initial_time": 0,
    "sample_text": "",
}


def set_key_default_style(key):
    if key in key_buttons:
        key_buttons[key].configure(fg_color="#232A39", border_color="#2E3750")


def fetch_and_append():
    new_words = Get_Online_API_Words(15)
    if not new_words:
        return

    new_text = " " + " ".join(new_words)
    text_display.insert("end", new_text)
    state["sample_text"] += new_text


def append_new_words():
    window.after(1, fetch_and_append)


def ensure_typing_focus():
    text_display._textbox.focus_force()
    logic["move_cursor"]()


def Update_Timmr():
    if state["remaining_time"] > 0:
        h = state["remaining_time"] // 3600
        m = (state["remaining_time"] % 3600) // 60
        s = state["remaining_time"] % 60

        timmer_label.configure(text=f"{h:02}:{m:02}:{s:02}")
        state["remaining_time"] -= 1
        window.after(1000, Update_Timmr)
    else:
        timmer_label.configure(text="Time Up!")
        text_display.unbind("<KeyPress>")
        text_display._textbox.unbind("<KeyPress>")
        logic["calculate_results"]()
        try_again_button.pack(pady=8)


def StartTest():
    state["current_index"] = 0
    state["correct_chars"] = 0
    state["wrong_chars"] = 0

    result_label.configure(text="")
    try_again_button.pack_forget()

    text_display.bind("<KeyPress>", logic["check_typing"])
    text_display._textbox.bind("<KeyPress>", logic["check_typing"])

    level = Level_dropdown.get()
    time_value = time_entry.get() if time_entry.winfo_exists() else "60"
    time_unit = time_unit_dropdown.get()

    if time_value == "":
        time_value = 60
    else:
        try:
            time_value = int(time_value)
        except ValueError:
            time_value = 60

    multiplier = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
    }

    total_seconds = time_value * multiplier.get(time_unit, 1)
    state["remaining_time"] = total_seconds
    state["initial_time"] = total_seconds

    minutes = total_seconds / 60
    words_needed = min(int(minutes * 40), 800)

    raw_words = Get_Online_API_Words(words_needed)
    filtered_words = Filter_as_words(raw_words, level)
    if not filtered_words:
        filtered_words = raw_words

    filtered_words = filtered_words[:words_needed]
    state["sample_text"] = Build_a_Paragraph(filtered_words)

    text_display.delete("1.0", "end")
    text_display.insert("1.0", state["sample_text"])
    text_display.tag_remove("correct", "1.0", "end")
    text_display.tag_remove("wrong", "1.0", "end")
    text_display._textbox.focus_force()

    if menu_popup.winfo_exists():
        menu_popup.destroy()

    window.deiconify()
    window.attributes("-fullscreen", True)
    Test_Frame.pack(fill="both", expand=True)

    logic["update_cursor"]()
    logic["move_cursor"]()

    window.after(120, ensure_typing_focus)
    window.after(260, ensure_typing_focus)

    Update_Timmr()


def TryAgain():
    StartTest()


def close_app():
    window.destroy()


ui_refs = build_ui(lambda: None, lambda e: "break")
window = ui_refs["window"]
menu_popup = ui_refs["menu_popup"]
Test_Frame = ui_refs["test_frame"]
Level_dropdown = ui_refs["level_dropdown"]
time_entry = ui_refs["time_entry"]
time_unit_dropdown = ui_refs["time_unit_dropdown"]
timmer_label = ui_refs["timmer_label"]
result_label = ui_refs["result_label"]
text_display = ui_refs["text_display"]

keyboard_refs = build_keyboard(Test_Frame)
key_buttons = keyboard_refs["key_buttons"]

logic = build_typing_logic(
    state=state,
    ui=ui_refs,
    key_buttons=key_buttons,
    set_key_default_style=set_key_default_style,
    append_new_words=append_new_words,
)

ui_refs["start_test_button"].configure(command=StartTest)
text_display.bind("<KeyPress>", logic["check_typing"])
text_display._textbox.bind("<KeyPress>", logic["check_typing"])
menu_popup.protocol("WM_DELETE_WINDOW", close_app)

try_again_button = ctk.CTkButton(
    Test_Frame,
    text="Try Again",
    command=TryAgain,
    width=180,
    height=36,
)

window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))
window.mainloop()