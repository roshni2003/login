import json
import os
choose=input("enter you want login or signup (if you want signup choose (1) or you want login choose (2) = ")
l=[]
d={}
maindict={}
if choose=="1":
    username=input("please enter your full name = ")
    pass1=input("please enter your password(uppercase,lowercase,digit,special character) = ")
    upper=0
    lower=0
    digit=0
    special=0
    for i in pass1:
        if (i.isupper()):
            upper+=1
        if (i.isdigit()):
            digit+=1
        if (i.islower()):
            lower+=1
        if(i=='@'or i=='$' or i=='_' or i=='#'):
            special+=1
    if upper>=1 and lower>=1 and digit>=1 and special>=1:
        print("your password is valid ")
        pas2=input("please confirm your password = ")
        if pass1==pas2:
            print("your password is confirmed")
            description=input("Enter about you = ")
            birth_date=input("enter Your Date Of Birth= ")
            Gender=input("enter your Gender= ")
            hobbies=input("Enter Your hobby= ")
            d["description"]=description
            d["birth date"]=birth_date
            d["Gender"]=Gender
            d["Hobbies"]=hobbies
            d["Username"]=username
            d["Password"]=pass1
            if os.path.exists('userdetails.json')== True:
                myfile=open("userdetails.json")
                opened_file=json.load(myfile)
                l=opened_file['user']
                l.append(d)
                maindict["user"]=l
                myfile=open("userdetails.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
            else:
                l.append(d)
                maindict["user"]=l
                myfile=open("userdetails.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
                b=maindict
        else:
            print("your password is not confirmed! try again")        
    else:
        print("your password is not valid please try again")
elif choose=="2":
    user_name=input("enter your username= ")
    login_pas=input("enter your Log in Password= ")
    with open("userdetails.json","r") as x:
        login_info=json.load(x)
        flag=False
        for i in login_info["user"]:
            if i["Username"]==user_name and i["Password"]==login_pas:
                flag=True
                print("usrname = ",i["Username"])
                print("password = ",i["Password"])
                print("description = ",i["description"])
                print("birth date = ",i["birth date"])
                print("Gender = ",i["Gender"])
                print("Hobbies = ",i["Hobbies"])
                break
        if flag==False:
             print(" sorry! Password and username are Invalid please first login your profile information")
else:
    print("please choose only 1 or 2 ")