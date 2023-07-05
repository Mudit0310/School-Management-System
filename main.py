from flask import Flask, render_template, request
import mysql.connector
from threading import Thread
from tkinter import *
from tkinter import messagebox

app = Flask(__name__)

@app.route('/')
def index():
    return form_html

@app.route('/submit/class', methods=['POST'])
def submit_class():
    CLASS = request.form['class']
    SECTION = request.form['section']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO CLASS_MSTR (CLASS, SECTION) VALUES (%s, %s)"
        values = (CLASS, SECTION.upper())
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/teacher', methods=['POST'])
def submit_teacher():
    FIRST_NAME = request.form['F_Name']
    LAST_NAME = request.form['L_Name']
    GENDER = request.form['Gender']
    JOIN_DATE = request.form['Join_date']
    SUBJECT1 = request.form['Sub1']
    SUBJECT2 = request.form['Sub2']
    EMAIL_ID = request.form['email']
    PHONE_NUMBER = request.form['Phone_no']
    CITY = request.form['City']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO TEACHER_MSTR(FIRST_NAME, LAST_NAME, GENDER, JOIN_DATE, SUBJECT1, SUBJECT2, EMAIL_ID, PHONE_NUMBER, CITY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (FIRST_NAME, LAST_NAME, GENDER, JOIN_DATE, SUBJECT1, SUBJECT2, EMAIL_ID, PHONE_NUMBER, CITY)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/student', methods=['POST'])
def submit_student():
    ADMISSION_DATE = request.form['A_date']
    FIRST_NAME = request.form['F_Name']
    LAST_NAME = request.form['L_Name']
    DATE_OF_BIRTH = request.form['dob']
    GENDER = request.form['Gender']
    STUDENT_MOBILE_NUMBER = request.form['S_Mobile']
    FATHER_NAME = request.form['Father_Name']
    FATHER_MOBILE_NUMBER = request.form['F_Mobile']
    MOTHER_NAME = request.form['Mother_Name']
    MOTHER_MOBILE_NUMBER = request.form['M_Mobile']
    CITY = request.form['S_City']
    AADHAR_NUMBER = request.form['Aadhar_No']
    ALUMINI = request.form['Alumini']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database      
        query = "INSERT INTO STUDENT_MSTR(ADMISSION_DATE, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, GENDER, STUDENT_MOBILE_NUMBER, FATHER_NAME, FATHER_MOBILE_NUMBER, MOTHER_NAME, MOTHER_MOBILE_NUMBER, CITY, AADHAR_NUMBER, ALUMINI) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ADMISSION_DATE, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, GENDER, STUDENT_MOBILE_NUMBER, FATHER_NAME, FATHER_MOBILE_NUMBER, MOTHER_NAME, MOTHER_MOBILE_NUMBER, CITY, AADHAR_NUMBER, ALUMINI)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/class-teacher', methods=['POST'])
def submiT_class_teacher():
    TEACHER_ID = request.form['teacher_ID']
    CLASS_CODE = request.form['class_code']
    SUBJECT = request.form['Subject']
    START_DATE = request.form['Start_date']
    END_DATE = request.form['End_date']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO CLASS_TEACHER_MSTR (TEACHER_ID, CLASS_CODE, SUBJECT_NAME, START_DATE, END_DATE) VALUES (%s, %s, %s, %s, %s)"
        values = (TEACHER_ID, CLASS_CODE, SUBJECT, START_DATE, END_DATE)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/class_dtls', methods=['POST'])
def submit_class_dtls():
    CLASS = request.form['class']
    SECTION = request.form['section']
    CLASS_TEACHER = request.form['class_teacher']
    STUDENT_COUNT = request.form['Student_count']
    VALID_INVALID = request.form['Valid_Invalid']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO CLASS_DTLS (CLASS, SECTION, CLASS_TEACHER, STUDENT_COUNT, VALID_INVALID) VALUES (%s, %s, %s, %s, %s)"
        values = (CLASS, SECTION.upper(), CLASS_TEACHER, STUDENT_COUNT, VALID_INVALID)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'

@app.route('/submit/teacher_att', methods=['POST'])
def submit_teacher_att():
    TEACHER_CODE = request.form['Teacher_code']
    DATE_ = request.form['date']
    AVAILABLE = request.form['Available']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO TEACHER_ATTENDANCE (TEACHER_CODE, DATE_, AVAILABLE) VALUES (%s, %s, %s)"
        values = (TEACHER_CODE, DATE_, AVAILABLE.UPPER())
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/teacher_leave_dtls', methods=['POST'])
def submit_teacher_leave_dtls():
    TEACHER_CODE = request.form['teacher_code']
    START_DATE = request.form['Start_date']
    END_DATE = request.form['End_date']
    REASON = request.form['Reason']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO TEACHER_LEAVE_DTLS (TEACHER_CODE, START_DATE, END_DATE, REASON) VALUES (%s, %s, %s, %s)"
        values = (TEACHER_CODE, START_DATE, END_DATE, REASON)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/Student_att', methods=['POST'])
def submit_student_att():
    REGISTRATION_NUMBER = request.form['Registration_number']
    DATE_ = request.form['date']
    AVAILABLE = request.form['Available']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO STUDENT_ATTENDANCE (REGISTRATION_NUMBER, DATE_, AVAILABLE) VALUES (%s, %s, %s)"
        values = (REGISTRATION_NUMBER, DATE_, AVAILABLE.upper())
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
@app.route('/submit/student_leave_dtls', methods=['POST'])
def submit_student_leave_dtls():
    REGISTRATION_NUMBER = request.form['Registration_number']
    START_DATE = request.form['Start_date']
    END_DATE = request.form['End_date']
    REASON = request.form['Reason']
    
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mudit0310',
            database='smsdb'
        )
        cursor = connection.cursor()

        # Save the data to the database
        query = "INSERT INTO STUDENT_LEAVE_DTLS (REGISTRATION_NUMBER, START_DATE, END_DATE, REASON) VALUES (%s, %s, %s, %s)"
        values = (REGISTRATION_NUMBER, START_DATE, END_DATE, REASON)
        cursor.execute(query, values)
        connection.commit()

        return 'Data submitted successfully'
    except mysql.connector.Error as error:
        return f'Error occurred: {error}'
    
if __name__ == '__main__':
    app.run()
