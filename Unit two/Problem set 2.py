# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:24:56 2021

@author: Maxi
"""
### PROBLEM SET 2

# Program 1
def program(balance,annualInterestRate,monthlyPaymentRate):
    ''''''''''
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal
    '''''''''''
    for i in range(0,12):
        min_payment = balance*monthlyPaymentRate
        unpaid_balance = balance-min_payment
        interest= (annualInterestRate/12.0)*unpaid_balance
        balance = unpaid_balance+interest
        #print("Remaining Balance of month ",i, " is: ", round(balance,2))
    print("Remaining Balance:", round(balance,2))
    
    
program(484,0.2,0.04)


# Program 2
#the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
def program2(balance,annualInterestRate):
    ''''''''''
    #balance - the outstanding balance on the credit card

    #annualInterestRate - annual interest rate as a decimal

    #monthlyPaymentRate - minimum monthly payment rate as a decimal
    
    #the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
    '''''''''''
    balance_ver = balance
    min_payment = 0
    while balance_ver>0: 
        min_payment +=10
        balance_ver = balance
        for i in range(0,12):
            unpaid_balance = balance_ver-min_payment
            interest= (annualInterestRate/12.0)*unpaid_balance
            balance_ver = unpaid_balance+interest
            print(i, balance_ver)
    return print("Lowest Payement: ", min_payment)
            
program2(5000,0.18)


## Program 3

#the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
def program3(balance,annualInterestRate):
    ''''''''''
    #balance - the outstanding balance on the credit card

    #annualInterestRate - annual interest rate as a decimal

    #monthlyPaymentRate - minimum monthly payment rate as a decimal
    
    #the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
    '''''''''''
    low = balance/12
    high = (balance*((1+annualInterestRate)**12))/12
    ans = (low+high)/2
    balance_ver = balance
    min_payment = 0
    while round(balance_ver,10)!=0: 
        min_payment = ans
        balance_ver = balance
        for i in range(0,12):
            unpaid_balance = balance_ver-min_payment
            interest= (annualInterestRate/12.0)*unpaid_balance
            balance_ver = unpaid_balance+interest
            print(i, balance_ver)
        if balance_ver < 0:
            high = ans
            ans = (low+high)/2
        else:
            low = ans
            ans = (low+high)/2
    return print("Lowest Payement: ", min_payment)
            
program3(5000,0.18)

