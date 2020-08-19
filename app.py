import datetime

class Transaction:
    consumerID = ''
    producerID  = ''
    quantity = ''
    date = datetime.datetime.now()

    #Constructor
    def __init__(self, cID, pID, qty, tdate):
        self.consumerID = cID
        self.producerID = pID
        self.quantity = qty
        self.date = tdate

class Account:
    id = '' #this should match with the party named at the transaction
    balance = 0.0
    
    #Constructor
    def __init__(self, id):
        self.id = id

    def get_balance(self):
        return self.balance

    #Check type of party and update account balance
    def update_balance(self, consumerID, producerID, quantity):
        if(self.id == consumerID):
            self.balance -= quantity
        elif(self.id == producerID):
            self.balance += quantity
        else:
            pass




#Generate Ledger of Transactions
#From an external source file (CSV in comma separated)
fname = input('Enter file name (press enter if not name provided): ')
if len(fname) < 1 : fname = 'ledgerData.csv'

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


#Data structures
parties = set() #to store the parties ids

transactions = [] #represents the Ledger of transactions

listOfTransactions = [] #list of dictionaries to store the parties information.


#Loop each line of the file that represents a transactions.
for line in fh: 
    tr = line.split(',')
    date = tr[0]	
    consumer = tr[1]
    producer = tr[2]
    quantity = float(tr[3])

    #add parties
    parties.add(consumer)
    parties.add(producer)

    #instantiate transaction object
    transaction = Transaction(consumer, producer, quantity, date)

    #Fill transactions list
    transactions.append(transaction)

#Loop into the ledger of transactions
for pId in parties:
    #Initialize account objects for each named party of a the ledger
    account = Account(pId)


    for tr in transactions:
        myDict = dict() # dictionary to store the information of each party 

        #Calculate balance for each transaction
        account.update_balance(tr.consumerID, tr.producerID, tr.quantity)

        #Add to the dictionary of parties
        myDict.update([ ('id', pId) , ('date', tr.date) , ('balance', str(account.get_balance())) ] )      
        listOfTransactions.append(myDict)


#Find out what each party's balance is at a specified date
inputDate = input('Enter Date: ')

# Filter dictionary by keeping elements whose values are equals to the input date
for e in listOfTransactions: 
   if(inputDate == e['date'] ):
    print(e)
