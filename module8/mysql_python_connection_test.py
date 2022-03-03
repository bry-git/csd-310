import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "sqlpass",
    "host": "127.0.0.1",
    "database": "pysports",
    "auth_plugin": "mysql_native_password",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print(f"\n Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password doesn't exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
