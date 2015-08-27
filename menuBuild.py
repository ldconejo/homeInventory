__author__ = 'luisconejo'
# Simplifies the process of creating terminal menus

# Builds a menu from a dictionary object
# Ask the user for input and returns the user's selection
def buildMenu(menuTitle, menuOptions, menuQuestion = 'Enter your choice:'):
    print '***************************************************************'
    print '********* ' + menuTitle
    for key, value in menuOptions.iteritems():
        print '* ' + str(key) + ' -- ' + value
    print '***************************************************************'
    result = raw_input(menuQuestion)
    return result



