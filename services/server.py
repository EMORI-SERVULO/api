import requests
from datetime import datetime
from dateutil import relativedelta
import os
import random
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                                user='root',
                                password='admin',
                                database='mydb',
                                cursorclass=pymysql.cursors.DictCursor)

class services():
  
    def create_solicitud(self,nombre,
        apellido,
        identificacion,
        edad,
        afinidad):
        estatus = 'Aceptada'
        grim= {'Sinceridad' :'Trébol de 1 hoja',
                    'Esperanza' : 'Trébol de 2 hojas',
                    'Amor':'Trébol de 3 hojas',
                    'Buena Fortuna' : 'Trébol de 4 hojas',
                    'Desesperación':'Trébol de 5 hojas'}
        grimorio = random.choice(list(grim.values()))
        with connection.cursor() as cursor:
            # Create a new record
            try:          
                sql = "INSERT INTO scholmagia (nombre, apellido, identificacion, edad, afinidad, estatus, grimorio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (nombre,apellido,identificacion,edad,afinidad,estatus, grimorio))
            except:
                print("An exception occurred") 

        connection.commit()

       
        
        return {"message":"creacion exitosa"}

    def get_solicitud(self):
           
            with connection.cursor() as cursor:
                # Create a new record
                try:          
                    cursor.execute('SELECT * FROM scholmagia')
                    rows = cursor.fetchall()    
                except:
                    print("An exception occurred") 

            connection.commit()
            return rows
    
    def get_grimorios(self, id):
           
            with connection.cursor() as cursor:
                # Create a new record
                try:          
                    cursor.execute('SELECT * FROM scholmagia WHERE id=%s', id) 
        
                    todo  = cursor.fetchone()
                    
                except:
                    print("An exception occurred") 

            connection.commit()
            return todo
    def borrar(self, id):
           
            with connection.cursor() as cursor:
                # Create a new record
                try:          
                    cursor.execute('DELETE FROM scholmagia WHERE id=%s', id) 
        
                    cursor.fetchone()
                    
                except:
                    print("An exception occurred") 

            connection.commit()
            return {"msg":"borrado exitoso"}
    
    def updateSolicitud(self, id,nombre,
        apellido,
        identificacion,
        edad,
        afinidad):
       
            with connection.cursor() as cursor:
                # Create a new record
                try:          
                    cursor.execute(('''UPDATE scholmagia SET nombre=('{0}'),apellido=('{1}'),identificacion=('{2}'),edad=('{3}'),afinidad=('{4}')
                                     WHERE id=('{5}')'''.format(nombre,apellido,identificacion,edad,afinidad,id)))
                                     
                except:
                    print("An exception occurred") 

            connection.commit()
            connection.close()
            return {"msg":"actualizado exitoso"}
    
    def updatestatus(self,id,estatus):
       
            with connection.cursor() as cursor:
                # Create a new record
                try:          
                    cursor.execute(('''UPDATE scholmagia SET estatus=('{0}')
                                     WHERE id=('{1}')'''.format(estatus,id)))
                                     
                except:
                    print("An exception occurred") 

            connection.commit()
            connection.close()
            return {"msg":"actualizado exitoso"}   
