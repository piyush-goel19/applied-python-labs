from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(self.window, text=f"Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, bg="white", width=300, height=250, highlightthickness=0)
        self.ques_text = self.canvas.create_text(150, 125, text="Ques goes here.",
                                                 font=("Arial", 20, "italic"),
                                                 fill=THEME_COLOR, width=300, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, command=lambda: self.check_answer("False"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=question_text)
        else:
            self.canvas.itemconfig(self.ques_text, text=f"Quiz Over! Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def check_answer(self, answer):
        feedback = self.quiz.check_answer(answer)
        if feedback == "True":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)