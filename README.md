# Self-Cashier Simulation
Self-Cashier is a simple Python program that simulates a self-cash system.
In this system, the user can do the following:
- Login into the system using Member ID
- Adding items to the cart
- Removing items from the cart
- Rename item in the cart
- Editing groceries including Qty and price of items
- View the contents of the cart
- Empty the contents of the basket
- Checkout groceries to process the payment
- Print Receipt right after checkout
After the user checkout their purchase, the system automatically logs out from the previous member. 
A login process using a member ID is required to perform another purchase.

# Task Description
- Transaction.py contains the functions used to process each available feature.
  In the transaction module there is a transaction constructor containing several main methods, namely add_item, remove_item, update_item_name, update_item_qty, update_item_price, print_receipt, and calculate_price. Details can be seen in the following code with some explanation in the lines that are needed.
- super_cashier.py is the main module to run to use this program. It contains the main-menu system and try-except for handling user input.

# How to Use
1. Download the Transaction.py and super_cashier.py modules
2. Save both in one local directory
3. Open the terminal and enter the directory where the module is stored
4. Run the super_cashier.py python module in the terminal
5. Operate according to the information that appears on the screen

# Test Case Results
1. Welcome Message (before Login)

![image](https://user-images.githubusercontent.com/96038150/205502460-277065c3-f22b-43fa-8792-d478a74e5eb3.png)

2. Adding Items to Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502635-ca6f0946-49b3-4e7a-a1d4-310fe8adcead.png)

3. Show Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502707-1a207511-1bf0-45b3-9522-a0988d5c1038.png)

4. Remove Item from Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502740-2f39e5b6-f32c-4f4c-b2fa-bf93946848bd.png)

5. Rename Item in Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502840-a85bb40b-f4b0-45dc-b3c5-7d9e6b318652.png)

6. Edit Qty Item in Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502864-8dcc0ee8-180b-41ac-a077-6ea6a66beb6d.png)

7. Edit Price Item in Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502901-bc03287c-f792-4732-b90e-9ee96107a982.png)

8. Clear Items in Cart
   
![image](https://user-images.githubusercontent.com/96038150/205502941-e807beb3-9e8b-4e3c-80f3-09fa218e7323.png)

9. Check-Out Items to Payment (Print Receipt)
   
![image](https://user-images.githubusercontent.com/96038150/205503090-01a629cf-8685-496f-9bdd-dcd7940b8b27.png)
