items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [],
    "unit": [],
    "unit_price (PLN)": []
}

text = ""
def intro_question():
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")

    elif init_answer == "show":

        items_list = []
        for i in items:
            items_list.append(i)
    
        items_letters_length = []
        for j in items_list:
            items_letters_length.append("-" * len(j))

        def items_tabs(items_x):
            print(*items_x, sep = '\t')
        items_tabs(items_list)
        items_tabs(items_letters_length)


intro_question()