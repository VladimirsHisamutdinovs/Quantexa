from collections import defaultdict
from dataclasses import dataclass
from itertools import chain, groupby
import csv
from statistics import mean

@dataclass
class Transaction:
    """
    This class represents the structure of data
    in transactions.txt
    """
    transactionId: str
    accountId: str
    transactionDay: int
    category: str
    transactionAmount: float 

file_path = 'transactions.txt'

# empty list to be populated with data
transactions = []


def create_transactionDB() :
    """
    This method loads data into memory and
    creates data object that we work with
    """
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') # read the file
        next(csv_reader) # skip the header
        
        for row in csv_reader:
            transaction = Transaction(row[0], row[1], int(row[2]), row[3], float(row[4])) # build an object              
            transactions.append(transaction)            

    return transactions


trans = create_transactionDB() # loads data into the memory

# this is to make range caps dynamic
# stores all unique days of the trade
days = set()
for trans_days in trans:
    days.add(trans_days.transactionDay)


def daytrade_ops(trans):
        
    """
    Calculates the total transaciton value for all transactions for each day
    
    """
       
    for i in range (trans[0].transactionDay, len(days)+1): 
       day_amount = (sum([day.transactionAmount for day in trans if day.transactionDay == i]))
       print(f' Day {i} brought {day_amount:.2f} in total')

sorted_trans = sorted(trans, key=lambda x: (x.accountId, x.category)) # need to sort transactions or groupby won't work correctly (duplicates)

def trans_type(trans):
    """
    Calculates the average value of transactions per account for each type of transaction
    The output should contain one line per account, each line should include the account id and the average
    value for each transaction type (ie 7 fields containing the average values).

    """
    
    
    for k, g in groupby(sorted_trans, lambda x: (x.accountId, x.category)): #  grouping them by accountId and category

            cat_trans = [x.transactionAmount for x in g ] # list of transactionAmounts frouped by accountId and category
            total_trans = sum(cat_trans) # total value of transactionAmounts per accountId and category
            avg_val = total_trans / len(cat_trans) # average value of transactionAmounts per accountId and category
                        
            print(f'AccountId: {k[0]}, transaction type {k[1]}, average value per transaction {avg_val:.2F}') # prints the output
                
d = defaultdict(float)

def totals_per_cat(transactions):
    """
    Accumulates transactionAmount per accountId
    """
    for accountId, transactionAmount in chain.from_iterable(transactions):
                 d[accountId] += transactionAmount
    trans_res = list(d.values())
    
    return trans_res
    
def rolling_window(trans, window_size, day): # We pass data, window size and day to calculate from as arguments
    """
    Calculates statistics for each account number for the previous five days of transactions, not
    including transactions from the day statistics are being calculated for. 
    The maximum transaction value in the previous 5 days of transactions per account.
    The average transaction value of the previous 5 days of transactions per account.
    The total transaction value of transactions types “AA”, “CC” and “FF” in the previous 5 days per
    account
    """

    # Lists per category to be populated later
    trans_AA = []
    trans_CC = []
    trans_FF = []

    # the base length check
    if day <= window_size:
        return trans
       
    for i in range(day-window_size, day): # implementing the rolling window
                   
        # each filter through transactionAmounts, accountIds and populates corresponding lists 
        # according to the category
        trans_AA.append([(x.accountId, x.transactionAmount) for x in sorted_trans  if x.category == "AA"])
        trans_CC.append([(x.accountId, x.transactionAmount) for x in sorted_trans  if x.category == "CC"])
        trans_FF.append([(x.accountId, x.transactionAmount) for x in sorted_trans  if x.category == "FF"])

        trans_keys = (([(x.accountId) for x in sorted_trans])) # list of accountId to be used in trans_dict as keys
        trans_values = (([( x.transactionAmount) for x in sorted_trans])) # list of transactionAmount to be used in trans_dict as values
        
        trans_dict = {} # Will be populated and used for stat computations

        # Populates a dict to be later iterated for max and average values        
        for key, value in zip(trans_keys, trans_values):
            if key not in trans_dict:
                trans_dict[key] = [value]
            else:
                trans_dict[key].append(value)     

        # Updates a list of unique keys for the dinamic range value
        for accountId, transactionAmount in chain.from_iterable(trans_AA):
            d[accountId] += transactionAmount
        unique_keys_list = list(d.keys())

        # Final print statement:    
        for el in range(0, len(unique_keys_list)): # loop for iterating over the categorical lists AA CC FF
            for st, vals in trans_dict.items(): # loop for iterating over values from trans_dict to compute MAX and AVERAGE stats
                print(f'''Day {i}  Account ID    {st}    Maximum  {max(vals)}  Average   {mean(vals)}   AA total value {totals_per_cat(trans_AA)[el]} CC total value {totals_per_cat(trans_CC)[el]} FF total value {totals_per_cat(trans_FF)[el]}  ''')


if __name__ == "__main__":
    
    """
    Please uncomment them one by one (preferrably) before launching
    Letter on the side correspond to the number of questions they answer
    In rolling_window(Q3) the arguments are: data, size of the window, day from which you
    want to calculate the stats from
    """

    
    #daytrade_ops(trans) #Q1
    
    
    #trans_type(trans) #Q2

    
    rolling_window(trans, 5, 10) #Q3

