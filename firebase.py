from flask import Flask, request, render_template, current_app
import os
from flask import Flask, flash, request, redirect, render_template

import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename


from flask import redirect, abort
import firebase_admin
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import smtplib
import pandas as pd



firebaseConfig = {
    "apiKey": "AIzaSyB9DaUxj2YCDMrNTOSgxpF49e6B5lCgOMA",
    "authDomain": "datahub-21e7e.firebaseapp.com",
    "databaseURL": "https://datahub-21e7e-default-rtdb.firebaseio.com",
    "projectId": "datahub-21e7e",
    "storageBucket": "datahub-21e7e.appspot.com",
    "messagingSenderId": "166143497203",
    "appId": "1:166143497203:web:4cf11ad5cfec0214ee7886",
    "measurementId": "G-6Z3W87LP23"
}
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

email = 'kAADEKOYA10'
email=email.title()

# result = db.collection('student').document(str(email)).get()
# if result.exists:
#     print(result.to_dict())

# docs = db.collection('student').where("UserID", "==", str(email)).get()
# for doc in docs:
#     print(doc.to_dict())


id = email
doc_ref = db.collection('student').document(str(id))
docs = doc_ref.collection(str('2002')).get()
docs = doc_ref.collection(str('2002')).document('Full-Time Information').get()
print(docs.to_dict())
info_doc = docs.to_dict()
# year = info_doc['Internship Year']
# company_name = info_doc['Company Name']
# pay = info_doc['Hourly Pay']
# position = info_doc['Position']
print(info_doc)
if info_doc:
    print("Dictionary is not empty!")
else:
    print("Dictionary is empty!")
# if len(info_doc) ==0 :
#     print("Dictionary is not empty!")
# else:
#     print("Dictionary is empty!")

# companyname = info_doc['Company Name']
# print(companyname)
#
# salary = info_doc['Salary']
# print(salary)
#
# email = info_doc['Personal Email']
# print(email)

# doc_ref = db.collection('student').document(str(id))
# fall_info = doc_ref.collection(str(2002)).document('Fall Internship Information').get()
# fall_info = doc_ref.collection(str(2022)).get()

# stuff = fall_info.to_dict()
#
# if stuff:
#     print("Dictionary is not empty!")
# else:
#     print("Dictionary is empty!")

# # print(stuff)
# doc_ref = db.collection('student').document(str(id))
# fall_info = doc_ref.collection(str(2002)).document('Fall Internship Information').get()
# print(fall_info.to_dict())

# fall_info = doc_ref.collection(str(2022)).document('Full-Time Information').get()

# stuff = fall_info.to_dict()
# print(stuff)


# # stuff = stuff.values()
# stuff = list(stuff)
# print(stuff)
# for i in docs:
#     li.append(i)
# print(li)
# print(list(docs.to_dict()))
#
# Company_name = stuff[1]
# print(Company_name)


# print(Company_name)
# for doc in docs:
#     print(doc.to_dict())

# def studentsignup():
#     userid = 'student id: '
#     email = 'kaadekoya10@my.fisk.edu'
#     email = email.lower()
#     studentsignup.email = email.title()
#
#     print(email)
#     if 'My.Fisk.Edu' in studentsignup.email :
#         print("yes")
#     else:
#         print("no")
#         # for i in email:
#         #     if i != '@':
#         #         userid = userid + i
#         #     elif i == '@':
#         #         break
#     # print(userid)
#
# def function_2():
#     print(studentsignup.email)
#
#
# studentsignup()
# function_2()
# email = 'kaadekoya10@fisk.edu'
# reg_email = 'kennyadekoya02@Yahoo.com'
#
# verification = ''
# fisk = 'fisk.edu'
# email = email.lower()
# email = email.title()
# userid = ''
# if fisk in email:
#     for i in email:
#         if i != '@':
#             userid = userid + i
#         elif i == '@':
#             break
# print(userid)
#
# # else:
# #         print("Invalid email: not a fisk university email")
# print(email)
# # print(userid)

