items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [],
    "unit": [],
    "unit_price PLN": []
}

text = ""
def intro_question():
    #X_replay == str(init_answer)
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")
    print("---", '\t', "----")

    items_list = []
    for i in items:
        items_list.append(i)

    def items_tabs(items_list):
        print(*items_list, sep = '\t')
    items_tabs(items_list)

intro_question()