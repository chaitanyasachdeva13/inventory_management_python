import json
import os

class Product: #Product Class with the attributes id, name, price, quantity

    def __init__(self, product_id,product_name,product_price,product_quantity):  #Constructor for the Product Class Object
        self._product_id = product_id
        self._product_name = product_name
        self._product_price = product_price
        self._product_quantity = product_quantity

    def get_product_id(self): #Getter Function for retrieving product_id
        return self._product_id
    
    def get_product_name(self): #Getter Function for retrieving product_name
        return self._product_name
    
    def get_product_price(self): #Getter Function for retrieving product_price
        return self._product_price
    
    def get_product_quantity(self): #Getter Function for retrieving product_quantity
        return self._product_quantity
    
    def set_product_id(self,product_id): #Setter Function for retrieving product_id
        self._product_id = product_id

    def set_product_name(self,product_name): #Setter Function for retrieving product_name
        self._product_name = product_name

    def set_product_price(self,product_price): #Setter Function for retrieving product_price
        self._product_price = product_price

    def set_product_quantity(self,product_quantity): #Setter Function for retrieving product_quantity
        self._product_quantity = product_quantity

class Inventory:  #Inventory Class with all the Methods
    def __init__(self):
        self._inventory_data = {} #dictionary to save all the products in the key:value pair

    def add_product(self):  #Method to Add a Product
        print("\nOption1:...............ADD PRODUCT....................\n")
        while 1: #Input Validation for product_id, it has to be alphanumeric
            product_id = input("Enter the Product ID (Press . to return to the Main Menu): ")
            if product_id == ".":
                print("\nReturning to main menu.")
                input("Press any key to continue...")
                return
            # product_id = input("\nEnter The Product ID :")
            
            if not product_id.isalnum() :
                print("Only Alphabets and Numbers Allowed")
            else:
                if product_id in self._inventory_data:
                    print("Product with same Product ID already Exists")
                else:
                    break
        
        while 1: #Input Validation for product_name, it has to be alphabetical
            product_name = input("\nEnter The Product Name :")
            if not product_name.isalpha() :
                print("Only Alphabets Allowed")
            else:
                break

        while 1: #Input Validation for product_price, it has to be a positive non zero number
            product_price = input("\nEnter The Product Price :")
            
            try:
                price = float(product_price)
                if price <= 0:
                    print("Enter a Positive Non Zero Price")
                else:
                    break
            except ValueError:
                print("Please Enter a Correct Numerical Value")
        
        while 1: #Input Validation for product_quantity, it has to be positive non zero integer
            product_quantity = input("\nEnter The Product Quantity :")
            if not (product_quantity.isdigit()):
                print("Please enter a positive Integer value")
            else:
                if int(product_quantity) <=0:
                    print("Please enter a non zero Quantity")
                else:
                    break

        new_product=Product(product_id, product_name,float(product_price),int(product_quantity)) #Creating a new object of type product and initialising it by the user entered details
        self._inventory_data[new_product.get_product_id()] = new_product #adding the new object to the _inventory_data
        print("\nPlease confirm the following new product details")
        print("\nProduct ID : " , (product_id))
        print("Product Name : " , (product_name))
        print("Product Price : " , (product_price))
        print("Product Quantity : " , (product_quantity))
        while 1: #Loop to confirm the addition of account
            x=input("\nConfirm (Y/n) (Y for confirmation and n to Re-enter the value again) :").lower()
            if x=='y':
                new_product=Product(product_id, product_name,float(product_price),int(product_quantity))
                self._inventory_data[new_product.get_product_id()] = new_product
                break
            elif x=='n':
                self.add_product()
                break
            else:
                print("Please Re-enter your Choice")

        print("\nProduct Added")
        input("\nPress any key to return to the main screen : ")

    def view_product(self): #Method to View a Specific Product Details
        
        print("\nOption4:...............VIEW PRODUCT....................\n")
        prod_id = input("\nEnter the Product ID (Press . to return to the Main Menu): ")
        if prod_id == ".":
            print("\nReturning to main menu.")
            input("Press any key to continue...")
            return
        prod=self._inventory_data.get(prod_id) #check if the product_id exists in the _inventory_data dictionary
        if prod:
            print("\nProduct Details : ")
            print("\nProduct ID : " , (prod.get_product_id()))
            print("Product Name : " , (prod.get_product_name()))
            print("Product Price : " , (prod.get_product_price()))
            print("Product Quantity : " , (prod.get_product_quantity()))
            input("\nPress any key to return to the main screen: ")
        else:
            print("Invalid Product ID")
            self.view_product()
    
    def display_all_products(self): #Method to List all Products in the inventory
        print("\nOption5:...............LIST ALL PRODUCTS....................\n")
        
        print("\nReport for all Products in the Inventory with Details ")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Product ID     |      Product Name      |    Product Price    |    Product Quantity    |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for prod in self._inventory_data.values():
            print("{:<15}\t\t{:<15}\t\t{:<15}\t\t{:<15}".format(
                prod.get_product_id(),
                prod.get_product_name(),
                str(prod.get_product_price()),
                str(prod.get_product_quantity())
            ))
        
        input("\nPress any key to return to the main screen: ")

    def delete_product(self): #Method to delete product from the inventory
        print("\nOption3:...............DELETE PRODUCT....................\n")
        
        prod_id = input("Enter the Product ID (Press . to return to the Main Menu): ")
        if prod_id == ".":
            print("\nReturning to main menu.")
            input("Press any key to continue...")
            return
        prod = self._inventory_data.get(prod_id) #Find the product using the product_id
        
        if prod_id in self._inventory_data:
            print("\nPlease confirm the following product to be deleted : ")
            print("\nProduct ID : " , (prod.get_product_id()))
            print("Product Name : " , (prod.get_product_name()))
            print("Product Price : " , (prod.get_product_price()))
            print("Product Quantity : " , (prod.get_product_quantity()))

            while 1:
                x=input("Confirm (Y/n) (Y for confirmation and n to Re-enter the product ID again):").lower()
                if x=='y':
                    del self._inventory_data[prod_id] #delete the product if the user enters Y (yes)
                    break
                elif x=='n':
                    self.delete_product() #Call the delete function again if the user press no
                    return
                else:
                    print("Please Re-enter the Choice :")
            # del self._inventory_data[prod_id]
        else:
            print("Invalid Product ID") 
        print("\nProduct Deleted")
        input("\nPress any key to return to the main screen: ")


    def modify_product(self): #Method to update product_price and product_quantity
        print("\nOption2:...............UPDATE PRODUCT....................\n")
        
        prod_id = input("Enter the Product ID (Press . to return to the Main Menu): ")
        if prod_id == ".":
            print("\nReturning to main menu.")
            input("Press any key to continue...")
            return
        prod = self._inventory_data.get(prod_id) #Find the product using the product_id
        if prod:
            print("Press Enter to Retain the Current value")
            while 1: #Loop to take the value of new price with the proper validation
                product_price=input(f"\nEnter the New Price [Current Value: {prod.get_product_price()} ] : ")
                
                try:
                    price = float(product_price)
                    if price <= 0:
                        print("Enter a Positive Non Zero Price")
                    else:
                        break
                except ValueError:
                    print("Please Enter a Correct Numerical Value")
        
            while 1: #Loop to take the value of new quantity with the proper validation
                product_quantity=input(f"\nEnter the New Quantity [Current Value: : {prod.get_product_quantity()} ] : ")
                if not (product_quantity.isdigit()):
                    print("Please enter a positive Integer value")
                else:
                    if int(product_quantity) <=0:
                        print("Please enter a non zero Quantity")
                    else:
                        break
            
            print("\nPlease confirm")
            print("Product ID : " , (prod.get_product_id()))
            print("Product Name : " , (prod.get_product_name()))
            print("Product Price : " , (product_price))
            print("Product Quantity : " , (product_quantity))

            while 1: #Confirmation Loop
                x=input("Confirm (Y/n) :").lower()
                if x=='y':
                    if product_price:
                        prod.set_product_price(float(product_price)) #Set the price of the respective Product Object's Price attribute to the new value if the user says Y(yes)
                    if product_quantity:
                        prod.set_product_quantity(int(product_quantity)) #Set the price of the respective Product Object's Quantity attribute to the new value if the user says Y(yes)
                    break
                elif x=='n':
                    self.modify_product()
                    return
                else:
                    print("please reenter the choice")

        else:
            print("Invalid Product ID")

        input("\n Press any key to return to the main screen")  

    
    def display_total_inventory(self): #Method for Generating Reports that shows the full inventory value
        print("\nOption7:...............TOTAL INVENTORY REPORT....................\n")
        
        total_inventory_value = sum((prod.get_product_price()*prod.get_product_quantity()) for prod in self._inventory_data.values()) #Calculate the total inventory value using all the products in the inventory
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Total Inventory Value : ", total_inventory_value)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("\nPress Enter to return to the main screen: ")

    def display_low_stock(self): #Method to Display Low Stock Alerts
        print("\nOption6:...............LOW STOCK ALERT REPORT....................\n")
        print("Following are the products with low stock in inventory (less than 5)")
        print("\n")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Product ID     |      Product Name      |    Product Price    |    Product Quantity    |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for prod in self._inventory_data.values():
            if prod.get_product_quantity() < 5: #Assumed threshold for low stock alerts is quantity less than 5
                # print(f"{prod.get_product_id():<20} {prod.get_product_name():<20} {prod.get_product_price():<20} {prod.get_product_quantity():<20}")
                print("{:<15}\t\t{:<15}\t\t{:<15}\t\t{:<15}".format(
                    prod.get_product_id(),
                    prod.get_product_name(),
                    str(prod.get_product_price()),
                    str(prod.get_product_quantity())
                ))

        input("\nPress Enter to return to the main screen: ")

    
    def load_json(self,file_path): #Method to Load data from JSON file
        try:
        
            file = open(file_path,"r") #Open the JSON file in the reading mode
            inventory_data = json.load(file) #load the contents of the json file in the inventory_data variable
            for product_data in inventory_data: #loop to save the JSON data in the form of Product Class Object
                prod = Product(
                    product_data["product_id"],
                    product_data["product_name"],
                    product_data["product_price"],
                    product_data["product_quantity"]
                )
                self._inventory_data[prod.get_product_id()] = prod #Add the object to the _inventory_data dictionary
            file.close()
        except FileNotFoundError:
            print("JSON file not found, starting with an empty account list.")
        

    def save_json(self, file_path): #Method to Save data in the JSON file
        inventory_data = [
            {
                "product_id": acc.get_product_id(),
                "product_name": acc.get_product_name(),
                "product_price": acc.get_product_price(),
                "product_quantity": acc.get_product_quantity()
            }
            for acc in self._inventory_data.values() #parsing through the products in the _inventory_data dictionary
        ]
        file = open(file_path, "w") #Open the file in the writing mode
        json.dump(inventory_data, file) #dump all the inventory_data in the json file
        file.close()
        


