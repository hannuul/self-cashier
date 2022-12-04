#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the modules needed for the following operations
import random
import os
import sys
import time
from IPython.display import clear_output
from transaction import *

# ---------------------------
# method to run the program #
# ---------------------------
def main():
    print("\t\t\tWELCOME TO WALLMART")
    login()

# --------------------------------------------------------------
# method to ask user to input member ID as a login requirement #
# --------------------------------------------------------------
def login():
    try:
        member_ID = input("Please enter your member ID : ")  # ask user to input member ID
        if member_ID.isdigit():                              # whether member ID is all-numeric
            if len(member_ID) == 6:                          # whether member ID contains 6 character
                pass
            else:
                raise ValueError
            pass
        else:
            raise TypeError
    except TypeError:
        print("Our Member ID consist of 6 numbers.")
        main()
    except EOFError:
        print("Please enter your member ID.")
        main()
    except ValueError:
        print("Our Member ID consist of 6 numbers.")
        main()
    else:
        random_ID = '0'                                      # random ID will always start with 0   
        nums = [1,2,3,4,5,6,7,8,9,0]
        for i in range(4):                                   # generate 4 following numbers
            random_ID += str(random.choice(nums))

        transaction_ID = str(member_ID)+"-"+str(random_ID)   # merge member ID and random number as Transaction ID
        transaction = Transaction(transaction_ID)            # create new transaction

        clear_output(wait=True)                              # clear console
        header(transaction)

# ---------------------------
# method to print main menu #
# ---------------------------
def header(transaction):
    print("==============================================")
    print("             WELCOME TO WALLMART")
    print("          One Stop Grocery Solution")
    print("==============================================")
    print(f"Your Transaction ID is          : {transaction.ID}")
    print("==============================================")
    print("A: Add Item\t\t   D: Edit Item Name")
    print("B: Show Cart\t\t   E: Edit Item Qty")
    print("C: Remove Item\t\t   F: Edit Item Price")
    print("----------------------------------------------")
    print("G: Check Out Cart\t   X: Clear Your Cart")
    print("----------------------------------------------")
    print("\t   Q: Cancel Transaction")
    print()
    choose_menu(transaction)

# -----------------------------------------------------------
# method to validate and process user's input for main menu #
# -----------------------------------------------------------
def choose_menu(transaction):
    print("==========Choose one menu to process==========")
    choice = input("You chose menu ")
    try:
        if not choice.isalpha():                              # wheter input is non-numeric
            raise TypeError
        elif len(choice) > 1:                                 # whether input is only one character
            raise ValueError
    except ValueError:
        print("Please choose among the menu.")
        choose_menu(transaction)
    except TypeError:
        print("Please choose among the menu.")
        choose_menu(transaction)
    except EOFError:
        print("Please choose one menu.")
        choose_menu(transaction)
    else:
        if choice.lower() == "a":
            choice_a(transaction)
        elif choice.lower() == "b":
            choice_b(transaction)
        elif choice.lower() == "c":
            choice_c(transaction)
        elif choice.lower() == "d":
            choice_d(transaction)
        elif choice.lower() == "e":
            choice_e(transaction)
        elif choice.lower() == "f":
            choice_f(transaction)
        elif choice.lower() == "g":
            choice_g(transaction)
        elif choice.lower() == "x":
            choice_x(transaction)
        elif choice.lower() == "q":
            choice_q(transaction)
        else:
            print("Please choose among the menu.")
            choose_menu(transaction)

# ---------------------------------------------
# method to process menu b (add item to cart) #
# ---------------------------------------------
def choice_a(transaction):
    name = input("Item Name\t: ")
    try:
        for i in range(len(transaction.item)):
            if transaction.item[i]["item"].lower() != name.lower():  # whether the same item already in cart
                continue
            else:
                raise ValueError
    except ValueError:                                               # tell user item already in cart
        print(f"--{name} already in your cart")
        print("You can edit or delete it through the other menus")
    else:
        while True:
            try:                                                     # whether input for qty is numeric
                qty = int(input("Item Qty\t: "))
            except ValueError:
                print("Qty must be a number")
            else:
                while True:
                    try:                                             # whether input for price is valid 
                        price = int(input("Item Price\t: "))
                        if price < 1000:
                            raise Exception
                    except ValueError:
                        print("Price must be a number w/o any separator")
                    except Exception:
                        print("Please enter a valid Item Price, in Rupiah")
                    else:
                        transaction.add_item(name, qty, price)        # add item to cart
                        break
                break
    finally:
        print()
        choose_menu(transaction)                                      # back to main menu
        
# --------------------------------------
# method to process menu b (show cart) #
# --------------------------------------
def choice_b(transaction):
    try:
        transaction.check_order()                                     # show shopping cart
    except IndexError:
        print("--Your Shopping Cart is EMPTY.")
        print("Add items to your cart through menu A")
    else:
        pass
    finally:
        print()
        choose_menu(transaction)
        
