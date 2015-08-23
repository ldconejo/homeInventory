__author__ = 'luisconejo'

import dbClass

if __name__ == '__main__':
    # Initialize database
    productDB = dbClass.dbClass('products')

    # Create products table
    tableColums = {'barcode':'INT PRIMARY KEY', 'Description':'TEXT'}

    productDB.createTable('PRODUCTS', tableColums)

    # Add entry to products table
    newProduct = (0001, 'TOILET_PAPER')
    productDB.addDBEntry('PRODUCTS', newProduct)

    # Search in the products table
    list = productDB.getTableRows('PRODUCTS')
    print list

    # Delete record
    productDB.deleteDBEntry('PRODUCTS','1','barcode')
