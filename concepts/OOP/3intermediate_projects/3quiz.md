### **Exercise B: Online Quiz** # wrong !
# Quiz → Question?
# Question → Answer?
# User → QuizAttempt?
# QuizAttempt → QuestionResponse?

# Task: When user takes quiz:
# 1. Who creates the QuizAttempt?
    -   quiz attempt is just storage so user initiates it
# 2. Who stores each answer?
    -   the answer object is told to store it by the quiz
# 3. Who calculates the score?
    -   quiz likely stores it in the user object

