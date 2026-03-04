# Typing-Speed-Checker
DAY - 41 - Project - python X Typing Speed Checker

# 📄 Offline Paragraph File

This project includes an offline paragraph file used when the word API is unavailable.

File name:


TYPING_MASTER_PARAGRAPH.txt


This file contains fallback text used by the typing engine. :contentReference[oaicite:0]{index=0}

Example content inside the file:


Third paragraph. Nisl purus in mollis nunc sed id semper risus. Ipsum a arcu cursus vitae congue mauris rhoncus aenean.
Ridiculus mus mauris vitae ultricies leo integer malesuada nunc. In tellus integer feugiat scelerisque.


---

## 📂 Where to place the file

Place the file in the same directory used in the code:


RawDataoftxt/TYPING_MASTER_PARAGRAPH.txt


Example structure:


TypingMaster
│
├── 41_TYPING_MASTER.py
├── TYPING_MASTER_SPEED_CHECKER_API_WORDS.py
├── TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py
├── TYPING_MASTER_SPEED_CHECKER_UI.py
├── TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py
│
└── RawDataoftxt
└── TYPING_MASTER_PARAGRAPH.txt


---

## 🧠 Why this file is needed

If the online word API fails or the internet is unavailable, the program will automatically load text from this file so the typing test can still run.

If you want, I can also give you a much more professional GitHub README (with badges, screenshots, demo GIF, and project banner) that makes the repository look like a real production project.

Sources
now full md

Here is the complete GitHub README.md including the paragraph file explanation and FileNotFoundError solution.
You can copy-paste directly into README.md.

# ⌨️ Typing Master – Python Typing Speed Tester

A modern **Typing Speed Test application** built using **Python and CustomTkinter**.

This project measures:

- Typing Speed (WPM)
- Accuracy
- Real-time keyboard highlighting
- Live cursor movement
- Dynamic word generation using API

This project was created during the **100 Days of Python – Day 41 challenge**.

---

# 🚀 Features

## ⌨️ Real-Time Typing Test
- Highlights correct and wrong characters
- Cursor moves dynamically while typing
- Backspace correction supported

## 🧠 Smart Word Generation
Words are fetched from an online API:


https://random-word-api.herokuapp.com


If the API fails, the program loads **offline text** from a local paragraph file.

## 🎮 Difficulty Levels

| Level | Word Length |
|------|-------------|
| Easy | 3–5 letters |
| Medium | 5–8 letters |
| Hard | Any length |

## ⏱ Timer Options

Users can choose time in:

- Seconds
- Minutes
- Hours
- Days

---

# 📊 Result Calculation

After the test ends the program calculates:


WPM = (Correct Characters / 5) / Minutes
Accuracy = (Correct Characters / Total Characters Typed) × 100


### Result Grades

| Grade | Condition |
|------|-----------|
| Excellent | WPM ≥ 60 and Accuracy ≥ 95% |
| Best | WPM ≥ 40 and Accuracy ≥ 90% |
| Good | WPM ≥ 25 and Accuracy ≥ 80% |
| Poor | Below the above values |

---

# 🧩 Project Structure


TypingMaster
│
├── 41_TYPING_MASTER.py
├── TYPING_MASTER_SPEED_CHECKER_API_WORDS.py
├── TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py
├── TYPING_MASTER_SPEED_CHECKER_UI.py
├── TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py
└── RawDataoftxt
└── TYPING_MASTER_PARAGRAPH.txt


---

# 📂 Module Explanation

### 1️⃣ Main Controller


41_TYPING_MASTER.py


Handles:

- Program state
- Timer
- Test start
- Connecting all modules together

---

### 2️⃣ Word API Module


TYPING_MASTER_SPEED_CHECKER_API_WORDS.py


Handles:

- Word API requests
- Word filtering by difficulty
- Paragraph generation

---

### 3️⃣ Typing Engine


TYPING_MASTER_SPEED_CHECKER_TYPING_LOGIC.py


Handles:

- Key detection
- Cursor movement
- Character validation
- Accuracy and WPM calculation

---

### 4️⃣ User Interface


TYPING_MASTER_SPEED_CHECKER_UI.py


Handles:

- Window creation
- Menu interface
- Textbox display
- Timer label

---

### 5️⃣ Keyboard UI


TYPING_MASTTER_SPEED_CHECKER_KEYBOARD_UI.py


Handles:

- Visual keyboard rendering
- Key highlighting system

---

# 📄 Offline Paragraph File

The project includes a fallback paragraph file:


TYPING_MASTER_PARAGRAPH.txt


This file contains typing text used when the API cannot fetch words.

Example content:


Third paragraph. Nisl purus in mollis nunc sed id semper risus.
Ipsum a arcu cursus vitae congue mauris rhoncus aenean.
Ridiculus mus mauris vitae ultricies leo integer malesuada nunc.


---

# ⚠️ FileNotFoundError Solution

If you see an error like:


FileNotFoundError: [Errno 2] No such file or directory


It means the program cannot find the offline paragraph file.

### Solution

Create the file:


RawDataoftxt/TYPING_MASTER_PARAGRAPH.txt


and place any paragraph text inside it.

Example:


Typing practice improves typing speed and accuracy.
Regular practice helps develop keyboard muscle memory.


---

# 🖥 Requirements

- Python 3.10+
- CustomTkinter
- Requests

Install dependencies:


pip install customtkinter
pip install requests


---

# ▶️ Run the Project


python 41_TYPING_MASTER.py


---

# 📚 Learning Goals

This project demonstrates:

- Python modular programming
- GUI development with CustomTkinter
- API integration
- Event-driven programming
- Real-time UI updates
- Keyboard event handling

---

# 📅 Project Progress

Part of:


100 Days of Python Challenge
Day 41 Project


---

# 👨‍💻 Author

**Robin Gupta**

Python Developer in Training 🚀
