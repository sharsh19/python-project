#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ORIGINAL CODE

'''  this programme is made as a prototype of a BANK page as dream account

Year of creation: 2023
Date of creation: 26 December
Date of complatation: 
Time of creation: 2:57 PM
Language used: python
interpretor: jupyter

module used:


function used :
key used:
Error Handler:
'''

print('''                    BANK OF CONVENIENT
               _______________________________
    [we understand you , we support you, we respect you dreams]
     ===========================================================
         
>>> welcome to the DREAM ACCOUNT page of BANK OF CONVINENT<<<
                       AMOUNT/TIME CHART
     >>DREAM AMOUNT<<                     >>MINIMUM TIME OF WITHDRAWL<<             
    50K - 2LAKH                              3-MONTHS                               
    2LAKH - 5LAKH                           6-MONTHS
    5LAKH - 10LAKH                          10-MONTHS
    10LAKH - 18 LAKH                        12-MONTHS
    18LAKH - 25 LAKH                        15-MONTHS
    25LAKH - 40 LAKH                        18-MONTHS
    40LAKH ABOVE (1cr)                      21-MONTHS


--please select  your required option

               1-CREATE ACCOUNT YOUR "DREAM ACCOUNT"
               2-DEPOSITE MONEY
               3-CHECK DREAM ACCOUNT BALANCE
               4-EXIT
''')
import random
import math
from colorama import Fore
import time
import pyautogui
amount=0
global deposit_amount
deposit_amount=0
global customer_dream_amount
customer_dream_amount=0

