import os
import sqlite3

class dbClass():

    # Constructor
    def __init__(self, dbFilename):
        self.dbFilename = dbFilename

        # Checks if the DB file already exists
        self.dbIsNew = not os.path.exists(self.dbFilename)

        # Create connection to database
        self.conn = sqlite3.connect(self.dbFilename)

        if self.dbIsNew:
            print "INFO: New database"
        else:
            print "INFO: Existing database"


    # Creates new db table
    # tableColumns is a dictionary object with the names of each table columns and details
    def createTable(self, tableName, tableColumns):
        # Assign internal cursor for table creation
        cur = self.conn.cursor()

        print tableColumns

        # Build SQL query to create table
        columnString = ''
        for column in tableColumns:
            columnString = columnString + column + ' ' + tableColumns[column] + ', '

        # Remove last trailing comma and space
        columnString = columnString[:-2]

        # Build query
        query = 'CREATE TABLE ' + tableName + '(' + columnString + ')'

        # Run query
        self.runDBQuery(query)

    # Adds an entry to table
    # columnValues is a list
    def addDBEntry(self, tableName, columnValues):

        # Build SQL query to add entry
        columnString = ''
        for column in columnValues:
            columnString = columnString + "'" + str(column) + "'" + ', '

        # Remove last trailing comma and space
        columnString = columnString[:-2]

        # Build query
        query = 'INSERT INTO ' + tableName + ' VALUES(' + columnString + ')'
        result = self.runDBQuery(query)

    # Deletes entry from table
    def deleteDBEntry(self,tableName,uniqueID, columnID):
        # Build SQL query to delete entry
        query = 'DELETE FROM ' + tableName + ' WHERE ' + columnID + '=' + "'" + uniqueID + "'"
        self.runDBQuery(query)

    # Searches DB for an entry
    def searchDB(self, tableName, searchValue, columnID):
        # Build SQL query to search for rows in table
        query = 'SELECT * FROM ' + tableName + ' WHERE ' + columnID + '=' + searchValue
        cur = self.runDBQuery(query)

        # Show results
        for row in cur.fetchall():
            print row

    # Get entire table
    def getTableRows(self, tableName):
        # Build SQL query
        query = 'SELECT * FROM ' + tableName
        cur = self.runDBQuery(query)
        resultList = []
        for row in cur.fetchall():
            resultList.append(row)
        return resultList

    # Runs a DB query
    def runDBQuery(self, query):
        cur = self.conn.cursor()
        print query
        # Try to create the table
        try:
            cur.execute(query)
            # Commit the result (for calls that add rows)
            self.conn.commit()

            # Return cursor for queries returning values
            return cur

        except sqlite3.OperationalError as errorMessage:
            print "ERROR:", errorMessage

        except sqlite3.IntegrityError as errorMessage:
            print "ERROR:", errorMessage





