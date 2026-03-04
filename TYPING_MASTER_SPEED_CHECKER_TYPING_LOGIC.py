from typing import Callable, Dict, Any


def build_typing_logic(
    state: Dict[str, Any],
    ui: Dict[str, Any],
    key_buttons: Dict[str, Any],
    set_key_default_style: Callable[[str], None],
    append_new_words: Callable[[], None],
):
    text_display = ui["text_display"]
    result_label = ui["result_label"]
    window = ui["window"]

    def get_lookup_key(event):
        pressed_key = event.keysym.lower()

        special_map = {
            "space": "space",
            "backspace": "backspace",
            "return": "enter",
            "tab": "tab",
            "caps_lock": "capslock",
            "control_l": "ctrl",
            "control_r": "ctrl",
            "alt_l": "alt",
            "alt_r": "alt",
            "super_l": "win",
            "super_r": "win",
            "menu": "menu",
            "shift_l": "shift",
            "shift_r": "shift",
            "escape": "esc",
            "minus": "-",
            "equal": "=",
            "bracketleft": "[",
            "bracketright": "]",
            "backslash": "\\",
            "semicolon": ";",
            "apostrophe": "'",
            "comma": ",",
            "period": ".",
            "slash": "/",
            "grave": "`",
            "num_lock": "numlock",
            "kp_enter": "numenter",
            "kp_0": "num0",
            "kp_1": "num1",
            "kp_2": "num2",
            "kp_3": "num3",
            "kp_4": "num4",
            "kp_5": "num5",
            "kp_6": "num6",
            "kp_7": "num7",
            "kp_8": "num8",
            "kp_9": "num9",
            "kp_decimal": "num.",
            "kp_divide": "num/",
            "kp_multiply": "num*",
            "kp_subtract": "num-",
            "kp_add": "num+",
        }

        if pressed_key in special_map:
            return special_map[pressed_key]

        if pressed_key.startswith("f") and pressed_key[1:].isdigit():
            return pressed_key

        if event.char:
            return event.char.lower()

        if pressed_key in key_buttons:
            return pressed_key

        return None

    def move_cursor():
        position = f"1.0+{state['current_index']}c"
        text_display._textbox.mark_set("insert", position)
        text_display._textbox.see(position)

    def update_cursor():
        text_display.tag_remove("current_char", "1.0", "end")
        start = f"1.0+{state['current_index']}c"
        end = f"1.0+{state['current_index'] + 1}c"
        text_display.tag_add("current_char", start, end)

    def should_append_words():
        remaining_text = state["sample_text"][state["current_index"]:]
        remaining_words = remaining_text.split()
        return len(remaining_words) <= 3

    def calculate_results():
        total_typed = state["correct_chars"] + state["wrong_chars"]
        if total_typed == 0 or state["initial_time"] == 0:
            return

        minutes = state["initial_time"] / 60
        wpm = (state["correct_chars"] / 5) / minutes
        accuracy = (state["correct_chars"] / total_typed) * 100

        grade_text = "Poor"
        if wpm >= 60 and accuracy >= 95:
            grade_text = "Excellent"
        elif wpm >= 40 and accuracy >= 90:
            grade_text = "Best"
        elif wpm >= 25 and accuracy >= 80:
            grade_text = "Good"

        result_label.configure(
            text=f"WPM: {round(wpm, 2)}   |   Accuracy: {round(accuracy, 2)}%\\nResult: {grade_text}"
        )

    def check_typing(event):
        lookup_key = get_lookup_key(event)

        if event.keysym == "Escape":
            window.attributes("-fullscreen", False)
            return "break"

        if lookup_key in key_buttons:
            key_buttons[lookup_key].configure(fg_color="#00E5A8", border_color="#77FFD8")

            def reset_key(k=lookup_key):
                if k in key_buttons:
                    set_key_default_style(k)

            window.after(150, reset_key)

        if event.keysym in ["Left", "Right", "Up", "Down"]:
            return "break"

        if event.keysym == "BackSpace":
            if state["current_index"] > 0:
                state["current_index"] -= 1
                move_cursor()

                start = f"1.0+{state['current_index']}c"
                end = f"1.0+{state['current_index'] + 1}c"

                if "correct" in text_display.tag_names(start):
                    state["correct_chars"] -= 1
                if "wrong" in text_display.tag_names(start):
                    state["wrong_chars"] -= 1

                text_display.tag_remove("correct", start, end)
                text_display.tag_remove("wrong", start, end)

            return "break"

        if len(event.char) == 0:
            return "break"

        if state["current_index"] >= len(state["sample_text"]):
            return "break"

        expected_char = state["sample_text"][state["current_index"]]
        typed_char = event.char

        start = f"1.0+{state['current_index']}c"
        end = f"1.0+{state['current_index'] + 1}c"

        if typed_char == expected_char:
            text_display.tag_add("correct", start, end)
            state["correct_chars"] += 1
        else:
            text_display.tag_add("wrong", start, end)
            state["wrong_chars"] += 1

        text_display.tag_config("correct", foreground="#00FF88")
        text_display.tag_config("wrong", foreground="#FF4C4C")

        if should_append_words():
            append_new_words()

        state["current_index"] += 1
        move_cursor()
        return "break"

    return {
        "get_lookup_key": get_lookup_key,
        "check_typing": check_typing,
        "move_cursor": move_cursor,
        "update_cursor": update_cursor,
        "should_append_words": should_append_words,
        "calculate_results": calculate_results,
    }
