import mysql.connector
from mysql.connector import Error
import streamlit as st
mydb = mysql.connector.connect(
    host=st.secrets["mysql"]["host"],
    port=st.secrets["mysql"]["port"],
    user=st.secrets["mysql"]["user"],
    password=st.secrets["mysql"]["password"],
    database=st.secrets["mysql"]["database"]
)
mycursor = mydb.cursor()


# create
def create_db():
    mycursor = mydb.cursor()
    mycursor.execute("USE contacts_db")
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    id INT AUTO_INCREMENT PRIMARY KEY ,
    name VARCHAR(100), 
    phone VARCHAR(50) ,
    email_address VARCHAR(100)
    )
    """)
    
    mycursor.close()


 # insert 
def insert_data(val):
    mycursor = mydb.cursor()
    mycursor.execute("USE contacts_db")
    sql = "INSERT INTO contacts(name,phone,email_address) values(%s,%s,%s)"
    if type(val) == list:
        mycursor.executemany(sql,val)
    elif type(val) == tuple:
        mycursor.execute(sql,val)
    else:
        single_val = tuple(val.values())
        mycursor.execute(sql,single_val)
    mydb.commit()
    mycursor.close()

# select
def select_data():
    mycursor = mydb.cursor()
    mycursor.execute("USE contacts_db")
    mycursor.execute("SELECT * FROM contacts")
    myresult = mycursor.fetchall()
    return myresult
    



# update
def update_data(record_id,**kwargs):
    mycursor = mydb.cursor()
    mycursor.execute("USE contacts_db")
    values_list= []
    columns_list = []
    for key,value in kwargs.items():
        columns_list.append(f"{key}= %s")
        values_list.append(value)
        
    dynamic_columns_string = ",".join(columns_list)
    sql = f"UPDATE contacts SET {dynamic_columns_string} WHERE id = %s "
    values_list.append(record_id)
    adr = tuple(values_list)
    mycursor.execute(sql,adr)
    mydb.commit()
    print(mycursor.rowcount,"record(s) affected")
    mycursor.close()

# delete
def delete_data(contact_id):
    mycursor = mydb.cursor()
    mycursor.execute("USE contacts_db")
    sql = "DELETE FROM contacts WHERE id = %s"
    mycursor.execute(sql,(contact_id,))
    mydb.commit()
    mycursor.close()