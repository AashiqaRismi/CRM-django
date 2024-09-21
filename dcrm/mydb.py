import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='altoris',
)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE AashiqaRismi")
print("all done")