import db_connect
def get_salt():
    mydb = db_connect.get_connection()
    salt = ''
    mycursor = mydb.cursor()
    mycursor.execute("SELECT enc_salt FROM salts ORDER BY RAND() LIMIT 1")
    myresult = mycursor.fetchall()
    for x in myresult:
        for y in x:
            salt = str(y)
    return salt