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
    cursor = db.cursor()
    sql = "SELECT * FROM team"
    cursor.execute(sql)

    teams = cursor.fetchall()
    print(f"\n-- DIPLAYING TEAMS --")
    for team in teams:
        print(f"Team ID: {team[0]}")
        print(f"Team Name: {team[1]}")
        print(f"Team Mascot: {team[2]}\n")

    cursor = db.cursor()
    sql = "SELECT * FROM player"
    cursor.execute(sql)

    players = cursor.fetchall()
    print(f"\n-- DISPLATING PLAYERS --")
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team: {player[3]}\n")

    input("press any key to contiue")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password doesn't exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()