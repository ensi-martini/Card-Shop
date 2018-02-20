import sqlite3
import easygui
import random

conn = sqlite3.connect('store.db')
cur = conn.cursor()

def initialize(cursor = cur, connection = conn):
    '''initialize(cursor, connection) --> None
    Resets Cards, Customers, and Transactions tables to original values'''
    
    #Emptying out the tables
    cur.execute('DELETE FROM Cards')
    cur.execute('DELETE FROM Customers')
    cur.execute('DELETE FROM Transactions')      
    
    cursor.execute('INSERT INTO Cards VALUES ("Blue-Eyes White Dragon",          5.99, "Ultra",   8, 89631139)')
    cursor.execute('INSERT INTO Cards VALUES ("Dark Magician",                   3.99, "Super",  15, 46986414)')
    cursor.execute('INSERT INTO Cards VALUES ("Kuriboh",                         0.99, "Common",  4, 40640057)')
    cursor.execute('INSERT INTO Cards VALUES ("Elemental Hero Neos",             2.99, "Rare",    6, 89943723)')
    cursor.execute('INSERT INTO Cards VALUES ("Cyber Dragon",                    7.99, "Ultra",   3, 70095154)')
    cursor.execute('INSERT INTO Cards VALUES ("Cyber Dragon",                    4.99, "Rare",   11, 70095153)')
    cursor.execute('INSERT INTO Cards VALUES ("Number 39: Utopia",              12.99, "Super",  22, 84013237)')
    cursor.execute('INSERT INTO Cards VALUES ("Mecha Phantom Beast Dracossack", 79.99, "Ultra",   1, 22110647)')
    cursor.execute('INSERT INTO Cards VALUES ("Obelisk the Tormentor",          13.99, "Common", 25, 62180201)')
    cursor.execute('INSERT INTO Cards VALUES ("Elemental Hero Flame Wingman",    2.99, "Rare",    8, 35809262)')
    cursor.execute('INSERT INTO Cards VALUES ("Evocator Chevalier",              1.99, "Common", 13, 96872283)')
    cursor.execute('INSERT INTO Cards VALUES ("Evocator Chevalier",              3.99, "Rare",    8, 96872282)')
    cursor.execute('INSERT INTO Cards VALUES ("Gearfried the Iron Knight",       7.99, "Ultra",   4, 11423705)')
    cursor.execute('INSERT INTO Cards VALUES ("Gearfried the Swordmaster",       8.99, "Ultra",   4, 57046845)')
    cursor.execute('INSERT INTO Cards VALUES ("Junk Synchron",                   1.99, "Rare",   11, 63977008)')
    cursor.execute('INSERT INTO Cards VALUES ("Panther Warrior",                 2.50, "Common", 12, 42035044)')
    cursor.execute('INSERT INTO Cards VALUES ("Dark Magician Girl",             17.99, "Super",   4, 38033121)')
    cursor.execute('INSERT INTO Cards VALUES ("Dark Magician Girl",             23.99, "Ultra",   1, 38033120)')
    cursor.execute('INSERT INTO Cards VALUES ("Metal Reflect Slime",             1.99, "Common", 16, 26905245)')
    cursor.execute('INSERT INTO Cards VALUES ("Goblin Attack Force",             3.99, "Rare",    8, 78658564)')
    cursor.execute('INSERT INTO Cards VALUES ("Giant Soldier of Steel",         35.99, "Super",   2, 57043117)')
    
    cursor.execute('INSERT INTO Customers VALUES ("Jen Grant",            13.56,  3, 46409334)')
    cursor.execute('INSERT INTO Customers VALUES ("Garth Oliver",         11.23,  2, 66343451)')
    cursor.execute('INSERT INTO Customers VALUES ("Harriette Anthonyson",  7.50,  1, 29779360)')
    cursor.execute('INSERT INTO Customers VALUES ("Katelynn Beckett",     12.11,  2, 86510104)')
    cursor.execute('INSERT INTO Customers VALUES ("Kaelea Hyland",         9.48,  1, 80779041)')
    cursor.execute('INSERT INTO Customers VALUES ("Kris Grenville",       25.46,  7, 47548596)')
    cursor.execute('INSERT INTO Customers VALUES ("Mariel Jakeman",       17.43,  6, 41692789)')
    cursor.execute('INSERT INTO Customers VALUES ("Steph Irving",        124.17, 14, 14598922)')
    cursor.execute('INSERT INTO Customers VALUES ("Orrell Daniell",       45.29, 10, 80895149)')
    cursor.execute('INSERT INTO Customers VALUES ("Vi Bateson",           22.67,  7, 95538857)')
    cursor.execute('INSERT INTO Customers VALUES ("Becca Abramson",        2.25,  1, 15469167)')
    cursor.execute('INSERT INTO Customers VALUES ("Myranda Selby",        14.68,  5, 96494271)')
    cursor.execute('INSERT INTO Customers VALUES ("Happy Milton",          7.89,  3, 76063214)')
    cursor.execute('INSERT INTO Customers VALUES ("Tansy Harmon",          0.00,  0, 43743790)')
    cursor.execute('INSERT INTO Customers VALUES ("Roseann Howse",        76.05, 11, 93330430)')
    cursor.execute('INSERT INTO Customers VALUES ("Darryl William",       19.84,  6, 68250415)')
    cursor.execute('INSERT INTO Customers VALUES ("Darryl William",       35.19,  8, 39291184)')
    cursor.execute('INSERT INTO Customers VALUES ("Gerrard Garfield",     36.25,  3, 32373005)')
    cursor.execute('INSERT INTO Customers VALUES ("Gerrard Garfield",     21.32,  9, 98397630)')
    cursor.execute('INSERT INTO Customers VALUES ("Kate Simpson",          0.00,  2, 36066059)')
    
    cursor.execute('INSERT INTO Transactions VALUES (89631139, 1, 46409334, 1997, 26713)')
    cursor.execute('INSERT INTO Transactions VALUES (46986414, 2, 46409334, 1997, 85778)')
    cursor.execute('INSERT INTO Transactions VALUES (40640057, 1, 46409334, 1998, 99201)')
    cursor.execute('INSERT INTO Transactions VALUES (89943723, 3, 66343451, 1999, 76128)')
    cursor.execute('INSERT INTO Transactions VALUES (70095153, 1, 66343451, 1999, 12598)')
    cursor.execute('INSERT INTO Transactions VALUES (70095154, 1, 29779360, 1999, 82458)')
    cursor.execute('INSERT INTO Transactions VALUES (84013237, 3, 86510104, 2000, 97302)')
    cursor.execute('INSERT INTO Transactions VALUES (62180201, 1, 86510104, 2000, 99727)')
    cursor.execute('INSERT INTO Transactions VALUES (35809262, 2, 80779041, 2001, 12435)')
    cursor.execute('INSERT INTO Transactions VALUES (96872283, 4, 47548596, 2002, 03073)')
    cursor.execute('INSERT INTO Transactions VALUES (96872282, 2, 41692789, 2003, 63622)')
    cursor.execute('INSERT INTO Transactions VALUES (22110647, 1, 14598922, 2004, 26835)')
    cursor.execute('INSERT INTO Transactions VALUES (11423705, 3, 80895149, 2005, 88352)')
    cursor.execute('INSERT INTO Transactions VALUES (57046845, 2, 95538857, 2006, 81139)')
    cursor.execute('INSERT INTO Transactions VALUES (63977008, 5, 15469167, 2007, 39235)')
    cursor.execute('INSERT INTO Transactions VALUES (42035044, 2, 96494271, 2008, 43200)')
    cursor.execute('INSERT INTO Transactions VALUES (38033121, 3, 76063214, 2009, 46117)')
    cursor.execute('INSERT INTO Transactions VALUES (38033120, 1, 93330430, 2010, 43844)')
    cursor.execute('INSERT INTO Transactions VALUES (26905245, 5, 68250415, 2011, 47227)')
    cursor.execute('INSERT INTO Transactions VALUES (57043117, 2, 39291184, 2012, 54239)')
    
    connection.commit()

