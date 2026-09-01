def format_date(date: str):
    year_value = date[6:]
    month_value = date[0:2]
    day_value = date[3:5]

    new_date = year_value + month_value + day_value

    return new_date


def sort_dates(dates: list[str]) -> list[str]:
    dates.sort()
    return dates

testinput = "08-12-2002"

print(format_date(testinput))