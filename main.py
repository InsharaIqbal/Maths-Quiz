from tkinter import *

from random import randint, choice
root= Tk()
root.geometry("500x500")
root.title("Maths Quiz app")



question=StringVar()
answer=StringVar()
givenAnswer=StringVar()
score=IntVar()
questionNumber=IntVar()

def generateQuestion():
    
    global ques_lbl

    questionNumber.set(questionNumber.get()+1)
    num_1=randint(1,10)
    num_2=randint(1,10)

    operator=choice(['+', '-', '*','/'])
    question.set(str(num_1) +operator +str(num_2))
    answer.set(eval(question.get()))

    if ques_lbl:
        ques_lbl.destroy()

    ques_lbl=Label(root, text=f"Question : {question.get()}", font=('Arial', 30))
    ques_lbl.grid(row=3, column=0)
    

def checkAnswer():
    global result_lbl
    if result_lbl:
        result_lbl.destroy()
        

    if str(answer.get())==givenAnswer.get():
        score.set(score.get()+1)
        result_lbl=Label(root, text="Correct", font=('Arial', 16),fg='green')
        result_lbl.grid(row=6, column=0)
        score_lbl=Label(root, text=f"Score: {score.get()}", font=('Arial', 16), fg='blue')
        score_lbl.grid(row=7, column=0)
    else:
      
        result_lbl=Label(root, text="Incorrect", font=('Arial', 16), fg='red')
        result_lbl.grid(row=6, column=0)


    generateQuestion()
        






#UI
Heading_lbl=Label(root,text= "Maths Quiz", font=('Arial', 30, 'bold'), fg=('blue'))
Heading_lbl.grid(row=0, column=0)

questionScale= Scale(root, from_=0, to=10, length=400, orient=HORIZONTAL, variable=questionNumber)
questionScale.grid(row=1, column=0)

complete_quest_lbl= Label(root, text="10th Question")
complete_quest_lbl.grid(row=1, column=0)


ques_lbl=Label(root, text=question.get(), font=('Arial', 30))
ques_lbl.grid(row=3, column=0)

answerEntry= Entry(root,textvariable=givenAnswer, font=('Arial', 20))
answerEntry.grid(row=4, column=0)

submit_btn=Button(root, text="submit", font=("Arial", 20 ),fg=('purple'), command=checkAnswer)
submit_btn.grid(row=5, column=3)



result_lbl=Label(root, text="Result", font=('Arial', 16), fg='blue')
result_lbl.grid(row=6, column=0)

score_lbl=Label(root, text=f"Score: {score.get()}", font=('Arial', 16), fg='blue')
score_lbl.grid(row=7, column=0)



root.mainloop()