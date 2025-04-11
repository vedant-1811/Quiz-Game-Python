import tkinter as tk
from tkinter import messagebox

# Question data (can be expanded or loaded from JSON)
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who developed Python?",
        "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Steve Jobs"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "def", "define", "function"],
        "answer": "def"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    }
]

# Initial variables
current_q = 0
score = 0

# Functions
def load_question():
    question_label.config(text=questions[current_q]["question"])
    for i in range(4):
        option_buttons[i].config(text=questions[current_q]["options"][i])

def check_answer(index):
    global current_q, score
    selected = questions[current_q]["options"][index]
    correct = questions[current_q]["answer"]

    if selected == correct:
        score_label.config(text=f"Score: {score + 1}")
        score_up()
    else:
        score_label.config(text=f"Score: {score}")
    
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is: {score}/{len(questions)}")
        root.destroy()

def score_up():
    global score
    score += 1

# GUI setup
root = tk.Tk()
root.title("🧠 Quiz App")
root.geometry("500x400")
root.resizable(False, False)

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450, justify="center")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=20)

load_question()
root.mainloop()

