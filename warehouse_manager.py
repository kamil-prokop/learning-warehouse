items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [],
    "unit": [],
    "unit_price": []
}


def intro_question():
    #X_replay == str(init_answer)
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")

intro_question()