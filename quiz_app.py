import tkinter as tk
from tkinter import messagebox
import random

# Predefined list of questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Lists",
        "question": "What is the output of the following code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "IndexError"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "What does the following code output?",
        "code": "print('Hello' + 'World')",
        "options": ["Hello", "World", "HelloWorld", "Error"],
        "answer": 2
    }
]

# Functionality for the app
def generate_question():
    topic = topic_entry.get().strip()
    if not topic:
        messagebox.showerror("Error", "Please enter a topic.")
        return

    filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
    if not filtered_questions:
        messagebox.showerror("Error", f"No questions found for topic: {topic}")
        return

    global current_question
    current_question = random.choice(filtered_questions)

    # Display question details
    topic_label.config(text=f"Topic: {current_question['topic']}")
    question_label.config(text=f"Question: {current_question['question']}")
    code_label.config(text=f"Code:\n{current_question['code']}")

    # Update options
    for i, option in enumerate(current_question['options']):
        option_buttons[i].config(text=option, value=i)

    feedback_label.config(text="")

def submit_answer():
    selected_option = selected_option_var.get()
    if selected_option == -1:
        messagebox.showerror("Error", "Please select an answer.")
        return

    if selected_option == current_question['answer']:
        feedback_label.config(text="Correct! Well done!", fg="green")
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red")

# Initialize the GUI app
app = tk.Tk()
app.title("Python Quiz Generator")
app.geometry("500x400")

# Input field for topic
tk.Label(app, text="Enter Python Topic:").pack(pady=5)
topic_entry = tk.Entry(app)
topic_entry.pack(pady=5)

# Button to generate a question
generate_button = tk.Button(app, text="Generate Python Question", command=generate_question)
generate_button.pack(pady=10)

# Display area for question details
topic_label = tk.Label(app, text="", font=("Arial", 12, "bold"))
topic_label.pack(pady=5)
question_label = tk.Label(app, text="", wraplength=400)
question_label.pack(pady=5)
code_label = tk.Label(app, text="", font=("Courier", 10), wraplength=400)
code_label.pack(pady=5)

# Radio buttons for answer options
selected_option_var = tk.IntVar(value=-1)
option_buttons = []
for i in range(4):
    rb = tk.Radiobutton(app, text="", variable=selected_option_var, value=i)
    rb.pack(anchor="w")
    option_buttons.append(rb)

# Submit button
submit_button = tk.Button(app, text="Submit", command=submit_answer)
submit_button.pack(pady=10)

# Feedback area
feedback_label = tk.Label(app, text="", font=("Arial", 10))
feedback_label.pack(pady=5)

# Start the app
app.mainloop()