def add_card(cursor = cur, connection = conn):
    '''add_card(cursor, connection) --> None
    Adds a card to the Cards table, and interacts with user through easygui'''
    
    response = easygui.multenterbox("Please enter the card's details:", "Ensi's Card Shop", ('Name', 'Price', 'Rarity', 'Quantity', 'Product ID'), ('', '', '', '', random.randint(10000000, 99999999)))        
    
    try:        
        #Not using .format, instead using built in SQL method to prevent security weakness
        cursor.execute('INSERT INTO Cards VALUES (?, ?, ?, ?, ?)', (response[0], float(response[1]), response[2], int(response[3]), int(response[4])))
        
        connection.commit()
        easygui.msgbox('Card added!', "Ensi's Card Shop")
        
    except Exception as error:
        easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
        
def add_customer(cursor = cur, connection = conn):
    '''add_customer(cursor, connection) --> None
    Adds a customer to the Customers table, and interacts with the user through easygui'''
    
    response = easygui.multenterbox("Please enter the customer's details: ", "Ensi's Card Shop", ('Name', 'Amount Spent', 'Visits', 'Customer ID'), ('', '0.00', '0', random.randint(10000000, 99999999)))
    
    try:
        
        cursor.execute('INSERT INTO Customers VALUES (?, ?, ?, ?)', (response[0], float(response[1]), int(response[2]), int(response[3])))
        
        connection.commit()
        easygui.msgbox('Customer added!', "Ensi's Card Shop")
        
    except Exception as error:
        
        easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
        
