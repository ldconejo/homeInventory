__author__ = 'luisconejo'

import inventoryClass
import menuBuild
import sys
import time

if __name__ == '__main__':
    # Initialize database
    inventory = inventoryClass.inventoryClass('inventory')

    while True:
        # Build main menu
        mainMenuOptions = { 1: 'Add new product to inventory',
                            2: 'Delete product from inventory',
                            3: 'List all items',
                            4: 'Quit'}

        choice = menuBuild.buildMenu('MAIN MENU', mainMenuOptions)

        if choice == '4':
            print 'INFO: Have a nice day!'
            sys.exit()

        elif choice == '1':
            # Add new product
            barcode = raw_input('Enter product barcode: ')
            description = raw_input('Enter product description: ')
            currDate = time.strftime("%m/%d/%Y")
            expDate = raw_input('Enter expiration date: ')
            inventory.addToInventory(barcode,description,currDate,expDate)
        elif choice == '2':
            # Delete existing product
            barcode = raw_input('Enter product barcode: ')
            inventory.removeFromInventory(barcode)
        elif choice == '3':
            # List all items
            itemList = inventory.listAll()
            try:
                for item in itemList:
                    print item
            except:
                print "ERROR: No items found"

