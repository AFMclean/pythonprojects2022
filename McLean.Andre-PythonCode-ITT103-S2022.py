#- Author: Andre F. McLean
#- Date Created: April 30th, 2022
#- Course: ITT103
#- Purpose: The purpose of this program is to calculate and then print the commission made by a sales person for an organization called Jamex.


def salesFunction1(sales_amt): 
         if sales_amt <1000: 
             rate = 1.06
             Comm_pay = sales_amt * rate
             print ("The total commission payment is $ ", Comm_pay)
         elif sales_amt > 1000 and sales_amt < 2000:
             rate = 1.07
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)
         else:
             rate = 1.1
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)

def salesFunction2(sales_amt):                          
        if sales_amt <= 1000:
             rate = 1.04                                     
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)
        elif sales_amt >= 1000:
             rate = 1.06                                   
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)      
            

def salesFunction3(sales_amt): 
            rate = 1.045 
            Comm_pay = sales_amt * rate
            print ("The total commission payment for SalesPerson: #, is $ ", Comm_pay)

def SalesAmt (sales_amt):
    while sales_amt < 1:
        print ("Invalid amount of sales entered, sales amount cannot be less than 1!")
        sales_amt = int(input ("Please enter the amount of sales made: "))
    
def exitp (salesClass):
        print ("You have chosen to end the transaction, thank you")
        import sys
        print("The program has ended! bye bye")
        sys.exit("Transaction terminated")
        
        

print ("Welcome to JamEx Limited Commission Receipt System.")
print ("To begin, kindly enter your assigned sales number below. ")
emp_number = input ("Enter Sales number here:  ")
print ("Thank you!")

salesClass =input("Please enter Sales Class: '1' = Class 1, '2' = Class 2, '3' = Class 3 or '4' to end: ")
saleClass = int(salesClass)
#exitp(salesClass)
sales_amt = input("Please enter the amount of sales made: ")
sales_amt = int(sales_amt)

SalesAmt(sales_amt)
    #sales_amt = int(sales_amt)

while salesClass != '4':
    if salesClass == '1':
                SalesAmt(sales_amt)
                salesFunction1(sales_amt)
    elif salesClass == '2':
                SalesAmt(sales_amt)
                salesFunction2(sales_amt)
    elif salesClass == '3':
                SalesAmt(sales_amt)
                salesFunction3(sales_amt)                
    else:
                print ("Invalid input, please try again!")

    salesClass = input("To complete another print request enter a class: '1' for Class 1, '2' for Class 2, '3' for Class 3 or '4' to end : ")
    #exitp(salesClass)
    if salesClass == '4':
        exitp(salesClass)
    else:
            sales_amt = input ("Please enter the amount of sales made: ")
            sales_amt = int(sales_amt)


exitp(salesClass)
