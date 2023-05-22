import random
import tkinter as tk


class FunMoney:
    def __init__(self, master):
        self.master = master
        self.master.title("Fun Money")
        self.master.geometry("400x400")

        self.current_balance_label = tk.Label(self.master, text="Current Balance: $0.00", font=("Arial", 14))
        self.current_balance_label.pack(pady=20)

        self.money_label = tk.Label(self.master, text="", font=("Arial", 50))
        self.money_label.pack(pady=50)

        self.add_money_button = tk.Button(self.master, text="Add Money", command=self.add_money)
        self.add_money_button.pack(pady=20)

        self.subtract_money_button = tk.Button(self.master, text="Subtract Money", command=self.subtract_money)
        self.subtract_money_button.pack(pady=20)

        self.reset_button = tk.Button(self.master, text="Reset Balance", command=self.reset_balance)
        self.reset_button.pack(pady=20)

        self.current_balance = 0.0
        self.update_balance()

    def update_balance(self):
        self.current_balance_label.config(text=f"Current Balance: ${self.current_balance:.2f}")

    def add_money(self):
        amount = random.choice([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00])
        self.current_balance += amount
        self.update_balance()
        self.money_label.config(text=f"+${amount:.2f}", fg="green")
        self.master.after(500, self.reset_money_label)

    def subtract_money(self):
        amount = random.choice([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00])
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.update_balance()
            self.money_label.config(text=f"-${amount:.2f}", fg="red")
        else:
            self.money_label.config(text="Insufficient Funds", fg="red")
        self.master.after(500, self.reset_money_label)

    def reset_balance(self):
        self.current_balance = 0.0
        self.update_balance()

    def reset_money_label(self):
        self.money_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    FunMoney(root)
    root.mainloop()
