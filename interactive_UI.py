from tkinter import *
from random import randint, choice

root = Tk()
root.geometry("800x600")
root.title("Maths Quiz App")
root.configure(bg="#f0f4f8")  # Light background color

# Variables
question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

def generateQuestion():
    global ques_lbl

    questionNumber.set(questionNumber.get() + 1)
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operator = choice(['+', '-', '*', '/'])
    question.set(f"{num_1} {operator} {num_2}")
    answer.set(eval(question.get()))

    if ques_lbl:
        ques_lbl.destroy()

    ques_lbl = Label(
        root,
        text=f"Question: {question.get()}",
        font=('Helvetica', 28, 'bold'),
        bg="#f0f4f8",
        fg="#333333"
    )
    ques_lbl.grid(row=3, column=0, columnspan=2, pady=20)

def checkAnswer():
    global score_lbl, result_lbl, submit_btn

    # If it's the 10th question, disable the submit button
    if questionNumber.get() == 10:
        submit_btn.config(state=DISABLED)  # Disable the submit button after the 10th question

    if result_lbl:
        result_lbl.destroy()

    # Check if the answer is correct
    if str(round(float(answer.get()), 2)) == str(round(float(givenAnswer.get()), 2)):
        score.set(score.get() + 1)
        result_lbl = Label(
            root,
            text="Correct!",
            font=('Helvetica', 18, 'bold'),
            fg='green',
            bg="#f0f4f8"
        )
    else:
        result_lbl = Label(
            root,
            text="Incorrect",
            font=('Helvetica', 18, 'bold'),
            fg='red',
            bg="#f0f4f8"
        )

    result_lbl.grid(row=6, column=0, columnspan=2, pady=10)

    # Update score label
    score_lbl.config(text=f"Score: {score.get()}")

    if questionNumber.get() == 10:
        score_lbl.config(text=f"Final Score: {score.get()}")  # Display final score after 10th question
    else:
        generateQuestion()  # Generate the next question

def restart():
    score.set(0)  # Reset score
    questionNumber.set(0)  # Reset question number
    submit_btn.config(state=NORMAL)  # Enable the submit button again
    generateQuestion()  # Generate the first question
    score_lbl.config(text=f"Score: {score.get()}")  # Reset the score display


# UI Components
Heading_lbl = Label(
    root,
    text="Maths Quiz",
    font=('Helvetica', 36, 'bold'),
    bg="#f0f4f8",
    fg="#0047ab"
)
Heading_lbl.grid(row=0, column=0, columnspan=2, pady=20)

questionScale = Scale(
    root,
    from_=0, to=10,
    length=500,
    orient=HORIZONTAL,
    variable=questionNumber,
    bg="#d7e3fc",
    troughcolor="#0056d8",
    highlightbackground="#f0f4f8"
)
questionScale.grid(row=1, column=0, columnspan=2, pady=10)

complete_quest_lbl = Label(
    root,
    text="10th Question",
    font=('Helvetica', 14),
    bg="#f0f4f8",
    fg="#555555"
)
complete_quest_lbl.grid(row=2, column=0, columnspan=2)

ques_lbl = Label(
    root,
    text="",
    font=('Helvetica', 28, 'bold'),
    bg="#f0f4f8",
    fg="#333333"
)
ques_lbl.grid(row=3, column=0, columnspan=2, pady=20)

answerEntry = Entry(
    root,
    textvariable=givenAnswer,
    font=('Helvetica', 20),
    width=20,
    bd=2,
    relief="groove"
)
answerEntry.grid(row=4, column=0, columnspan=2, pady=10)

submit_btn = Button(
    root,
    text="Submit",
    font=("Helvetica", 20, 'bold'),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    relief="flat",
    command=checkAnswer
)
submit_btn.grid(row=5, column=0, columnspan=2, pady=20)

result_lbl = Label(
    root,
    text="Result",
    font=('Helvetica', 18),
    bg="#f0f4f8",
    fg="#333333"
)
result_lbl.grid(row=6, column=0, columnspan=2, pady=10)

score_lbl = Label(
    root,
    text="Score: 0",
    font=('Helvetica', 18, 'bold'),
    bg="#f0f4f8",
    fg="#0047ab"
)
score_lbl.grid(row=7, column=0, columnspan=2, pady=10)

restart_btn = Button(
    root,
    text="Restart",
    font=("Helvetica", 20, 'bold'),
    bg="#f44336",
    fg="white",
    activebackground="#e53935",
    relief="flat",
    command=restart
)
restart_btn.grid(row=8, column=0, columnspan=2, pady=20)

generateQuestion()
root.mainloop()
