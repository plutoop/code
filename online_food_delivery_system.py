print('''                                          -------------INTRODUCTION---------------
Online food ordering system Allows user to ordering food from a website or other application. The product can be eitherready-to-eat food
(e.g., direct from a home-kitchen, restaurant, or a ghost kitchen)  

Our Purpose is to make a program that can take essential information for ordering food from the user, making profile for the user, take order,
send order confirmation, cancel Order etc. 

We can also use this idea in to real life by creating an app that can function the same and launch it for public use and generate revenue
for each order. Not only this will connect the restaurants directly to the consumer but will also generate jobs for people who will deliver
the food to the Consumer directly from the restaurant.''') 
print()
print()
print()
print('                                        -------------------OUR-GOAL---------------------')
print()
print()
print()
print('''Our goal to achieve is that to connect as many consumer (especially who cannot cook themselves)
directly to the restaurants by charging minimum taxes on their order so they can easily order food and also provide
them promo codes for discount on their food  

Our main aim is to generate employability 
all over the India and also promote small food business to grow fast. 

The records of data of the user info and their order history will be saved in our database systems securely.  ''')
print()
print()
print()
print('                                  -----------------------FUTURE-SCOPE------------------------------------')
print()
print()
print()
print('''The Future scope of this project that we can built a real-life  working application that
        function the same as our project code and launch it in the market for public use and to generate employability in all over the India. ''')

print()
print()
print()
print()
print()
print()
print()                    #-------------------------IMPORTING ALL THE MODULES NEEDED------------------------------------#
import mysql.connector as sqltor
import random
#----------------------------------------------------------CREATING ALL THE FIXED VARIABLE NEEDED------------------------------------------------------#
x=random.randint(30,50)
con =sqltor.connect(host='localhost',user='root',password='zishan123',database='online_food_delivery_system')
TOTAL_MONEY=0
DELIVERY_TAX=30
FIXED_TAX=10
cart=[]
                    #--------------------------------------------------MAIN_PROGRAM_STARTED----------------------------------------------------------------------------#
print('------------------------------------------------WELCOME_TO_ONLINE_FOOD_DELIVERY_SYSTEM--------------------------------------------')

            #----------------------------------------------------------ASKING THE PERSONAL------------------------------------------------------------------------#
def PERSONAL_DATA():
    global NAME
    global ADDRESS
    global EMAIL
    global PHONE_NO
    NAME=(input('PLEASE ENTER YOUR NAME:-'))
    ADDRESS=input('PLEASE ENTER YOUR ADDRESS')
    EMAIL=input('PLEASE ENTER YOUR EMAIL ADDRESS')
    PHONE_NO=int(input('PLEASE ENTER THE PHONE NO'))

PERSONAL_DATA()

                 #---------------------------------------------FUNCTION_CREATED_PERSONAL_DATA---------------------------------------------------#

cur=con.cursor()
cur.execute('select* from menu')
data=cur.fetchmany(3)
print()
print()
print('----------------------------------------------------WHAT DO YOU WANT TO EAT--------------------------------------------------------------------------')

print()

print()

print()
     #----------------------------------------------------------------------ASKING_SOME_CHOICES-------------------------------------------------------------------------------#
while True:
    print('---------------------------------------------------','SERIAL_NO',',','CATEGORY','------------------------------------------------------------------------------------')


    for i in data:
    
        print('                                                   ',i,'')

    choice1=int(input('ENTER THE CHOICE OF CATEGORY ACCORDING TO SERIAL NO,ENTER "4"  If YOUR ORDERING IS DONE:-'))
    if choice1==1:
        print('YOUR CHOICE OF CATEGORY IS INDIAN')
        cur.execute('select* from Indian')
        data1=cur.fetchmany(7)
        print('---------------------------------------------------','S_NO','DISH NAME','RATE','------------------------------------------------------------------------------------')
        for i in data1:
            print('                                                ',i,'')
        n=int(input('ENTER THE CHOICE OF DISH ACCORDING TO SERIAL NO'))
        TOTAL_MONEY+=data1[n-1][2]
        cart.append(data1[n-1])
        continue
    elif choice1==2:
        print('YOUR CHOICE OF CATEGORY IS AMERICAN')
        cur.execute('select* from Amarican')
        data1=cur.fetchmany(7)
        print('---------------------------------------------------','S_NO','DISH NAME','RATE','------------------------------------------------------------------------------------')
        for i in data1:
            print('                                                ',i,'')
        n=int(input('ENTER THE CHOICE OF DISH ACCORDING TO SERIAL NO'))
        TOTAL_MONEY+=data1[n-1][2]
        cart.append(data1[n-1])
        continue
    elif choice1==3:
        print('YOUR CHOICE OF CATEGORY IS ITALIAN')
        cur.execute('select* from Italian')
        data1=cur.fetchmany(7)
        print('---------------------------------------------------','S_NO','DISH NAME','RATE','------------------------------------------------------------------------------------')
        for i in data1:
            print('                                                ',i,'')
        n=int(input('ENTER THE CHOICE OF DISH ACCORDING TO SERIAL NO'))
        TOTAL_MONEY+=data1[n-1][2]
        cart.append(data1[n-1])
        continue
    else:
        print("WAIT UNTILL WE CALCULATE TOTAL COST")
        break
