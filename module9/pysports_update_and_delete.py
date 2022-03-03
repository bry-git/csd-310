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
db = mysql.connector.connect(**config)


def display_players(collection):
    for item in collection:
        print(f"Player ID: {item[0]}")
        print(f"First Name: {item[1]}")
        print(f"Last Name: {item[2]}")
        print(f"Team Name: {item[3]}\n")


def error_handler(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password doesn't exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)


try:  # insert a record into player table
    sql = "INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1);"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    sql = "SELECT player_id, first_name, last_name, team_name " \
          "FROM player " \
          "INNER JOIN team ON player.team_id = team.team_id;"
    cursor.execute(sql)
    players = cursor.fetchall()

    print(f"\n -- DISPLAYING PLAYERS AFTER INSERT --")
    display_players(players)
    input("press any key to continue")

    # update a record
    sql = "UPDATE player " \
          "SET team_id = 2," \
          "first_name = 'Gollum'," \
          "last_name = 'Ring Stealer' " \
          "WHERE first_name = 'Smeagol'"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    sql = "SELECT player_id, first_name, last_name, team_name " \
          "FROM player " \
          "INNER JOIN team ON player.team_id = team.team_id;"
    cursor.execute(sql)
    players = cursor.fetchall()

    print(f"\n -- DISPLAYING PLAYERS AFTER UPDATE --")
    display_players(players)

    input("press any key to continue")

    # delete a record
    sql = "DELETE FROM player WHERE first_name = 'Smeagol'"

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    sql = "SELECT player_id, first_name, last_name, team_name " \
          "FROM player " \
          "INNER JOIN team ON player.team_id = team.team_id;"

    cursor.execute(sql)
    players = cursor.fetchall()

    print(f"\n -- DISPLAYING PLAYERS AFTER DELETE --")
    display_players(players)

    input("press any key to continue")

except mysql.connector.Error as err:
    error_handler(err)

finally:
    db.close()

