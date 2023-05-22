import tkinter as tk
from tkinter import messagebox
import random

class MoneyMathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Money Math Game")
        self.master.geometry("400x400")

        self.num_problems = 0
        self.num_correct = 0

        self.problem_label = tk.Label(self.master, text="", font=("Arial", 20))
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.master, font=("Arial", 16))
        self.answer_entry.pack(pady=20)

        self.check_button = tk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=20)

        self.new_problem_button = tk.Button(self.master, text="New Problem", command=self.new_problem)
        self.new_problem_button.pack(pady=20)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=20)

        self.new_problem()

    def new_problem(self):
        self.pennies = random.randint(0, 5)
        self.nickels = random.randint(0, 3)
        self.dimes = random.randint(0, 2)
        self.quarters = random.randint(0, 1)

        problem_str = f"How much money is {self.pennies} pennies, {self.nickels} nickels, {self.dimes} dimes, and {self.quarters} quarters?"
        self.problem_label.config(text=problem_str)

        self.total = self.pennies + self.nickels*5 + self.dimes*10 + self.quarters*25

    def check_answer(self):
        answer = self.answer_entry.get()
        if answer == str(self.total):
            tk.messagebox.showinfo("Congratulations!", "That's correct!")
            self.num_correct += 1
        else:
            tk.messagebox.showwarning("Uh oh!", f"That's incorrect. The correct answer is {self.total}.")

        self.num_problems += 1
        self.new_problem()

    def quit_game(self):
        if self.num_problems == 0:
            accuracy = 0
        else:
            accuracy = self.num_correct / self.num_problems
        accuracy_percent = accuracy * 100

        message_str = f"You answered {self.num_correct} out of {self.num_problems} problems correctly ({accuracy_percent:.0f}%)."
        tk.messagebox.showinfo("Game Over", message_str)

        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    MoneyMathGame(root)
    root.mainloop()
