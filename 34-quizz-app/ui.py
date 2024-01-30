from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # ----------------------------------------------- WINDOW
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=340, height=500)

        # ----------------------------------------------- LABEL
        self.score_label = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
            font=(FONT_NAME, 16),
        )
        self.score_label.grid(row=0, column=1)

        # ----------------------------------------------- CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,  # In order to wrap the question text
            text="Question",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # ----------------------------------------------- BUTTONS
        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=lambda: self.answer_selected(True),
        )
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=lambda: self.answer_selected(False),
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_text, text="You have reached the end of the quiz!"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_selected(self, answer: bool):
        self.give_feed_back(self.quiz.check_answer(str(answer)))

    def give_feed_back(self, is_response_correct):
        if is_response_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
