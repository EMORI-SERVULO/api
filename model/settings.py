from flask import Flask,render_template, request
import pymysql.cursors

def create_tables():

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='admin',
                                database='mydb',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            try:
                ssql = " CREATE TABLE IF NOT EXISTS scholmagia(id int auto_increment, nombre varchar(100), apellido varchar(50), identificacion varchar(50), edad int(11), afinidad varchar(50),estatus varchar(50), grimorio varchar(50), primary key (id));"
                
                cursor.execute(ssql)
                
                #sql = "INSERT INTO solicitud (email, password) VALUES (%s, %s)"
                #cursor.execute(sql, ('alain@gmail.com', 'very-secret'))
            except:
                print("An exception occurred") 

        connection.commit()

        