while True:
    try:
        customer_option =input("Enter_Your_option:--")
        customer_option2=int(customer_option)
        if  not customer_option.isdigit():
            print("WRONG INPUT\n ENTER VALID OPTION")
        elif customer_option== " ":
            print("BLANK INPUT")    
        #options
        if customer_option2== 1:
            print(" ")
            print("PERSONAL DETAILS")
            print(" ")
            #input validations
                 #NAME
            customer_name = input("FULL NAME:--")
            lenn1=len(customer_name)
            if lenn1>=16 or lenn1<=2:
                pyautogui.alert("Name too short!")
                print("Name is too short\n Character Limit(16) Exceed !")
            elif customer_name.isdigit():
                print("Name can't be Numeric")
            elif customer_name==" ":
                print("Name is Mandatory!")
            else:
                customer_contact = input("CONTACT NO:--")
                lenn2=len(customer_contact)
                if not customer_contact.isdigit():
                    print("Contact can't be alphabatic!")
                elif lenn2<=9:
                    print("Contact input less than 10!")
                elif lenn2>=11:
                    print("Contact input more than 10!")
                elif customer_contact==" ":
                    print("Contact is Mandatory!")
                else:
                    customer_email_id = input("EMAIL ID:--")
                    if customer_email_id==" ":
                        print("Email is Mandatory!")
                    else:
                        customer_gender = input("GENDER:--")
                        genders=('male,MALE,Male,FEMALE,Female,female,TRANSGENDER,Transgender,transgender')
                        if not customer_gender in genders:
                            print("Mismatch Gender!")
                        elif customer_gender== " ":
                            print("Gender is Mandatory!")
                        elif customer_gender.isdigit():
                             print("Invalid Input!")
                        else:
                            Customer_YOB=input("YEAR OF BIRTH(0000):--")
                            customer_yob_int=int(Customer_YOB)
                            valid_years=[y for y in range(1940,2099) ]
                            current_year=2024
                            if Customer_YOB==" ":
                                print("MANDATORY OPTION!")
                            elif  (current_year-customer_yob_int)<16:
                                pyautogui.alert("YOU MUST BE 16 YEAR OR OLDER! ")
                                print("YOU ARE NOT OF 16 YEARS!")
                            elif not Customer_YOB.isdigit():
                                print("INVALID INPUT!(abc)")
                            else:
                                pyautogui.alert("AGE VERIFICATION\nyou are over 16 years")
                                customer_DOB = input("D.O.B(dd/mm/yyyy):--")
                                if customer_DOB==" ":
                                    print("DOB is Mandatory!")
                                elif customer_DOB.isalpha():
                                    print("Invalid Date Format!")
                                else:
                                    customer_pan = input("PAN NO:--")
                                    if customer_pan==" ":
                                        print("PAN is mandatory!")
                                    else:
                                        customer_status = input("STATUS(student/bussiness):--")
                                        lenn4=len(customer_status)
                                        if not  customer_status.isalpha():
                                            print("INVALID INPUT!")
                                        elif customer_status==" ":
                                            print("STATUS is Mandatory !")
                                        elif lenn4>=16 or lenn4<=4:
                                            print("STATUS can't be short\n Character Exceed!")
                                            print(" ")
                                            print("please enter your dream amount, amount to be collected for your dream..")
                                        else:
                                            customer_dream_amount = input("DREAM AMOUNT:--")
                                            lenn5=len(customer_dream_amount)
                                            if lenn5>=8:
                                                print("AMOUNT LIMIT EXCEED!")
                                            elif lenn5<=4:
                                                print("AMOUNT ENTERED TOO SHORT!")
                                            elif not customer_dream_amount.isdigit():
                                                print("INVALID INPUT")
                                            else:
                                                customer_nationality = input("NATIONALITY:--")
                                                nationality=['indian','INDIAN','Indian']
                                                
                                                if not customer_nationality.isalpha():
                                                    print("INVALID INPUT")    
                                                elif customer_nationality not in nationality:
                                                    print("Nationality Must be\n INDAIN ! ")
                                                else:
                                                    
                                                    customer_address = str(input("LANDMARK/STREET:--"))
                                                    customer_location = str(input("CITY:--"))
                                                    customer_state = str(input("STATE:--"))
                                                    customer_pincode = input("PINCODE:--")
                                                    lenn6=len(customer_pincode)
                                                    str_pincode = str( customer_pincode)
                                                    if customer_pincode== " ":
                                                        print("MANDATORY SECTION !")
                                                    elif not customer_pincode.isdigit():
                                                        print("INVALID INPUT")
                                                    elif lenn6>=7:
                                                        print("INVALID PINCODE")
                                                    elif lenn6<=5:
                                                        print("PINCODE TOO SHORT !")
                                                        print(" ")
                                                        print("PERENTAL DETAILS:-")
                                                        print(" ")
                                                    else:   
                                                        fathers_name = input("GUARDIAN NAME:--")
                                                        lenn7=len(fathers_name)
                                                        if lenn7>=16 or lenn7<=2:
                                                            print("father's Name is too short\n Character Limit(16) Exceed !")
                                                        elif  fathers_name.isdigit():
                                                            print("Name can't be Numeric")
                                                        elif fathers_name== "  ":
                                                            print(" father's Name is Mandatory!")
                                                        else:
                                                            mothers_name = input("MOTHERS NAME:--")
                                                            lenn8=len(mothers_name)
                                                            if lenn8>=16 or lenn8<=2:
                                                                print("mother's Name is too short\n Character Limit(16) Exceed !")
                                                            elif  mothers_name.isdigit():
                                                                print("Name can't be Numeric")
                                                            elif mothers_name==" ":
                                                                print("mother's Name is Mandatory!")
                                                            else:
                                                                parent_husband_contact = input("GUARDIAN CONTACT NO:--")
                                                                lenn9=len(parent_husband_contact)
                                                                if not  parent_husband_contact.isdigit():
                                                                    print("Contact can't be alphabatic!")
                                                                elif lenn9>=11:
                                                                    print("Contact input more than 10!")
                                                                elif lenn9<=9:
                                                                    print("Contact input Less than 10!")
                                                                elif parent_husband_contact==" ":
                                                                    print("Contact is Mandatory!")
                                                                else:
                                                                    nomine_name = (input("NOMINEE NAME:--"))
                                                                    lenn10=len(nomine_name)
                                                                    if lenn10>=16 or lenn10<=2:
                                                                        print(" Nominee's Name is too short\n Character Limit(16) Exceed !")
                                                                    elif  nomine_name.isdigit():
                                                                        print("Name can't be Numeric")
                                                                    elif nomine_name== " ":
                                                                        print("Name is Mandatory!")
                                                                    else:
                                                                        nominee_contact = (input("NOMINEE CONTACT NO.:--"))
                                                                        lenn11=len(parent_husband_contact)
                                                                        if not nominee_contact.isdigit():
                                                                            print("Contact can't be alphabatic!")
                                                                        elif lenn11>=11:
                                                                            print("Contact input more than 10!")
                                                                        elif lenn11<=9:
                                                                            print("Contact input Less than 10!")
                                                                        elif nominee_contact== "  ":
                                                                            print("Contact is Mandatory!")
                                                                        else:
                                                                            nominee_pan = input("NOMINEE PAN NO:--")
                                                                            if nominee_pan==" ":
                                                                                pyautogui.alert("PAN is mandatory!")
                                                                            else:
                                                                                print(" ")
                                                                                sample1=str(customer_contact)
                                                                                sample2=str(customer_pincode)
                                                                                slice1=slice(-4)
                                                                                slice2=slice(2)
                                                                                UID="CNVT"+sample1[slice1]+sample2[slice2]#......................................................................
                                                                                
                                                                                print('''    
                                TERMS & CONDITION   
                         __________________________________
         Acording to the terms and condition of this DREAM account,
         you can't be able to withdrawl your balance, possible only when 
         its circumstances beyond one's control.a certain amount of intrest 
         will be deduced from account balance at that circumstance.avability 
         of account holder and nominee is compusolry with  each individual proof
         identity.minimum time of wihtdrawl is 3 months maximum depends upon the 
         DREAM amount.
                                                             :-- BANK OF CONVINENT                                                                   
                                                                                 ''')
                                                                                 
                                                                                print(" ")
                                                                                
                                                                                print('''
                        I here by declares that, information given above is true
                        and agrees all TERMS & CONDITION applied on this process.
            
            
                            press(ok) to agree the TERM & CONDITION OF BANK
                        _______________________________________________________
                        Select "y" for yes|"n" for no to agree TERMS & CONDITION
                                                                                ''')
                                                                                
                                                                                
                                                                                user_response = input("select(y/n):--")
                                                                                
                                                                                
                                                                                if user_response== "y":
                                                                                    pyautogui.confirm('AGREE TERMS & CONDITION')
                                                                                if pyautogui.confirm('AGREE TERMS & CONDITION')=='OK':
                                                                                    
                                                                                    print(" ")
                                                                                    print("UID:"+Fore.RED+UID)
                                                                                    print("            "+Fore.WHITE+"CUSTOMER DETAILS")
                                                                                    print("CONTACT:-"+"(+91)",customer_contact)
                                                                                    print("EMAIL ID:-",customer_email_id)
                                                                                    print("D.O.B:-",customer_DOB)
                                                                                    print("PAN ID:-",customer_pan)
                                                                                    print("ADDRESS:-",customer_address.upper()+","+customer_location.upper()+","+ str_pincode+","+customer_state.upper())
                                                                                    print("DREAM DEPOSIT:-"+"INR",customer_dream_amount,".00" )
                                                                                    time.sleep(2)
                                                                                    pyautogui.confirm("                "+"   CONGRATULATIONS\n ACCOUNT HAS BEEN CREATED SUCCESSFULLY")
                                                                                    time.sleep(1)
                                                                                    print(" ")
                                                                                    print("DREAM ACCOUNT HAS BEEN CREATED!")
                                                                                    print("        ",u'\N{check mark}')
                                                                                      
                                                                                elif pyautogui.confirm('agree TERMS & CONDITION')=='Cancel':
                                                                                    pyautogui.alert('please agree to proceed')
                                                                                             
                                                                                elif user_response== "n":
                                                                                    pyautogui.alert('please agree to proceed')
                                                                                    time.sleep(2)
                                                                                    print("Agreement DECLINED")
                                                                                    print(" ")
                                                                                  ##DEPOSITE FUNCTION  
        elif customer_option2== 2:
            CONTACT =input("REGISTERED CONTACT NO:-")
            EMAIL= input("REGISTERED EMAIL ID:-")
            if CONTACT==customer_contact and EMAIL==customer_email_id: 
                deposit_amount = int(input("DEPOSIT AMOUNT:--"))
                time.sleep(1)
                print("please wait...")
                time.sleep(1)
                pyautogui.confirm('AMOUNT DEPOSITED')
                print(" ")
                print("SUCCESSFULLY DEPOSITED ")
                print("        ",u'\N{check mark}')
                time.sleep(2)
                print(" ")
                print(Fore.RED+"congratulations!")
                print("AMOUNT DEPOSITED, YOUR ARE FEW STEP AWAY TO YOUR DREAM")
                print("Total Amount:-"+"INR",deposit_amount,".00")   
                print(" ")
                print("WELL DONE !")
                print("THANK YOU FOR BANKING WITH US! HAVE A PLEASENT DAY! ")
            else:
                print("NO ACCOUNT FOUND")
                pyautogui.alert('INVALID ACCOUNT !')
                print(" ")
            ## CHECKING BALANCE FUNCTION
        elif customer_option2== 3:
            CONTACT = int(input("REGISTERED CONTACT NO:-"))
            EMAIL= input("REGISTERED EMAIL ID:-")
            print(" ")
            if CONTACT==customer_contact and EMAIL==customer_email_id:
                print("DREAM AMOUNT:-", customer_dream_amount)
                print(" ")
                print("CURRENT DREAM BALANCE--"+"INR",deposit_amount,".00")
                print(" ")
                print("left dream balance to be deposited:-"+"INR", customer_dream_amount-deposit_amount,".00")
                print(" ")
                print("WELL DONE !")
                print("THANK YOU FOR BANKING WITH US! HAVE A PLEASENT DAY! ")
                print(" ")
            else:
                print("NO ACCOUNT FOUND")
                pyautogui.alert('INVALID ACCOUNT !')
                print(" ")
                
        elif customer_option== 4:
            break
    except Exception as e:
         print("something error",e)
                                  
     

