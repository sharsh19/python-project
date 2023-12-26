#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' this programme is made as a prototype to generate gmail of a user using his/her input data.

Year of creation: 2023
Date of creation: 23 october
Time of creation: 7:55 PM
date of complatation:26 october
time of complatation:10:30 PM
Language used: python
interpretor: jupyter

module used:
RAND0M
function used : input,if elif,else,isalpha,isalnum,isdigit,for(loop),len
by: HARSH
'''





import random as r

fname=str(input("your first name::-"))
first=fname.upper()
lenn1=len(fname)
if not fname.isalpha():
    print("name cant be numeric")
elif lenn1>=10 or lenn1<=3:
    print("limit exceed! or max 4 character ")        
elif fname==" ":
    print("name cant be blank")
else:    
    lname=str(input("your last name::-"))
    last=lname.upper()
    lenn2=len(lname)
    if not lname.isalpha():
        print("name cant be numeric")
    elif lenn2>=10 or lenn2<=3:
        print("limit exceed! or max 4 character ") 
    elif lname==" ":
        print("name cant be blank")
    else:    
        contact=(input("mobile number::-"))
        lenn3=len(contact)
        if contact==" ":
            print("number cant be blank")
        elif lenn3>=11 or lenn3<10:
            print("number more than 10 or not proper ")     
        elif not contact.isdigit():
            print("number cant be alphabetic")
        else:
            date=input("enter date of birth(00)::-")
            intt2=int(date)
            lenn4=len(date)
            dates=[y for y in range(1,31)]
            if date==" ":
                print("date cant be blank")
            elif intt2<1 or intt2>31:
                print("enter valid date or exceed! ")    
            elif lenn4>=3 or lenn4<1:
                print("length exceed ")       
            elif not date.isdigit():
                print("enter numeric format(00)")
            else:
                month=str(input("enter your birth month(jan)::- "))
                big=month.upper()
                months=('january,february,march,april,may,june,july,august,september,october,november,december')
                if month==" ":
                    print("month cant be blank")
                elif not month in months:
                    print("month not match with months name")
                elif not month.isalpha():
                    print("please enter full month name")
                else:
                    year=input("enter birth year(0000)::-")
                    intt=int(year)
                    lenn5=len(year)
                    years=[y for y in range(1940,2099)]
                    if year==" ":
                        print("year cant be blank")
                    elif intt<=1940 or intt>2099:
                        print("enter valid age ( from 1940) or exceed! ")
                    elif lenn5>=5:
                        print("age character exceed")
                    elif not year.isdigit():
                        print("please enter in numeric::- ")
                    else:
                        print("")
                        print('''DO YOU HERE BY CONFIRMS THAT ABOVE INFORMATION IS CORRECT AND ALLOWS OUR TERMS AND CONDITIONS!
                                         
                        ''')
                        print("                     PLEASE SELECT (y=yes n=no)")
                        
                        conformation=input("enter(y/n)::-  ")
                        if conformation=="n":
                            print("sorry u declined")
                        elif conformation=="y" :    
                            
                            range1=r.randrange(4,10,1)
                            join1=str(range1)
                            
                            range2=r.randrange(1,10,3)
                            join2=str(range2)
                            
                            range3=r.randrange(5,10)
                            join3=str(range3)
                            
                            lower=first.lower()
                            lower2=last.lower()
                            print("")
                            print('''                        --[USER INFO]--          ''')
                            
                            print("first name:>",first)
                            print("last name:>",last)
                            print("contact:>","(+91)"+("")+contact)
                            print("DOB:>",date+"-"+big+"-"+year)
                            print("your email id is_")

                            print("")
                            print(lower+join1+join2+"@gmail.com")
                            print("        or")
                            print(lower2+join2+join1+join3+"@gmail.com")
                            print("        or")
                            print(lower+lower2+join3+join1+"@gmail.com")
                            print("        or")
                            print(lower2+lower+join2+join3+"@gmail.com")
                            
                        else:
                            print("wrong input")
                            

