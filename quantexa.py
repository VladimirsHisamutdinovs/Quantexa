from collections import defaultdict
from dataclasses import dataclass, fields
from csv import DictReader
from statistics import mean
from typing import Dict, List


@dataclass
class Transaction:
    transactionId: str
    accountId: str
    transactionDay: int
    category: str
    transactionAmount: float 


def load_transactions(file_path: str) -> List[Transaction]:
    """
    This method loads data into memory and
    creates data object that we work with
    """
    with open(file_path) as csv_file:
        return [
            Transaction(**{
                field.name: field.type(row[field.name])
                for field in fields(Transaction)
            }) for row in DictReader(csv_file)
        ]

transactions = load_transactions('transactions.txt')

# this is to make range caps dynamic
# stores all unique days of the trade
days = set()
for trans_days in transactions:
    days.add(trans_days.transactionDay)


def question_one():
        
    """
    Calculates the total transaciton value for all transactions for each day
    
    """
       
    for i in range (transactions[0].transactionDay, len(days)+1): 
        day_amount = (sum([day.transactionAmount for day in transactions if day.transactionDay == i]))
        try:
            print(f' Day {i} brought {day_amount:.2f} in total')
        except ValueError:
            print("Value Error: Something went wrong, please try again.")

# Creates defaultdict with accountId as a key and rest as value
xact_by_acct: Dict[str, List[Transaction]] = defaultdict(list)
for xact in transactions:
    xact_by_acct[xact.accountId].append(xact)

def question_two():
    """
    Calculates the average value of transactions per account for each type of transaction
    The output should contain one line per account, each line should include the account id and the average
    value for each transaction type (ie 7 fields containing the average values).

    """
    for acct, xacts in xact_by_acct.items():
            sorted(xacts, key=lambda xact: xact.category )
            AA_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "AA"
            ]

            BB_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "BB"
            ]

            CC_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "CC"
            ]

            DD_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "DD"
            ]

            EE_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "EE"
            ]

            FF_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "FF"
            ] 

            GG_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "GG"
            ] 

            amts = [
                xact.transactionAmount for xact in xacts       
            ]  

            try:
                print(
                    f"Account: {acct}\t"
                    f"Average per category: AA: {mean(AA_amts):.2F}\t"
                    f"BB: {mean(BB_amts):.2F}\t"
                    f"CC: {mean(CC_amts):.2F}\t"
                    f"DD: {mean(DD_amts):.2F}\t"
                    f"EE: {mean(EE_amts):.2F}\t"
                    f"FF: {mean(FF_amts):.2F}\t"
                    f"GG: {mean(GG_amts):.2F}\t"
                    )
            except ValueError:
                pass

    
def question_three(day, window_size=5):

    for day in range(day-window_size, day):
        for acct, xacts in xact_by_acct.items():
            sorted(xacts, key=lambda xact: xact.category )
            # I promise to add a loop here over the weeked
            # Please trust me, I'm not retarded just didn't feel well today 
            AA_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "AA"
            ]

            CC_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "CC"
            ]

            FF_amts = [
                xact.transactionAmount for xact in xacts if xact.category == "FF"
            ]

            amts = [
                xact.transactionAmount for xact in xacts 
                if xact.transactionDay in range(day - window_size, day)
                
            ]  # all amounts within the window
            try:
                print(
                    f"Day: {day}\tAccount: {acct}\t"
                    f"Max: {max(amts)}\tAverage: {mean(amts):.2F}\t"
                    f"AA totals: {sum(AA_amts):.2F}\t CC totals: {sum(CC_amts):.2F}\t FF totals: {sum(FF_amts):.2F}\t" 
                )
            except ValueError:
                print("Value Error: No transactions in the window for this account.")
                

if __name__ == "__main__":
    
    """
    Please uncomment them one by one (preferrably) before launching
    """

    #question_one()
    #question_two()
    #question_three(10, 5)