class Restaurant:
    def __init__(self,add_item_to_menu,book_tables,customer_orders):
        self.menu_item = add_item_to_menu
        self.book_table = book_tables
        self.customer_orders = customer_orders

    def print(self):
        print(self.menu_item,self.book_table,self.customer_orders)

#p1=Restaurant("chilli paneer","table 2","kofta")
#p2=Restaurant("kofta","table 4","paneer tikka")
#p3=Restaurant("paneer tikka","table 10","butter chicken")
#p4=Restaurant("butter chicken","table 21","chowmein")
#p5=Restaurant("korma","table 5","tea")
#p6=Restaurant("chowmein","table 19","coffee")
#p7=Restaurant("tea","table 14","chilli paneer")
#p8=Restaurant("coffee","table 31","korma")
#
#p1.print()
#p2.print()
#p3.print()
#p4.print()
#p5.print()
#p6.print()
#p7.print()
#p8.print()

p0=Restaurant(
    ["chilli paneer","kofta","paneer tikka","butter chicken","korma","chowmein","tea","coffee"],
    [1,2,3,4,5],
    ["kofta","tea","korma","paneer tikka","chowmein"]
    )

#print(p1.menu_item)
#print(p1.book_table)
#print(p1.customer_orders)

#print("__MENU ITEMS__")
#
#for i in p1.menu_item:
#    print(i)
#
#print("__TABLE RESERVATIONS__")
#
#for i in p1.book_table:
#    print(i)
#
#print("__CUSTOMER ORDERS__")
#
#for i in p1.customer_orders:
#    print(i)

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



