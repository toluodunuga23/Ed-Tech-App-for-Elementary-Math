import random
import tkinter as tk


class ClockGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Clock Game")
        self.master.geometry("400x400")

        self.current_time = tk.Label(self.master, font=("Arial", 50))
        self.current_time.pack(pady=20)

        self.dice_label = tk.Label(self.master, font=("Arial", 100))
        self.dice_label.pack(pady=50)

        self.roll_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

        self.game_started = False
        self.current_time_value = 0
        self.correct_count = 0
        self.total_count = 0

    def start_game(self):
        self.current_time_value = random.randint(1, 12)
        self.update_time()
        self.game_started = True
        self.correct_count = 0
        self.total_count = 0

    def update_time(self):
        if self.game_started:
            self.current_time_value = (self.current_time_value + 1) % 12
            if self.current_time_value == 0:
                self.current_time_value = 12
        self.current_time.config(text=str(self.current_time_value))
        self.master.after(1000, self.update_time)

    def roll_dice(self):
        if self.game_started:
            result = random.randint(1, 6)
            self.dice_label.config(text=str(result))
            self.total_count += 1
            if result == self.current_time_value:
                self.correct_count += 1
                self.current_time.config(fg="green")
            else:
                self.current_time.config(fg="red")
            self.master.after(500, self.reset_dice)

    def reset_dice(self):
        self.dice_label.config(text="")
        self.current_time.config(fg="black")
        if self.total_count >= 10:
            self.game_started = False
            self.show_results()

    def show_results(self):
        self.roll_button.config(state="disabled")
        self.current_time.config(text=f"Score: {self.correct_count}/{self.total_count}")

if __name__ == "__main__":
    root = tk.Tk()
    ClockGame(root)
    root.mainloop()
