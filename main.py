import tkinter as tk
from tkinter import ttk
import json
from random import randint, choice

start_text = "Französisch verben"
with open("verbs.json", "r") as f:
    verbs = json.load(f)
keys = list(verbs.keys())
answer = ""
verbrange = [17, -1]

def check_verb(_=""):
    if label.cget("text")!=start_text:
        if entry.get() == answer:
            answer_label.config(text=f"Right answer :)")
        else:
            answer_label.config(text=f"Wrong answer ({answer})")
        if entry.get() != "":
            entry.delete(0, tk.END)
        generate_verb()
    else:
        generate_verb()
def generate_verb(_=""):
    global answer
    verb_inf = choice(keys) #suis
    #print(f"VERB in INFINITIVE: {verb_inf}")
    verb_con = verbs[verb_inf]
    #print(f"ALL CONJUCATIONS of this verb: {verb_con}")
    # { "present" : {"suis", "es", ...},
    #   "passe compose" : {"été", "avoir", ...},
    #  ...}

    tense = randint(0, 7)
    tense = list(verb_con.keys())[tense] # present, passe compose, imparfait, ...
    #print(f"the TENSE: {tense}")
    person = randint(0, 5)

    if tense !="passe compose" and tense != "plus-que-parfait" and tense != "conditionnel passe" and tense != "imperatif":
        answer = verb_con[tense][person]
    elif tense == "imperatif":
        person = choice([1, 3, 4])
        answer = verb_con[tense][person]
    elif tense == "plus-que-parfait":
        answer = f"{verbs[verbs[verb_inf][tense][1]]['imparfait'][person]} {verbs[verb_inf][tense][0]}"
    elif tense == "conditionnel passe":
        answer = f"{verbs[verbs[verb_inf][tense][1]]['conditionnel present'][person]} {verbs[verb_inf][tense][0]}"
    elif tense == "passe compose":
        answer = f"{verbs[verbs[verb_inf][tense][1]]['present'][person]} {verbs[verb_inf][tense][0]}"
    #print(f"and the PERSON is: {person+1}\n\n")

    #Question on Screen
    person += 1
    if person <= 3:
        label.config(text=f"Was ist die {person}. Person singular von dem Verb {verb_inf} in der Zeitform {tense}?")
    else:
        label.config(text=f"Was ist die {person-3}. Person plural von dem Verb {verb_inf} in der Zeitform {tense}?")

root = tk.Tk()
root.title("Französisch Verben")
root.geometry("1100x600")

label = tk.Label(root, text=start_text, font=("Arial", 20))
label.pack(pady=20)


entry = ttk.Entry(root, width=20, font=("Arial", 18))
entry.bind("<Return>", check_verb)
entry.pack()


answer_label = tk.Label(root, font=("Arial", 20, "bold"))
answer_label.pack()

root.mainloop()
