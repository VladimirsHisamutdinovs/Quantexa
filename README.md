# Quantexa
This is a technical task for Junior Big Data Engineer performed in Python. 
Main file with the solution is called quantexa.py
File with transactions is called transactions.txt (please save it to the same dir as the file or provide absolute path for it to function properly)
Please uncoment method calls at the bottom of the file to see the answers on Q1, Q2, Q3

## Data
The data provided is stored within transactions.txt and consists of 991 transactions presented in a comma separated format and spread over a month. The transactions are for multiple accounts and there are multiple types of transaction. The file has the following columns:
* transactionId: String representing the id of a transaction
* accountId: String representing the id of the account which made the transaction transaction
* day: Integer representing the day the transaction was made on (time information was removed)
* category: String representing the type of category of the transaction 
* transactionAmount: Double representing the value of the transaction

## Output
Q1 output calculates the total transaction value for all transactions performed each day over the month. The output contains one line for each day and each line includes the day and the total value.
Q2 output calculates the average value of transactions per account for each type of transaction (there are seven in total). 
The output presents one line per account and per category (transaction type). Each line includes the account id and the average value of the transaction type.
Q3 output For each day, each account has transaction statistics calculated for five days prior (not including transactions from the day itself). The output has one line per day per account id and each line has each of the calculated statistics. The statistics are:
The maximum transaction value in the previous 5 days of transactions per account
The average transaction value of the previous 5 days of transactions per account
The total transaction value of transactions types “AA”, “CC” and “FF” in the previous 5 days per account
IMPORTANT: for Q3, the method expects the day from which you want to calculate your stats from and the size of the window. 