def menu():

    inventory = Inventory() #Initialise an Object of Inventory Class
    inventory.load_json("products.json") #Load the contents of the file 
    while True: #while loop for menu system
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("              ########################################  ")
        print("              #   WELCOME TO INVENTORY MANAGEMENT    #   ")
        print("	      #                SYSTEM                #    ")
        print("              ########################################   ")
        print("1. ADD PRODUCT")
        print("2. UPDATE PRODUCT")
        print("3. DELETE PRODUCT")
        print("4. VIEW PRODUCT")
        print("5. DISPLAY ALL PRODUCTS")
        print("6. DISPLAY LOW STOCK ALERTS")
        print("7. DISPLAY TOTAL INVENTORY VALUE ")
        print("8. EXIT ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("CHOOSE AN OPTION")
        x = input("ENTER YOUR CHOICE: ")

        if x == '1':
            inventory.add_product()
        elif x == '2' :
            inventory.modify_product()
        elif x == '3':
            inventory.delete_product()
        elif x == '4':
            inventory.view_product()
        elif x == '5':
            inventory.display_all_products()
        elif x == '6':
            inventory.display_low_stock()
        elif x == '7':
            inventory.display_total_inventory()
        elif x == '8':
            print("\n\n\tThank you for using inventory management system")
            print("\n\tHope you had a great time using our inventory management tool")
            print("\n\tWe wish to have you here again")
            inventory.save_json("products.json") #save the data in JSON file on program exit
            break
        else:
            print("\nWrong choice entered")
            input("\nPress any Key to go back to Main Menu : ")

if __name__ == "__main__":
    menu()
