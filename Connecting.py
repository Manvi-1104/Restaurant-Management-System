

import mysql.connector as sql

mydb=sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="110104",
    auth_plugin='mysql_native_password',
    database="evergreen_restaurant")
print(mydb)
