from random import choice

questions = ["Why is the sky blue?: ", "where do babbys come from?: ",
             "Why are there no dinosaurs?: ", "Why is there a face on the moon?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("oh... Okay.")

             