def add_transaction(cursor = cur, connection = conn):
    '''add_transaction(cursor, connection) --> None
    Adds a transaction to the Transaction table, then updates that customer's data in the Customers table, and interacts with the user through easygui'''
    
    #Getting the latest year
    cur.execute('SELECT MAX(Year) FROM Transactions')
    year = cur.fetchall() #Since it is a tuple inside a list, we still need to use indexing to get the value
    
    response = easygui.multenterbox('Please enter the transaction details: ', "Ensi's Card Shop", ('Product ID', 'Quantity', 'Customer ID', 'Year', 'Transaction ID'), ('', '', '', year[0][0], random.randint(10000, 99999)))
    
    try:
        
        cursor.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?, ?)', (int(response[0]), int(response[1]), int(response[2]), int(response[3]), int(response[4])))
        
        try:
            #Updating a customer's Amount_Purchased and Visits value, according to what they bought
            #NOTE: this query is more complicated than some of the queries below, maybe acknowedge it as such?
            cursor.execute('''UPDATE Customers SET Amount_Spent = 
                              (SELECT Amount_Spent FROM Customers WHERE Customer_ID = {}) + 
                              ((SELECT Price FROM Cards WHERE Cards.Product_ID = {}) * {})'''.format(response[2], response[0], response[1]))
            
            cursor.execute('''UPDATE Customers SET Visits = 
                              (SELECT Visits FROM Customers WHERE Customer_ID = {}) + 1'''.format(response[2]))
            
            connection.commit()
            easygui.msgbox('Customer {} data successfully updated!', "Ensi's Card Shop")
        
        except Exception as error:
            easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
            
        connection.commit()
        easygui.msgbox('Transaction added!', "Ensi's Card Shop")
        
    except Exception as error:        
        easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")

#Creating tables from scatch if they don't exist, reseting them if they already did
try:
    
    cur.execute('CREATE TABLE Cards (Name TEXT, Price REAL, Rarity TEXT, Quantity INTEGER, Product_ID INTEGER, PRIMARY KEY (Product_ID))')
    
except:
    
    cur.execute('DROP TABLE Cards')
    cur.execute('CREATE TABLE Cards (Name TEXT, Price REAL, Rarity TEXT, Quantity INTEGER, Product_ID INTEGER, PRIMARY KEY (Product_ID))')
    
try:
    
    cur.execute('CREATE TABLE Customers (Name TEXT, Amount_Spent REAL, Visits INTEGER, Customer_ID INTEGER, PRIMARY KEY (Customer_ID))')
    
except:
    
    cur.execute('DROP TABLE Customers')
    cur.execute('CREATE TABLE Customers (Name TEXT, Amount_Spent REAL, Visits INTEGER, Customer_ID INTEGER, PRIMARY KEY (Customer_ID))')
    
try:    
    cur.execute('CREATE TABLE Transactions (Product_ID INTEGER, Quantity INTEGER, Customer_ID INTEGER, Year INTEGER, Transaction_Number INTEGER, PRIMARY KEY (Transaction_Number))')
        
