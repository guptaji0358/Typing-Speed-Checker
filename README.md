# Typing-Speed-Checker
DAY - 41 - Project - python X Typing Speed Checker

# ⌨️ Typing Master – Python Typing Speed Tester

A modern **Typing Speed Test application** built with **Python and CustomTkinter**.

This project measures:

- Typing Speed (WPM)
- Accuracy
- Real-time keyboard highlighting
- Cursor tracking while typing
- Dynamic word generation using API

This project was created during the **100 Days of Python – Day 41 Challenge**.

---

# 🚀 Features

## ⌨️ Real-Time Typing Test
- Highlights correct and incorrect characters
- Cursor moves automatically while typing
- Backspace correction supported
- Dynamic text expansion when words finish

## ⌨️ Visual Keyboard
- Full keyboard layout
- Keys highlight when pressed
- Includes numpad keys

## 🌐 Online Word Generator
Words are fetched from:


https://random-word-api.herokuapp.com


If the API fails, the program uses an **offline paragraph file**.

---

# 🎮 Difficulty Levels

| Level | Word Length |
|------|-------------|
| Easy | 3–5 letters |
| Medium | 5–8 letters |
| Hard | Any length |

---

# ⏱ Timer Options

Users can choose time in:

- Seconds
- Minutes
- Hours
- Days

---

# 📊 Result Calculation

After the test ends:


WPM = (Correct Characters / 5) / Minutes
Accuracy = (Correct Characters / Total Characters Typed) × 100


### Result Grades

| Grade | Condition |
|------|-----------|
| Excellent | WPM ≥ 60 and Accuracy ≥ 95% |
| Best | WPM ≥ 40 and Accuracy ≥ 90% |
| Good | WPM ≥ 25 and Accuracy ≥ 80% |
| Poor | Below above values |

---

# 🧩 Project Structure

All files should be placed **in the same folder**.


TypingMaster
│
├── 41_TYPING_MASTER.py
├── TYPING_MASTER_SPEED_CHECKER_API_WORDS.py
├── TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py
├── TYPING_MASTER_SPEED_CHECKER_UI.py
├── TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py
└── TYPING_MASTER_PARAGRAPH.txt


---

# 📂 Module Explanation

## Main Controller


41_TYPING_MASTER.py


Handles:

- Program state
- Timer
- Starting the test
- Connecting all modules together

---

## Word API Module


TYPING_MASTER_SPEED_CHECKER_API_WORDS.py


Handles:

- Word API requests
- Word filtering
- Paragraph generation

---

## Typing Logic


TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py


Handles:

- Key detection
- Cursor movement
- Correct / incorrect character detection
- Accuracy and WPM calculation

---

## User Interface


TYPING_MASTER_SPEED_CHECKER_UI.py


Handles:

- Window creation
- Menu interface
- Text display
- Timer display

---

## Keyboard UI


TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py


Handles:

- Visual keyboard layout
- Key highlighting

---

# 📄 Offline Paragraph File

The project includes a fallback text file:


TYPING_MASTER_PARAGRAPH.txt


This file is used when the API cannot fetch words.

Example content:


Typing practice improves speed and accuracy.
Consistent training helps develop keyboard muscle memory.


---

# ⚠️ ModuleNotFoundError / FileNotFoundError Fix

If you see errors like:


ModuleNotFoundError


or


FileNotFoundError


it usually means Python cannot find the project files.

### ✔ Correct Solution

Make sure **all project files are placed in the same folder**.


TypingMaster
│
├── 41_TYPING_MASTER.py
├── TYPING_MASTER_SPEED_CHECKER_API_WORDS.py
├── TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py
├── TYPING_MASTER_SPEED_CHECKER_UI.py
├── TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py
└── TYPING_MASTER_PARAGRAPH.txt


### ❌ Do NOT modify Python paths

You do **not need code like this**:


import sys
sys.path.append("some_folder")


Keeping all files in **one folder** is the recommended setup.

---

# 🖥 Requirements

- Python 3.10+
- CustomTkinter
- Requests

Install dependencies:


pip install customtkinter
pip install requests


---

# ▶️ Run the Program

Navigate to the project folder and run:


python 41_TYPING_MASTER.py


---

# 📚 Learning Goals

This project demonstrates:

- Python modular programming
- GUI development with CustomTkinter
- API integration
- Event-driven programming
- Keyboard event handling
- Real-time UI updates

---

# 📅 Project Progress

Part of:


100 Days of Python Challenge
Day 41 Project


---

# 👨‍💻 Author

**Robin Gupta**

Python Developer in Training 🚀
