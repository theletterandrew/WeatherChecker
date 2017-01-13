# UserWeather.py

# Creates an instance of a User with the required information (Name, number, locations, minimum-temperature)
# Calls the method notifyUser(), which sends the user a text if it will rain (>20% chance) or will be cold (<minimum-tepmerature)
# in any of their listed locations.

# This is best implemented by using Windows Task Scheduler (or similar for your OS) to run this script at whatever time you'd like to be
# notified. This allows you to have different users be notified at different times.

import weatherV2

Me = weatherV2.User('Me', '**YOUR-NUMBER**', ['**LIST-OF-YOUR-PROXIMAL-CITIES**'], 60)
Me.notifyUser()