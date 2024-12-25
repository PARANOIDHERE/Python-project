from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Russian_Russia')

def get_weekday(birthdate):

    date_object = datetime.strptime(birthdate, "%d.%m.%Y")
    weekday = date_object.strftime("%A")
    return weekday

def get_birthdate():
    while True:
        try:
            day = int(input("Введите день рождения (1-31): "))
            month = int(input("Введите месяц рождения (1-12): "))
            year = int(input("Введите год рождения (например, 1990): "))

            if 1 <= day <= 31 and 1 <= month <= 12:
                birthdate = f"{day}.{month:02}.{year}"
                return birthdate
            else:
                print("Некорректный ввод данных. Попробуйте ещё раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте ещё раз.")

def is_leap_year(year):
    birthdate_obj = datetime.strptime(birthdate, "%d.%m.%Y")
    if (birthdate_obj.year % 4 == 0 and birthdate_obj.year % 100 != 0) or (birthdate_obj.year % 400 == 0):
        return True
    return False

def calculate_age(birthdate):
    today = datetime.now()
    birthdate_obj = datetime.strptime(birthdate, "%d.%m.%Y")
    age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))
    return age

digits = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    '2': [
        " *** ",
        "*   *",
        "   * ",
        "  *  ",
        "*****"
    ],
    '3': [
        " *** ",
        "*   *",
        "   **",
        "*   *",
        " *** "
    ],
    '4': [
        "   * ",
        "  ** ",
        " * * ",
        "*****",
        "   * "
    ],
    '5': [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "**** "
    ],
    '6': [
        " *** ",
        "*    ",
        "**** ",
        "*   *",
        " *** "
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   "
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        " ****",
        "    *",
        " *** "
    ],
    '.': [
        "     ",
        "     ",
        "     ",
        "     ",
        "  *  "
    ]
}

def print_number(number):
    for row in range(5): 
        line = ""
        for digit in str(number):
            if digit in digits:
                line += digits[digit][row] + "  " 
        print(line)

birthdate = get_birthdate()
print_number(birthdate)
weekday = get_weekday(birthdate)
print(f"День недели вашего дня рождения: {weekday}")
age = calculate_age(birthdate)
print(f"Ваш возраст:{age}")
birthdate_obj = datetime.strptime(birthdate, "%d.%m.%Y")
if is_leap_year(birthdate_obj.year):
    print(f"{birthdate_obj.year} - это високосный год.")
else:
    print(f"{birthdate_obj.year} - это не високосный год.")

