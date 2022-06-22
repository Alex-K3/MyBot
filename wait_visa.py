import requests
import sqlite3


def read_sqlite_table(name_city):
    try:
        sqlite_connection = sqlite3.connect('city_code.db')
        cursor = sqlite_connection.cursor()
        sqlite_select_query = cursor.execute('SELECT code from Data WHERE city=?', (name_city,)).fetchone()
        cursor.close()
        result = sqlite_select_query[0]
        return result

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def city(user_name_city):
    try:
        result = requests.get(f'https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid={read_sqlite_table(user_name_city)}&aid=VisaWaitTimesHomePage')
        result.raise_for_status()
        wait = result.text.strip().split(' Days,')
        return f""" 
Предполагаемое время ожидания собеседования на неиммиграционную визу в посольстве или консульстве США в город {user_name_city}:

Гостевая виза: {wait[0]} дней
Студенческая/гостевая виза по обмену: {wait[1]} дней
Все другие неиммиграционные визы: {wait[2]} дней
        """
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

# user_name_city = str(input("Введите посольство или консульство США: ")).title()
# url = f'https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid={read_sqlite_table(user_name_city)}&aid=VisaWaitTimesHomePage'


# if __name__ == "__main__":
#     city(url)
