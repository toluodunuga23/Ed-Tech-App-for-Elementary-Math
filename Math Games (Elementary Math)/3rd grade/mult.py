from tkinter import *
import random

class MultiplicationQuiz:
    def __init__(self):
        self.window = Tk()
        self.window.title("Multiplication Quiz")
        self.score = 0

        # Add a timer
        self.time_left = 230
        self.timer = Label(self.window, text=f"Time left: {self.time_left}", font=("Helvetica", 20))
        self.timer.pack(pady=20)

        self.equation = Label(self.window, text="", font=("Helvetica", 24))
        self.equation.pack(pady=20)

        self.answer = Entry(self.window, font=("Helvetica", 24))
        self.answer.pack(pady=20)

        self.submit = Button(self.window, text="Submit", font=("Helvetica", 16), command=self.check_answer)
        self.submit.pack(pady=20)

        # Add a score tracker
        self.score_label = Label(self.window, text=f"Score: {self.score}", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

        self.feedback = Label(self.window, text="", font=("Helvetica", 20))
        self.feedback.pack(pady=20)

        self.new_question()

        # Call the countdown function
        self.countdown()

        # Center the window on the screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        mainloop()

    def new_question(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        self.answer.delete(0, END)
        self.equation.config(text=f"{num1} x {num2} = ")
        self.correct_answer = num1 * num2

    def check_answer(self):
        guess = int(self.answer.get())
        if guess == self.correct_answer:
            self.feedback.config(text="Correct!")
            self.score += 1
            # Update the score tracker
            self.score_label.config(text=f"Score: {self.score}")
            self.new_question()
        else:
            self.feedback.config(text="Incorrect.")
            self.feedback.config(text="Incorrect. The correct answer was " + str(self.correct_answer))
            
        
            
            self.new_question()

    # Add a timer function
    def countdown(self):
        if self.time_left > 0:
            # Update the timer label
            self.timer.config(text=f"Time left: {self.time_left}")
            # Decrement the time left variable
            self.time_left -= 1
            # Call this function again after 1 second
            self.window.after(1000, self.countdown)
        else:
            # Stop the quiz when time runs out
            self.feedback.config(text=f"Time's up! Final score: {self.score}")
            # Disable the answer entry and submit button
            self.answer.config(state=DISABLED)
            self.submit.config(state=DISABLED)
        # Play again
        

# Initialize the MultiplicationQuiz class
MultiplicationQuiz()