print()
print()
       #-----------------------------------------------------SHOWING_ALL_THE CHOICES_STORED_IN_THE_CART-------------------------------------------------------------#

if len(cart)!=0:
    print('                                                   YOUR TOTAL ITEMS IN THE CART IS:-                                                   ')
    print('---------------------------------------------------','S_NO','DISH NAME','RATE','------------------------------------------------------------------------------------')  
    for i in cart:
        print('                                                    ',i,'')
    choice5=int(input('DO YOU WANT TO REMOVE ANYTHING FROM THE CART(PRESS 1 FOR YES):-'))
    while choice5==1:
        choice4=int(input('PLEASE ENTER THE POSITION OF THE DIST_NAME YOU WANT TO REMOVE'))
        a=cart.pop((choice4)-1)
        TOTAL_MONEY=TOTAL_MONEY-(a[2])
        print('YOUR NEW ITEMS IN THE CART IS')
        print('---------------------------------------------------','S_NO','DISH NAME','RATE','------------------------------------------------------------------------------------')  
        for i in cart:
            print('                                                    ',i,'')
        if len(cart)!=0:

            choice5=int(input('DO YOU WANT TO REMOVE ANYTHING ELSE FROM THE CART(PRESS 1 FOR YES):-'))
        else:
            break
print()
print()
print()

if len(cart) !=0:
    print('YOUR TOTAL AMOUNT ',TOTAL_MONEY)
    print('ADDING SOME DISCOUNT COUPONS')      
    print()
    print()
        #--------------------------------------------------DEDUCTING_SOME_MONEY_ACCORDING_TO_THE_DISCOUNT_APPLIED------------------------------------------------------# 
    print()
    print('DISCOUNT ADDED',x,'%')
    print('ADDING DELIVERY TAX ',DELIVERY_TAX,'AND FIXED TAX',FIXED_TAX)
        #----------------------------------------------------ADDING_SOME_DELIVERY_TAX&FIXED_TAX----------------------------------------------------------------------------#
    print('YOUR TOTAL AMOUNT AFTER ADDING DISCOUNT',(TOTAL_MONEY-((TOTAL_MONEY)*(x/100)))+DELIVERY_TAX+FIXED_TAX)


    conti=int(input('--------------------DO YOU WANT TO CONTINUE THE FINAL ORDERING(1 FOR YES) '))
           #-----------------------------------------------------FINALIZING_THE_ORDER_BY_ASKING_CONFIRMATION_FROM_THE_USER------------------------------------------------------#
    if conti==1:
        print()
        print('--------------------YOUR NAME:-',NAME,'ADDRESS WHERE YOU LIVE:-',ADDRESS,'CONTACT NO:-',PHONE_NO,'EMAIL ADDRESS:-',EMAIL,'---------------------------')
        print('---------------------YOUR ORDER WILL BE DELIVERED BY SANJAY KUMAR WITH IN 30 MINUTES THE DETAILS HAVE BEEN SENT TO YOUR EMAIL ADDRESS ABOUT THE DELIVERY MAN---------------')
        print('-------------------------------------THANK YOU FOR USING OUR PROGRAM FOR ORDERING FOOD-----------------------------------------')
        print('------------------------------------------------ITS BEEN AN HONOUR -----------------------------------')
        print('---------------------------------------------COME BACK LATER-------------------------------------------------------------------------------')
        #==================================================================CANCELING_THE_ORDER================================================================================#
else:
    print('------------------------------------------------COME BACK LATER-------------------------------------------------------------------------------')
