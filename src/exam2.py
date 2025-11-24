import datetime

"""Current time"""
print(datetime.datetime.now())

def calculate_age(birthdate):
    """This function calculates the age of a person given its birthdate."""
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
my_birthdate = datetime.date(2006, 4, 14)
my_age = calculate_age(my_birthdate)
print(f"I am {my_age} years old.")


"""This calculates the time until christmas!"""
xmas_2025 = datetime.datetime(2025, 12, 25, 0, 0, 0)
now = datetime.datetime.now()
time_left = xmas_2025 - now

print(f"Time left until Christmas: {time_left}")

from pytz import timezone

"""This is code from a website called kdnuggets.com that calculates timezones I wanted to try out. """
nyc_tz = timezone('America/New_York')
nyc_time = datetime.datetime.now(nyc_tz)
print(f"New York Time: {nyc_time}")

london_tz = timezone('Europe/London')
london_time = nyc_time.astimezone(london_tz)
print(f"London Time: {london_time}")

