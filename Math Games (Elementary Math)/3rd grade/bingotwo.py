import random
import tkinter as tk

class MathGame:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")

        # create the labels for the equation and the score
        self.equation_label = tk.Label(master, font=('Arial', 24))
        self.equation_label.pack(pady=10)
        self.score_label = tk.Label(master, font=('Arial', 16))
        self.score_label.pack(pady=10)

        # create the entry box for the user to enter their answer
        self.answer_entry = tk.Entry(master, font=('Arial', 24))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind('<Return>', self.check_answer)


        # Create a correct if the user's answer is correct and an incorrect label if it is incorrect for 10 seconds
    


        # create the buttons for starting a new game and quitting
        self.new_game_button = tk.Button(master, text="New Game", font=('Arial', 16), command=self.new_game)
        self.new_game_button.pack(pady=10)
        self.quit_button = tk.Button(master, text="Quit", font=('Arial', 16), command=master.quit)
        self.quit_button.pack(pady=10)

        # set the initial score and start a new game
        self.score = 0
        self.new_game()

    def new_game(self):
        # generate a random equation and display it
        self.a = random.randint(1, 100)
        self.b = random.randint(1, 100)
        self.operation = random.choice(['+', '-'])
        if self.operation == '+':
            self.answer = self.a + self.b
        else:
            self.answer = self.a - self.b
        self.equation_label.config(text=f"{self.a} {self.operation} {self.b} =")

        # clear the answer entry box and update the score label
        self.answer_entry.delete(0, 'end')
        self.score_label.config(text=f"Score: {self.score}")

    def check_answer(self, event):
        # check if the user's answer is correct and update the score accordingly
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.score += 1
                # show the correct label for 10 seconds
              
                self.score_label.config(text=f"Score: {self.score}")
            self.new_game()
        except ValueError:
            pass

root = tk.Tk()
game = MathGame(root)
root.mainloop()
