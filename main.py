
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json


import sys


app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")


user={}



def load_users():
    global user
    if os.path.exists("Credentials.txt"):
        with open("Credentials.txt", "r") as f:
            try:
                user = json.load(f)
            except json.JSONDecodeError:
                user = {}
    else:
        user = {}

def save_users():
    with open("Credentials.txt", "a") as f:
        json.dump(user, f)






def create_user():
    global user
    try:
        print(".......Create an Account.........")
        name = str(input("create your username...."))
        load_users()
        
        if name in user:
            print("Username already exists! Try again.")
            sys.exit()
        
    except Exception as e:
            print("Error loading credential file:", e)
            user = {}
    else:
        user = {}

        
    try:
        code = int(input("Input your desired code: "))
        user[name] = code
        save_users()
        print("........Successfully Created......")
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)

        
       
       
        print("........Successfully Created......")
        user[name] = code
        # storing a data in the file
        with open("Credentials.txt", "w") as f:
            f.write(str(user))

        
        # #append
        # f = open("Credentials.txt","a")
        # credentials = user
        # f.write(str(credentials))
        # f.close()
        


    except Exception as e:
        print(e)
        sys.exit(1)

    


    
def authentication(func):
    def employee():
       global user
       attempt = 0
       while True:
            username = str(input("Enter your username......"))
            passcode = int(input("Enter the Code..."))
            func()
            
            if username in user and user[username] == passcode:
                print("Authenticated")
                print("Access Granted...Thank you!!")
                a = input("Do you want to change your code...")
                if a.lower() == "yes":
                    new_code = int(input("Enter the new code..."))
                    user[username] = new_code
                    print("changed successfully")
                    employee()

                break
        
                    
            else:
                print("Access Denied")
                attempt +=1
                print("attempts = ",attempt,"/5")
                print("Try Again...")
                if attempt>5:
                    print("Maximum Attempt Reached.....")
                    break        

    return employee


create_user()
@authentication
def say_name():
    print("Authenticating....")
    

    

say_name()
