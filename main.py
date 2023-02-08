import datetime

def special_day_delta(date):
    current_year = datetime.datetime.now().year
    special_days = [("Lunar New Year", datetime.datetime(current_year, 1, 22)),
                    ("Valentine's Day", datetime.datetime(current_year, 2, 14)),
                    ("Pi Day", datetime.datetime(current_year, 3, 14)),
                    ("April Fools' Day", datetime.datetime(current_year, 4, 1)),
                    ("World Turtle Day", datetime.datetime(current_year, 5, 23)),
                    ("Summer Solstice", datetime.datetime(current_year, 6, 21)),
                    ("Independence Day", datetime.datetime(current_year, 7, 4)),
                    ("US Coast Guard Day", datetime.datetime(current_year, 8, 4)),
                    ("World Ozone Day", datetime.datetime(current_year, 9, 16)),
                    ("Int'l Day of Older Persons", datetime.datetime(current_year, 10, 1)),
                    ("National Butter Day", datetime.datetime(current_year, 11, 17)),
                    ("Christmas", datetime.datetime(current_year, 12, 25))]
    
    delta = None
    nearest_special_day = None
    for special_day in special_days:
        new_delta = abs(special_day[1].date() - date.date())
        if not delta or new_delta < delta:
            delta = new_delta
            nearest_special_day = special_day[0]
    return nearest_special_day, delta.days

input_date = input("Enter the date in the following format: YYYY.MM.DD: ")
date = datetime.datetime.strptime(input_date, '%Y.%m.%d')
nearest_special_day, delta = special_day_delta(date)

print(f'{abs(delta)} day(s) {"after" if delta > 0 else "before"} {nearest_special_day}')
