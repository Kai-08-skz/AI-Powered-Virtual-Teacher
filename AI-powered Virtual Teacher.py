import random
from tkinter import *

# Global variable for the correct answer and the score
correct_answer = ""
score = 0
questions_asked = 0

# Function to ask a quiz question
def ask_quiz_question():
    global correct_answer, questions_asked  # Declare as global to modify its value

    questions = [
        ("What is the capital of France?", "paris"),
        ("Who wrote 'Romeo and Juliet'?", "shakespeare"),
        ("What is the largest planet in our solar system?", "jupiter"),
        ("What is the square root of 16?", "4"),
        ("What is the atomic number of oxygen?", "8")
    ]
    
    # Randomly choose a question and set the correct answer
    question, correct_answer = random.choice(questions)
    
    # Display the question
    question_label.config(text=question)

    # Enable the answer entry and submit button
    answer_entry.config(state=NORMAL)
    submit_button.config(state=NORMAL)
    
    # Disable the start button after the quiz starts
    start_button.config(state=DISABLED)

# Function to check the answer
def check_answer():
    global score, questions_asked  # Declare as global to modify its value
    answer = answer_entry.get().lower().strip()  # Get and clean the answer
    
    # Increment the question count
    questions_asked += 1

    # Check if the answer is correct
    if answer == correct_answer:
        score += 1
        result_label.config(text="Correct! Well done!", fg="green")
    else:
        result_label.config(text=f"Oops! The correct answer is {correct_answer}.", fg="red")
    
    # Clear the answer entry
    answer_entry.delete(0, END)
    
    # Show a new question after a delay
    root.after(1000, ask_quiz_question)

    # Show fun fact or joke after answer
    show_fun_fact_or_joke()

    # After a few questions, display the final score
    if questions_asked >= 5:
        show_final_score()

# Function to show the final score
def show_final_score():
    final_score_label.config(text=f"Your Final Score is: {score}/5", fg="blue")

# Function to show a fun fact or a joke after the answer
def show_fun_fact_or_joke():
    facts_and_jokes = [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
        "Here's a joke: Why don't skeletons fight each other? They don't have the guts!",
        "Fun Fact: A day on Venus is longer than a year on Venus!",
        "Joke: Why did the computer go to the doctor? It had a virus!"
    ]
    fun_fact_or_joke_label.config(text=random.choice(facts_and_jokes))

# Function to start the lesson
def start_lesson():
    global score, questions_asked
    score = 0
    questions_asked = 0
    ask_quiz_question()

# Function to show greeting and initialize the UI
def show_greeting():
    global root, start_button  # Make start_button global

    root = Tk()
    root.title("Interactive AI Virtual Teacher")
    root.geometry("600x400")

    greeting_label = Label(root, text="Hello! I am your AI Teacher. Let's start learning!", font=("Helvetica", 16))
    greeting_label.pack(pady=30)

    start_button = Button(root, text="Start Quiz", command=start_lesson, font=("Helvetica", 14))
    start_button.pack(pady=20)

    global question_label
    question_label = Label(root, text="", font=("Helvetica", 14), height=2)
    question_label.pack(pady=20)

    global answer_entry
    answer_entry = Entry(root, font=("Helvetica", 14), state=DISABLED)
    answer_entry.pack(pady=10)

    global submit_button
    submit_button = Button(root, text="Submit Answer", command=check_answer, font=("Helvetica", 14), state=DISABLED)
    submit_button.pack(pady=20)

    global result_label
    result_label = Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=20)

    global fun_fact_or_joke_label
    fun_fact_or_joke_label = Label(root, text="", font=("Helvetica", 12), fg="blue")
    fun_fact_or_joke_label.pack(pady=10)

    global final_score_label
    final_score_label = Label(root, text="", font=("Helvetica", 14), fg="blue")
    final_score_label.pack(pady=20)

    root.mainloop()

# Main execution
if __name__ == "__main__":
    show_greeting()

