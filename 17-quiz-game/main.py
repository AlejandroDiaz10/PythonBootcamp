# https://replit.com/@appbrewery/quiz-game-start

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of question objects from the question_data.
game_questions = [
    Question(question["question"], question["correct_answer"])
    for question in question_data
]

# Create a QuizBrain object.
quiz = QuizBrain(game_questions)

# While there are still questions in the quiz, ask the next question.
while quiz.still_has_questions():
    quiz.next_question()

# When the quiz is over, print the final score.
quiz.final_score()