# --------------------------------------------------
# method to process menu c (remove item from cart) #
# --------------------------------------------------
def choice_c(transaction):
    if len(transaction.item) == 0:                                    # whether there is item in the cart
        print("Your Shopping Cart is EMPTY. No item to remove.")
        choose_menu(transaction)
    else:
        name = input("Item to Remove\t: ")                            # choose item to remove
    try:
        for i in range(len(transaction.item)):
            item = transaction.item[i]["item"]
            if item.lower() == name.lower():                          # if item found in cart
                break
            else:
                if i == len(transaction.item)-1:                      # if item does not found in cart
                    raise ValueError
    except ValueError:
        print(f"--{name} doesn't exist in your cart.")
    else:
        transaction.remove_item(item)                                 # remove item from cart
    finally:
        print()
        choose_menu(transaction)        

# --------------------------------------------
# method to process menu d (edit itame name) #
# --------------------------------------------
def choice_d(transaction):
    if len(transaction.item) == 0:
        print("Your Shopping Cart is EMPTY. No item to edit.")
        choose_menu(transaction)
    else:
        name = input("Item to Rename\t: ")                            # choose item to edit 
    try:
        for i in range(len(transaction.item)):
            item = transaction.item[i]["item"]
            if item.lower() == name.lower():
                break
            else:
                if i == len(transaction.item)-1:
                    raise ValueError
    except ValueError:
        print(f"--{name} doesn't exist in your cart.")
    else:
        updated_name = input(f"Rename {item} as: ")
        transaction.update_item_name(item, updated_name)              # update item in cart
    finally:
        print()
        choose_menu(transaction) 

# ------------------------------------------
# method to process menu e (edit item qty) #
# ------------------------------------------
def choice_e(transaction):
    if len(transaction.item) == 0:
        print("Your Shopping Cart is EMPTY. No item to edit.")
        choose_menu(transaction)
    else:
        name = input("Edit Qty of\t: ")
        
    try:
        for i in range(len(transaction.item)):
            item = transaction.item[i]["item"]
            if item.lower() == name.lower():
                break
            else:
                if i == len(transaction.item)-1:
                    raise ValueError
    except ValueError:
        print(f"--{name} doesn't exist in your cart.")
    else:
        while True:
            try:
                updated_qty = int(input(f"Qty of {item}\t: "))
            except ValueError:
                print("Qty must be a number")
            else:
                transaction.update_item_qty(item, updated_qty)
                break
    finally:
        print()
        choose_menu(transaction)

# --------------------------------------------
# method to process menu f (edit item price) #
# --------------------------------------------
def choice_f(transaction):
    if len(transaction.item) == 0:
        print("Your Shopping Cart is EMPTY. No item to edit.")
        choose_menu(transaction)
    else:
        name = input("Edit Price of\t: ")
        
    try:
        for i in range(len(transaction.item)):
            item = transaction.item[i]["item"]
            if item.lower() == name.lower():
                break
            else:
                if i == len(transaction.item)-1:
                    raise ValueError
    except ValueError:
        print(f"--{name} doesn't exist in your cart.")
    else:
        while True:
            try:
                updated_price = int(input(f"Price of {item}\t: "))
                if updated_price<1000:
                    raise Exception
            except ValueError:
                print("Price must be a number")
            except Exception:
                print("Please enter a valid item price, in Rupiah")
            else:
                transaction.update_item_price(item, updated_price)
                break
    finally:
        print()
        choose_menu(transaction)

# --------------------------------------------
# method to process menu g (payment process) #
# --------------------------------------------
def choice_g(transaction):
    try:
        transaction.print_receipt()
    except IndexError:
        print("Your Shopping Cart is EMPTY. No item to process.")
        print("Add items to your cart through menu A")
        print()
        choose_menu(transaction)
    except:
        print("Failed to process payment")
        print()
        choose_menu(transaction)
    else:
        print("\nTHE PAYMENT HAS BEEN BILLED TO YOUR CREDIT CARD")
        print("------THANK YOU FOR SHOPPING AT WALLMART------")
        choice_q(transaction)                                         # process to logout

# ------------------------------------------------------
# method to process menu x (remove all item from cart) #
# ------------------------------------------------------
def choice_x(transaction):
    try:
        if transaction.item == []:
            raise Exception
    except Exception:
        print("--Your Shopping Cart is still EMPTY.")
    else:
        transaction.reset_transaction()
    finally:
        print()
        choose_menu(transaction)
        
# -----------------------------------------------
# method to process menu v (cancel transaction) #
# -----------------------------------------------
def choice_q(transaction):
    try:
        transaction.reset_transaction()                                # reset shopping cart
    except:
        print("Log out request failed.")
        print()
        choose_menu(transaction)
    else:
        transaction.ID = ''                                            # reset transaction ID
        print("Logging Out from your account", sep=' ', end=' ', flush=True) 
        for countdown in range(3,0,-1):
            time.sleep(1.5)
            print(".", sep=' ', end=' ', flush=True)
        time.sleep(1.5)
        print("Logged Out", sep=' ', end=' ', flush=True)
        clear_output(wait=True)
        main()                                                         # re-run the program
        
#===========================================================================
# run the program #
main()


# In[ ]:




