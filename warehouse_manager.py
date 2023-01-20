items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [120, 1000, 12000, 25],
    "unit": ["l", "kg", "kg", "kg"],
    "unit price (PLN)": [2.3, 3, 1.2, 40]
}

def intro_question():
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")

    elif init_answer == "show":

        items_keys = [i.title() for i in items]
        items_letters_length = ["-" * len(j) for j in items_keys]
        
        items_values = []
        for j in range(0,len(items.items())):
            for i in items:
                items_values.append(items.get(i)[j])

        items_final_list = []
        items_final_list.append(items_keys)
        items_final_list.append(items_letters_length)

        for i in range(0,4):
            items_final_list.append(items_values[4*i:4+4*i])

        def get_items():
            for row in items_final_list:
                print("{: <10} {: <15} {: <10} {: <20}".format(*row))
        get_items()

intro_question()