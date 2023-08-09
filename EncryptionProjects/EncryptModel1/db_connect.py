import mysql.connector
def get_connection():
    con_obj =  mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="encrypt_data_pro",
        auth_plugin='mysql_native_password'
    )
    return con_obj