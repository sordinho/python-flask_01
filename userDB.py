# Created by Davide Sordi in 16/04/2018 at 23.02

import pymysql


def check_user(username):
    """
    Function to check if a user is in the DB
    :param username: username given by the user from login form
    :return: none if wrong user or all user data
    """
    query = "SELECT id,username,password,fullname FROM users WHERE username=%s"

    connection = pymysql.connect(user="root", password="sysadmin", database="wakekill", host="localhost")
    cursor = connection.cursor()
    cursor.execute(query, (username,))

    result = cursor.fetchone()  # faccio il fetch solo del primo elemento perche sono sicuro che lo username sia unico nel DB

    cursor.close()
    connection.close()

    return result

def get_alarms(user_id):
    query = "SELECT id,hour FROM alarms WHERE user_id=%s"

    connection = pymysql.connect(user="root", password="sysadmin", database="wakekill", host="localhost")
    cursor = connection.cursor()
    cursor.execute(query, (user_id,))

    alarms = cursor.fetchall()  # faccio il fetch

    cursor.close()
    connection.close()

    return alarms


if __name__ == "__main__":
    print(check_user("davide"))
    print(check_user("miki"))
    print(check_user("fulvio"))
    print(get_alarms(1))
