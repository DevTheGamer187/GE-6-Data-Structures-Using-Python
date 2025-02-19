class Restaurant:
    def __init__(self,add_item_to_menu,book_tables,customer_orders):
        self.menu_item = add_item_to_menu
        self.book_table = book_tables
        self.customer_orders = customer_orders

    def print(self):
        print(self.menu_item,self.book_table,self.customer_orders)

p1=Restaurant(["chilli paneer","kofta","paneer tikka","butter chicken","korma","chowmein","tea","coffee"],[1,2,3,4,5],[])

p2=Restaurant([],[],[])
print("Menu Items :- ",p1.menu_item)
print("Table Reservations:- ",p1.book_table)

while True:
    order=input("Give your order:- ")
    p2.customer_orders.append(order)
    print("Done ordering??")
    option=input("press n to end:- ")
    if option == "n":
        break

reservations=input("enter table number:- ")
p2.book_table.append(reservations)
print("Customer orders:- ",p2.customer_orders,"on table number:-",p2.book_table[0])