# @app.route('/')
#
# # @app.route('/', methods = ['GET', 'POST'])
# def index():
#     return render_template('index.html')
#
# @app.route('/data', methods = ['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         file = request.form['upload-file']
#         data = pd.read_excel(file)
#         return render_template('data.html', data=data.to_html())
#
# if __name__ =='__main__':
#     app.run(debug=True)
    #
# data = webUrl.read()
# print (data)

#
# firebaseConfig = {
#     "apiKey": "AIzaSyB9DaUxj2YCDMrNTOSgxpF49e6B5lCgOMA",
#     "authDomain": "datahub-21e7e.firebaseapp.com",
#     "databaseURL": "https://datahub-21e7e-default-rtdb.firebaseio.com",
#     "projectId": "datahub-21e7e",
#     "storageBucket": "datahub-21e7e.appspot.com",
#     "messagingSenderId": "166143497203",
#     "appId": "1:166143497203:web:4cf11ad5cfec0214ee7886",
#     "measurementId": "G-6Z3W87LP23"
# }
#
# #
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# #
# #
# #
# # # #creating a new sign up
# # # email = input("Please enter your email address: \n")
# # # email = email.lower()
# # # # password = input("Please enter your password: \n")
# # # #
# # # # id = ''
# # # # for i in email:
# # # #     if i != '@':
# # # #         id = id+i
# # # #     elif i=='@':
# # # #         break
# # # # # print(id)
# # # # cred = credentials.Certificate('firebase-sdk.json')
# # # # firebase_admin.initialize_app(cred)
# # # #
# # # # user = auth.create_user(uid=id, email=email, password =password)
# # # # print("you did it part 1")
# # # # #
# # # # #
# # # firebase = pyrebase.initialize_app(firebaseConfig)
# # # auth = firebase.auth()
# # # #
# # # email = "KAAdekoya10@my.fisk.edu"
# # # email = email.lower()
# # # # print(email)
# # # password = "Ayomipo02"
# # # login = auth.sign_in_with_email_and_password(email, password)
# # #
# # # cred = credentials.Certificate('firebase-sdk.json')
# # # firebase_admin.initialize_app(cred)
# #
# # # print(userid)
# # #
# # # result = db.collection('student').document(str(userid)).get()
# # # result = result.to_dict()
# # # # print(result)
# # # # doc_ref.set({
# # # #         'UserID': str(id),
# # # #         'First Name': str(first_name),
# # # #         'Last Name': str(last_name)
# # # #         'Email': str(email),
# # # #         'Student Number': str(student_number),
# # # #         'Major': str(major)
# # # # })
# # # name = result.get("First Name")
# # # lastname = result.get("Last Name")
# # # email = result.get("Email")
# # # number = result.get("Student Number")
# # # major = result.get("Major")
# #
# #
# cred = credentials.Certificate('firebase-sdk.json')
# firebase_admin.initialize_app(cred)
#
# email = "KAAdekoya10@my.fisk.edu"
# email = email.lower()
# email = email.title()
# # print(email)
# password = "Ayomipo02"
#
#
# def firstFunction():
#     global var
#     var = ''
#
#
#
# firstFunction()
#
#
# def gym():
#     var = 'ehdasjnk'
#     print(var)
#
# gym()
#
#
# # # result.set({
# # #         'hello': 'YESSSIR'
# # # })
# #
# #
# # # print(name)
# #
# # # if result.exists:
# # #     print(result.to_dict())
# # #     if
# #     # print(result('First Name'))
# #
# # # docs = db.collection('student').where('Email', "==", email).get()
# # # for doc in docs:
# # #     print(doc.to_dict())
# #
# # # print(docs)
# # # #
# # # # # #creating a new sign up
# # # # email = input("Please enter your email address: \n")
# # # # password = input("Please enter your password: \n")
# # # # name= input("Please enter your first name: \n")
# # # # lname= input("Please enter your last name: \n")
# # # # id = ''
# # # # for i in email:
# # # #     if i != '@':
# # # #         id = id+i
# # # #     elif i=='@':
# # # #         break
# # # # # print(id)
# # # # user = auth.create_user(uid=id, email=email, password =password)
# # # # # print("you did it part 1")
# # # #
# # # # db = firestore.client()
# # # #
# # # # doc_ref = db.collection('student').document(str(id))
# # # #
# # # # doc_ref.set({
# # # #     'UserID': str(id),
# # # #     'name': str(name),
# # # #     'lname': str(lname),
# # # #     'email': str(email)
# # # # })
# # #
# # # firebaseConfig = {
# # #     "apiKey": "AIzaSyB9DaUxj2YCDMrNTOSgxpF49e6B5lCgOMA",
# # #     "authDomain": "datahub-21e7e.firebaseapp.com",
# # #     "databaseURL": "https://datahub-21e7e-default-rtdb.firebaseio.com",
# # #     "projectId": "datahub-21e7e",
# # #     "storageBucket": "datahub-21e7e.appspot.com",
# # #     "messagingSenderId": "166143497203",
# # #     "appId": "1:166143497203:web:4cf11ad5cfec0214ee7886",
# # #     "measurementId": "G-6Z3W87LP23"
# # # }
# # #
# # #
# # # #auth!!!!
# # #
# # #
# # # firebase = pyrebase.initialize_app(firebaseConfig)
# # # auth = firebase.auth()
# # # #
# # # # cred = credentials.Certificate('firebase-sdk.json')
# # # # firebase_admin.initialize_app(cred)
# # #
# # # # #creating a new sign up
# # # # email = input("Please enter your email address: \n")
# # # # password = input("Please enter your password: \n")
# # # #
# # # # id = ''
# # # # for i in email:
# # # #     if i != '@':
# # # #         id = id+i
# # # #     elif i=='@':
# # # #         break
# # # # # print(id)
# # # # user = auth.create_user(uid=id, email=email, password =password)
# # # # print("you did it part 1")
# # # # #
# # #
# # # # # password reset
# # # # email = 'kennyadekoya02@yahoo.com'
# # # # link = auth.generate_password_reset_link(email, action_code_settings=None)
# # # # print(link)
# # # # print("you did it part 2")
# # #
# # #
# # # #
# # # #sign in
# # # email = "kaadekoya10@my.fisk.edu"
# # # password = "Ayomipo02"
# # # login = auth.sign_in_with_email_and_password(email, password)
# # # db = firestore.client()
# # #
# # # doc_ref = db.collection('student').document(str(id))
# # #
# # # docs = db.collection('student').where("Email", "==", str(email)).get()
# # #
# # # print(docs)
# # # first_name = docs
# # # print("you did it part 3")
# # #
# # # #
# # # # # generate email authentication
# # # # email = input("Please enter your email address: \n")
# # # # link = auth.generate_email_verification_link(email)
# # # # print(link)
# # # # print("you did it part 4")
# # # #
# # # #
# # # # #valiidation
# # # # print("you did it bro: {0}".format(user.uid))
# # # # print("IT WORKS BRO")
# # # from flask import Flask, request, render_template
# # # from flask import redirect, abort
# # #
# # # app = Flask(__name__)
# # #
# # # # creating a homepage for the dashboard
# # # @app.route('/')
# # # def homepage():
# # #     return render_template("studentpage.html")#returns/runs the code from the html file
# # #
# # #
# # # @app.route('/result', methods=['POST', 'GET'])
# # # def result():
# # #     output = request.form.to_dict()
# # #     print(output)
# # #     firstname = output["NAME"]
# # #
# # #     return render_template('studentpage.html', name=name)
