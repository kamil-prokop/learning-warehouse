items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [],
    "unit": [],
    "unit_price PLN": []
}


def intro_question():
    #X_replay == str(init_answer)
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")
    
    for k, v in items.items():
        text = k
        print(text)

intro_question()