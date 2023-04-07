# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

available_zones = {'1': "Africa/Algiers",
                   '2': "Africa/Bujumbura",
                   '3': "Africa/Blantyre",
                   '4': "America/New_York",
                   '5': "America/Montserrat",
                   '6': "Asia/Oral",
                   '7': "Asia/Pyongyang",
                   '8': "Australia/NSW",
                   '9': "Australia/Sydney",
                   }

print(f"Please choose a time zone (or 0 to quit):")

for place in available_zones:
    print("\t{}, {}".format(place, available_zones[place]))

while True:
    choose_timezone = input()

    if choose_timezone == '0':
        break

    if choose_timezone in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choose_timezone])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choose_timezone], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time in {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("The UTC time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print()




