from tkinter import *
from random import randint

root = Tk()
root.title("Flashcards")
root.geometry("500x500")

words=[
    (("Holla"),("Hello")),
    (("Adios"),("Goodbye")),
    (("Buenos Dias"),("Good Morning")),
    (("Buenas Tardes"),("Good Afternoon")),
    (("Buenas Noches"),("Good Night")),
    (("Como Estas"),("How are you")),
    (("Estoy Bien"),("I am fine")),
    (("Estoy Mal"),("I am not fine")),
    (("Hasta Luego"),("See you later")),
    (("Hasta Manana"),("See you tomorrow")),
    (("Hasta Pronto"),("See you soon")),
    (("Hasta La Vista"),("See you later")),
    (("Hasta Nunca"),("See you never")),
    (("Hasta Ahora"),("See you now")),
    (("Hasta Entonces"),("See you then")),
    (("Hasta Siempre"),("See you always")),

]
count=len(words)

def next():
    # clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)



    #Create random selection
    global random_word
    random_word=randint(0, count-1)
    #Update Spanish Word
    spanish_word.config(text=words[random_word][0])

def answer():
    if my_entry.get().capitalize()==words[random_word][1]:
       answer_label.config(text=f"Correct!!{words[random_word][0]} is {words[random_word][1]}")
 
 


    
    else:
       answer_label.config(text=f"Incorrect!!{words[random_word][0]} is not {my_entry.get().capitalize()}")




spanish_word= Label(root, text="", font=("Helvetica", 48))
spanish_word.pack(pady=50)

answer_label= Label(root, text="")
answer_label.pack(pady=20)



#Create entry box
my_entry= Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)






#Create buttons
button_frame= Frame(root)
button_frame.pack(pady=20)


answer_button = Button(button_frame, text="Answer",command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next Word", command=next )
next_button.grid(row=0, column=1, padx=20)





hint_button= Button(button_frame, text="hint")
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label= Label(root, text="")
hint_label.pack(pady=20)


# Run next function when program starts
next()










root.mainloop()
