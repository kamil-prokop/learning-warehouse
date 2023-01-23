items = {
    "name": ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity": [120, 1000, 12000, 25],
    "unit": ["l", "kg", "kg", "kg"],
    "unit price (PLN)": [2.3, 3, 1.2, 40]
}
#wypisanie wszystkich kluczy ze słownika - zapisane do listy
items_keys = [i.title() for i in items]

#kreska podziału - zapisane do listy
items_letters_length = ["-" * len(j) for j in items_keys]

#spisanie wszystkich wartości ze słownika - zapisane do listy 
items_values = []
for j in range(0,len(items.items())):
    for i in items:
        items_values.append(items.get(i)[j])

#połączenie list
items_final_list = []
items_final_list.append(items_keys)
items_final_list.append(items_letters_length)

#podzielenie zbiorczej listy z wartości na mniejsze listy
for i in range(0, len(items.items())):
    items_final_list.append(items_values[4*i:4+4*i])


def intro_question():
    init_answer = input("What would you like to do? ")
    if init_answer == "exit":
        print("Exiting... Bye!")

    elif init_answer == "show":

        def get_items():
            for row in items_final_list:
                print("{: <10} {: <15} {: <10} {: <20}".format(*row))
        get_items()

    elif init_answer == "add":
        print("Adding to warehouse...")
        
        item_name = input("Item name: ")
        item_quantity = input("Item quantity: ")
        item_unit = input("Item unit of measure (eg.: l, kg, pcs): ")
        item_price = input("Item price in PLN: ")
        item_list = []
        item_list.append(item_name)
        item_list.append(item_quantity)
        item_list.append(item_unit)
        item_list.append(item_price)
                
        def add_item(name, quantity, unit_name, unit_price):
            items_final_list.append(item_list)
            for row in items_final_list:
                print("{: <10} {: <15} {: <10} {: <20}".format(*row))
        add_item(item_name, item_quantity, item_unit, item_price)
        
        print("Successfully added to warehouse. Current status:")

    elif init_answer == "sell":
        item_to_be_sold = input("Item name: ")
        quantity_to_be_sold = input("Quantity to sell: ")
        
        def sell_item(name_to_sold, quantity_to_sold):
            for i in items_final_list:
                if i[0] == str(item_to_be_sold):
                    i[0] = i[0]
                    i[1] = i[1] - int(quantity_to_be_sold)
                elif i[0] != item_to_be_sold:
                    i[0] = i[0]           
            
            print("Successfully sold ", quantity_to_be_sold, "unit of ", item_to_be_sold)
            
            for row in items_final_list:
                print("{: <10} {: <15} {: <10} {: <20}".format(*row))
            
        sell_item(item_to_be_sold, quantity_to_be_sold)

intro_question()