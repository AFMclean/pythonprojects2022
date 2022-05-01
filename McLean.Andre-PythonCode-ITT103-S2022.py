#- Author: Andre F. McLean
#- Date Created: April 30th, 2022
#- Course: ITT103
#- Purpose: The purpose of this program is to calculate and then print the commission made by a sales person for an organization called Jamex.

#SalesFunction1 is called once the user selects class 1, then calculates and prints the commission.
def salesFunction1(sales_amt):
    if sales_amt <1000: 
        rate = 1.06
        Comm_pay = sales_amt * rate
        print ("The total commission payment is $ ", Comm_pay)
    elif sales_amt > 1000 and sales_amt < 2000:
        rate = 1.07
        Comm_pay = sales_amt * rate
        print ("The total commission payment for : is $ ", Comm_pay)
    else:
        rate = 1.1
        Comm_pay = sales_amt * rate
        print ("The total commission payment for : is $ ", Comm_pay)
        
#SalesFunction2 is called once the user selects class 2, then calculates and prints the commission.
def salesFunction2(sales_amt):
        if sales_amt <= 1000:
             rate = 1.04                                     
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)
        elif sales_amt >= 1000:
             rate = 1.06                                   
             Comm_pay = sales_amt * rate
             print ("The total commission payment for SalesPerson: is $ ", Comm_pay)      
            
#SalesFunctio31 is called once the user selects class 3, then calculates and prints the commission.    
def salesFunction3(sales_amt):
    rate = 1.045 
    Comm_pay = sales_amt * rate
    print ("The total commission payment for SalesPerson: is $ ", Comm_pay)

#SalesAmt is used to request the amount of sales made by the user and then validates if the entry is accurate. Any figure less than 1 is not acceptable.
def SalesAmt ():
    sales_amt = int(input ("Please enter the amount of sales made: "))
    while(sales_amt <= 0):
        sales_amt = input("Invalid Entry!! Please enter the amount of sales made (any value less than 1 is not valid: ")
        sales_amt = int(sales_amt)
    return sales_amt

#exitp is a function that uses import sys to end/terminate the program once an invalid enter for the class is received or when the user decides to end the program    
def exitp (salesClass):
        print ("You have chosen to end the transaction, thank you")
        import sys
        print("The program has ended! bye bye")
        sys.exit("Transaction terminated") 

#START
print ("Welcome to JamEx Limited Commission Receipt System.")

#lets ask the customer for the sales  number, we only ask this once. A user can work in multiple classes each week and as the organization requires.
#the sales number is like an identification number for the user and only one user can use the system at a time to print the commission pay.
print ("To begin, kindly enter your assigned sales number below. ")
emp_number = input ("Enter Sales number here:  ")
print ("Thank you!")

#lets ask the customer for the sales class, the sales class is like different departments/ areas of work within the organization and does generate a different sales commission based on the ammount.
salesClass =input("Please enter Sales Class: '1' = Class 1, '2' = Class 2, '3' = Class 3 or any other number to end: ")
saleClass = int(salesClass)

#any other sales class type will end the program
if salesClass < '1' or salesClass > '3':
    exitp(salesClass)
else:
    print("Entry validated!!")

#Calling SalesAmt function to accept the amount of sales the user has made and then checks to see if the entry is within the criteria (1 or greater).
sales_amt = SalesAmt()
  
#while loop to ensure that the user can make multiple print request per sales 
while salesClass != '4':
    if salesClass == '1':
                
                salesFunction1(sales_amt)
    elif salesClass == '2':
                
                salesFunction2(sales_amt)
    elif salesClass == '3':
                
                salesFunction3(sales_amt)                
    else:
                print ("Invalid input, please try again!")

    salesClass = input("To complete another print request enter a class: '1' for Class 1, '2' for Class 2, '3' for Class 3 or any other number to end: : ")
    
    if salesClass < '1' or salesClass > '3':
        exitp(salesClass)
    else:
            sales_amt = SalesAmt()
            
#exitp is called to check the salesclass entered and then end the program if the user decides to end or the value is not within the criteria.
exitp(salesClass)
