from tkinter import *

# get_next_question 함수를 도와주기위한 import 실질적으로
# quiz = QuizBrain(question_bank)
# quiz_ui = QuizInterface(quiz)
# 이 두 줄을 사용해도 되나 실수 방지 + 자동완성 도움을 위해서 import
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)
        self.score_label = Label(text=f"score: {quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 120,
                                                     width=280,
                                                     text="Some Quiz text",
                                                     fill=THEME_COLOR, font = ("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, command=self.true_button, highlightthickness=0)
        worng_image = PhotoImage(file="images/false.png")
        self.worng_button = Button(image=worng_image, command=self.false_button, highlightthickness=0)
        self.right_button.grid(column=0, row=2)
        self.worng_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text = f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.worng_button.config(state="disabled")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