except:

    cur.execute('DROP TABLE Transactions')   
    cur.execute('CREATE TABLE Transactions (Product_ID INTEGER, Quantity INTEGER, Customer_ID INTEGER, Year INTEGER, Transaction_Number INTEGER, PRIMARY KEY (Transaction_Number))')
    
initialize()

choice = easygui.buttonbox("What would you like to do?", "Ensi's Card Shop", ('Reset Database', 'Initialize Data', 'Add Info', 'Built-In Queries', 'Custom Query', 'Quit'))

while choice != 'Quit':
    
    if choice == 'Reset Database':
        
        cur.execute('DELETE FROM Cards')
        cur.execute('DELETE FROM Customers')
        cur.execute('DELETE FROM Transactions')
        
    elif choice == 'Initialize Data':    
        initialize()
        
    elif choice == 'Add Info':
        
        add_choice = easygui.buttonbox('What would you like to do?', "Ensi's Card Shop", ('Add Product', 'Add Customer', 'Add Transaction'))
        
        if add_choice == 'Add Product':      
            add_card()
        
        elif add_choice == 'Add Customer':
            add_customer()
        
        elif add_choice == 'Add Transaction':
            add_transaction()
    
    elif choice == 'Custom Query':
        query = easygui.enterbox('Please enter your custom query:', "Ensi's Card Shop")
        
        try:
            cur.execute(query)
            
            if query.startswith('SELECT'):
                
                message = ''    
                
                for card in cur.fetchall():
                    message += str(card) + '\n' 
                    
                easygui.codebox('This is the database information you queried', "Ensi's Card Shop", message)
            
        except Exception as error:
            easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
        
    elif choice == 'Built-In Queries':
        
        query_choice = easygui.buttonbox('Please choose a query:', "Ensi's Card Shop", ("Customer's Purchases", 'Net Revenue', 'Add Column', 'Like Search', 'Popularity'))
        
        if query_choice == "Customer's Purchases":
            
            cur.execute('SELECT Name, Customer_ID FROM Customers')
            #NOTE: customer is a string, NOT a tuple
            customer = easygui.choicebox('Choose a customer to examine the purchases of', "Ensi's Card Shop", cur.fetchall())
            
            try:
                #Extracting all this customer's purchase history from transactions based on the common value Customer_ID
                cur.execute('''SELECT * FROM Transactions 
                               NATURAL JOIN Customers WHERE Transactions.Customer_ID = {} 
                               ORDER BY Customers.Name '''.format(customer[customer.find("',") + 3: customer.find(")")]))
                
                message = ''
                
                for transaction in cur.fetchall():
                    message += 'Customer purchased {} copies of a card with the product ID {}\n'.format(transaction[1], transaction[0])
                    
                easygui.codebox('This is the database information you queried', "Ensi's Card Shop", message)
                
            except Exception as error:
                easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
                
        elif query_choice == 'Net Revenue':
            
            period = easygui.multenterbox('Between which years do you wish to analyze? (inclusive)', "Ensi's Card Shop", ('Starting Year', 'Ending Year'))
            
            #Adding up all the product sold in the timeframe specified
            cur.execute('''SELECT SUM(Cards.Price) FROM Transactions
                           JOIN Cards WHERE Transactions.Product_ID = Cards.Product_ID AND Transactions.Year >= {} AND Transactions.Year <= {}
                           ORDER BY Transactions.Year'''.format(period[0], period[1]))
            
            revenue = cur.fetchall()  
            
            try:
                easygui.msgbox('Between {} and {}, the store has earned ${:.2f}, before expenses.'.format(period[0], period[1], revenue[0][0]), "Ensi's Card Shop")
            
            except Exception as error:
                easygui.msgbox('ERROR: {}'.format(error), "Ensi's Card Shop")
                
        elif query_choice == 'Add Column':
            
            easygui.msgbox('WARNING! Adding a column may render certain parts of the program unuseable. Proceed with caution', "Ensi's Card Shop", 'I will')    
           
            table = easygui.buttonbox('What would you like to add a column to?', "Ensi's Card Shop", ('Cards', 'Customers', 'Transactions'))
            column = easygui.enterbox('What is the column called?', "Ensi's Card Shop")
            column_type = easygui.buttonbox('What type of value is this column?', "Ensi's Card Shop", ('STRING', 'INTEGER', 'REAL'))
            
            cur.execute('ALTER TABLE {} ADD COLUMN {} {}'.format(table, column, column_type))
            cur.execute('SELECT Product_ID FROM {}'.format(table))
            
            data = cur.fetchall()
            
            for insert in data:
                
                replace = easygui.enterbox('UPDATE {} SET {} = '.format(table, column), "Ensi's Card Shop")
                
                if column_type == 'STRING':
                    cur.execute('UPDATE {} SET {} = "{}" WHERE Product_ID = {}'.format(table, column, replace, int(insert[0])))
                    
                else:
                    cur.execute('UPDATE {} SET {} = {} WHERE Product_ID = {}'.format(table, column, replace, int(insert[0])))

                
        elif query_choice == 'Like Search':
            
            table = easygui.buttonbox('Which table would you like to search within?', "Ensi's Card Shop", ('Cards', 'Customers', 'Transactions'))
            
            if table == 'Cards':
                value = easygui.buttonbox('What value are you searching for?', "Ensi's Card Shop", ('Name', 'Price', 'Rarity', 'Quantity', 'Product_ID'))
                
            elif table == 'Customers':
                value = easygui.buttonbox('What value are you searching for?', "Ensi's Card Shop", ('Name', 'Amount_Spent', 'Visits', 'Customer_ID'))
                
            else:
                value = easygui.buttonbox('What value are you searching for?', "Ensi's Card Shop", ('Product_ID', 'Quantity', 'Customer_ID', 'Year', 'Transaction_ID'))
            
            search_type = easygui.buttonbox('What do you remember about the term?', "Ensi's Card Shop", ('Starts with..', 'Ends with..', 'Includes..', 'Excludes..', 'Is X characters long..', 'Custom'))
            
            if search_type == 'Starts with..':                
                beginning = easygui.enterbox('What does the term start with?', "Ensi's Card Shop")
                cur.execute('SELECT * FROM {} WHERE {} LIKE "{}%"'.format(table, value, beginning))
                
            elif search_type == 'Ends with..':
                end = easygui.enterbox('What does the term end with?', "Ensi's Card Shop")
                cur.execute('SELECT * FROM {} WHERE {} LIKE "%{}"'.format(table, value, ending))
                
            elif search_type == 'Includes..':
                included = easygui.enterbox('What does the term include?', "Ensi's Card Shop")
                cur.execute('SELECT * FROM {} WHERE {} LIKE "%{}%"'.format(table, value, included))
                
            elif search_type == 'Excludes..':
                excluded = easygui.enterbox('What does the term exclude?', "Ensi's Card Shop")
                cur.execute('SELECT * FROM {} WHERE {} NOT LIKE "%{}%"'.format(table, value, excluded))
                
            elif search_type == 'Is X characters long..':
                length = int(easygui.enterbox('How long is the term?', "Ensi's Card Shop"))
                cur.execute('SELECT * FROM {} WHERE {} LIKE "{}"'.format(table, value, '_' * length))
                
            else:
                search = easygui.enterbox('What is your specification?', "Ensi's Card Shop")
                cur.execute('SELECT * FROM {} WHERE {} LIKE "{}"'.format(table, value, search))
                
            message = ''
            
            for result in cur.fetchall():
                message += str(result) + '\n'
                
            easygui.codebox('Here are the results of your like search', "Ensi's Card Shop", message)
            
        else:
            
            #Getting the amount of each card sold, ordering them from greatest to least
            cur.execute('''SELECT Name, Transactions.Product_ID, Transactions.Quantity FROM Transactions 
                           JOIN Cards WHERE Cards.Product_ID = Transactions.Product_ID
                           GROUP BY Transactions.Product_ID
                           ORDER BY Transactions.Quantity DESC''')
            
            message = ''
            
            for popularity in cur.fetchall():
                message += str(popularity) + '\n'
            
            easygui.codebox('Here is the popularity of all the cards', "Ensi's Card Shop", message)
               
    choice = easygui.buttonbox("What would you like to do?", "Ensi's Card Shop", ('Reset Database', 'Initialize Data', 'Add Info', 'Built-In Queries', 'Custom Query', 'Quit'))