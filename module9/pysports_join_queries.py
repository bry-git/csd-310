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
    sql = "SELECT player_id, first_name, last_name, team_name " \
          "FROM player " \
          "INNER JOIN team ON player.team_id = team.team_id;"

    cursor.execute(sql)
    players = cursor.fetchall()
    print(f"\n -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password doesn't exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
