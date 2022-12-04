# import the modules and/or libraries that will be needed
import tabulate
from collections import Counter
from IPython.display import clear_output

class Transaction():
    # Constructor
    def __init__(self, ID):
        self.ID = ID              # ID Transaction
        self.item = []            # declare empty list of shopping item (Shopping Cart)
        self.qty = 0              # declare number of shopping item as 0
        self.num = 0              # declare item's order number in receipt, starts with 1
        self.price_total = 0      # declare grand total as 0
        
    # method for adding item to cart
    # data of item consists of number, item name, qty, 
    # price per item, and total price
    def add_item(self, name, qty, price):
        self.num += 1
        self.total =+ qty*price                                    
        self.item.append({'no':self.num, 'item':name, 'qty':qty,
                          '@price':price, 'total':self.total})
        print(f"{name} has been added to cart.")     # show confirmation message   
        
    # method for removing item from cart
    def remove_item(self, remove):
        point = None              # variable to store index of the removed item
        for i in range(len(self.item)):
            if point is None:
                # delete item which item name matched the user input
                if self.item[i]['item'] == remove:
                    point = i
                    del self.item[i]
                    self.num -= 1
                    print(f"{remove} has been removed from cart.")   # show confirmation message
                #pass  
            else:
                # update order number of items after the removed item
                if i>point:
                    self.item[i-1]['no'] -= 1
                pass
        return self.item
    
    # method for editting item name
    def update_item_name(self, prev_name, updated_name):
        for i in range(len(self.item)):
            if self.item[i]['item'].lower() == prev_name.lower():
                self.item[i]['item'] = updated_name
                print(f"{prev_name} has been updated as {updated_name}")
                break 
        return self.item
    
    # method to editting item qty and total price
    def update_item_qty(self, name, updated_qty):
        for i in range(len(self.item)):
            if self.item[i]['item'].lower() == name.lower():
                self.item[i]['qty'] = int(updated_qty)
                self.item[i]['total'] = self.item[i]['qty']*self.item[i]['@price']
                print(f"qty of {name} has been updated to {updated_qty}")
                break
        return self.item
    
    # method to editting item price and total price
    def update_item_price(self, name, updated_price):
        for i in range(len(self.item)):
            if self.item[i]['item'].lower() == name.lower():
                self.item[i]['@price'] = int(updated_price)
                self.item[i]['total'] = self.item[i]['qty']*self.item[i]['@price']
                print(f"price of {name} has been updated to {updated_price}")
                break
        return self.item
    
    # method for counting qty of shopping item
    def count_item(self):
        qty_total = sum(x['qty'] for x in self.item)
        return qty_total
    
    # method for calculating total list price
    def sum_price(self):
        self.price_total = sum(x['total'] for x in self.item)
        return self.price_total
    
    # method for printing the Most Updated Shopping Cart
    # The shopping cart will be printed with a format
    def check_order(self):        
        header = self.item[0].keys()                    # set keys of dictionary as header
        rows =  [x.values() for x in self.item]         # loop values of dictionary per rows         
        print("\n            * Your Shopping Cart *")         
        print("+-------------------------------------------+")
        print(tabulate.tabulate(rows, header, intfmt=",", colalign=("center","center","center","center","right")))
        print("+-------------------------------------------+")
        print(f"  Qty : {self.count_item()}           Grand Total : Rp{self.sum_price():,}")
        
    # method for final-checking the shopping cart and
    # printing the the amount that needs to be paid.
    # This method specifically will print the pre-payment receipt
    def print_receipt(self):
        # clear console to print receipt
        for i in range(10):
            clear_output(wait=True)    
        # print receipt
        print("==============================================")
        print("                   WALLMART")
        print("          One Stop Grocery Solution")
        print("==============================================")
        print(f"Receipt for Transaction ID : {self.ID}")
        header = self.item[0].keys()                    # define header of table
        rows =  [x.values() for x in self.item]         # define rows of table
        print("\nPurchased Item:")
        print(tabulate.tabulate(rows, header, tablefmt="outline", intfmt=",",
                                colalign=("center","center","center","center","right")))
        qty_total = sum(x['qty'] for x in self.item)
        self.price_total = sum(x['total'] for x in self.item)
        print(f"Qty : {qty_total} items         Grand Total : Rp{self.price_total:,}\n") 
        self.calculate_price()
        
    # method for calculating discount and discounted price
    # under the condition:
    #   5% for a total spend of more than 200,000
    #   8% for a total spend of more than 300,000
    #   10% for a total spend of more than 500,000
    def calculate_price(self):
        print("==============================================")
        print(f"                     Total Price   : Rp{self.price_total:,}")
        if self.price_total > 500_000:
            print(f"                     Discount(10%) :-Rp {int(self.price_total*0.1):,}")
            print(f"                  Discounted Price : Rp{int(self.price_total*0.9):,}")
        elif self.price_total > 300_000:
            print(f"                     Discount(8%)  :-Rp {int(self.price_total*0.08):,}")
            print(f"                  Discounted Price : Rp{int(self.price_total*0.92):,}")
        elif self.price_total > 200_000:
            print(f"                     Discount(5%)  :-Rp {int(self.price_total*0.05):,}")
            print(f"                  Discounted Price : Rp{int(self.price_total*0.95):,}")
        else:
            pass
    
    # method to clear shopping cart
    def reset_transaction(self):
        self.item.clear()
        return self.item

