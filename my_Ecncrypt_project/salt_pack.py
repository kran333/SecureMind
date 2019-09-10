import mysql.connector
def get_salt():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="encrypt_data_pro",
        auth_plugin='mysql_native_password'
    )
    salt = ''
    mycursor = mydb.cursor()
    mycursor.execute("SELECT enc_salt FROM salts ORDER BY RAND() LIMIT 1")
    myresult = mycursor.fetchall()
    for x in myresult:
        for y in x:
            salt = str(y)
    return salt