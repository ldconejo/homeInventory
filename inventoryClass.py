import dbClass

# Some code sources
# sqlite3
# http://pymotw.com/2/sqlite3/

class inventoryClass():
    # Class constructor
    def __init__(self, inventoryName):

        # Create database object for home inventory
        self.inventoryDB = dbClass.dbClass(inventoryName)

        # Create table for inventory items
        tableColumns = {'barcode':'INT', 'Description':'TEXT', 'Entry_Date':'TEXT', 'Expiration_Date':'TEXT'}
        self.inventoryDB.createTable('INVENTORY', tableColumns)


    # Adds new product type to database.
    # Note that this one does not refer to actual inventory, but to an abstract description of a product that may or may
    # not currently be in inventory
    def __addNewProduct__(self):
        pass

    # Adds inventory item.
    # An inventory item is a physical quantity of a product entering the household
    def addToInventory(self, barcode, description, entryDate, expDate):
        valueList = (barcode, description, entryDate, expDate)
        self.inventoryDB.addDBEntry('INVENTORY', valueList)

    # Removes inventory item
    # Removes an inventory item that
    def removeFromInventory(self, barcode):
        self.inventoryDB.deleteDBEntry('INVENTORY',barcode,'Expiration_Date')

    # Searches for products in the product table

    # Searches for items in inventory matching certain conditions
    def searchInventory(self,barcode):
        self.inventoryDB.searchDB('INVENTORY',barcode,'barcode')

    # Gets all items from the DB
    def listAll(self):
        result = self.inventoryDB.getTableRows('INVENTORY')
        return result