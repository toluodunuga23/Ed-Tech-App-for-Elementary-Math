import random
import tkinter as tk

class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")
        self.master.geometry("300x300")
        
        self.dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        
        self.dice_label = tk.Label(self.master, font=("Arial", 100))
        self.dice_label.pack(pady=50)
        
        self.roll_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=20)
        
    def roll_dice(self):
        result = random.randint(1, 6)
        self.animate_dice(result)
        
    def animate_dice(self, result, i=0):
        if i == 10:
            self.dice_label.config(text=self.dice[result-1])
            return
        
        dice_face = random.choice(self.dice)
        self.dice_label.config(text=dice_face)
        
        self.master.after(100, self.animate_dice, result, i+1)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    DiceRoller(root)
    root.mainloop()
