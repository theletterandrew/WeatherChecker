# WeatherChecker
A Python 3 program that will text you if it is going to rain or be cold today.

## Please Note:
This program will not run for you without some modifications as I have sanitized the files to exclude my personal information. If you'd like to use this program yourself, I recommend the following changes-

* Populate the variables at the top of sendAText.py with your own Twilio credentials
* Within weatherV2.py, the string variable 'address' should be updated to include your own Weather Underground API key and your state.
* UserWeather.py should be changed so that it creates a User object containing your own information.

## How I Use This Program
First, I'd like to say that this program solves a very first-world problem. Even in the age of smart phones, I always forget to check the weather. To be frank though, I honestly don't care what the weather forecast says unless it means I have to bring a jacket or an umbrella that day. This program solves this problem by only notifying me when it matters.

Within Windows Task Scheduler, I add a new task set to run at 8:30 AM everyday. The task runs AndrewWeather.py which then will notify me if there's more than a 20% chance of rain or a forecasted low temperature lower than 60F.

The advantage of having a seperate file (UserWeather.py) to create an instance of the User class is that this allows for different users to be alerted at different times by scheduling a task for each user.

## Future Plans?
* Maybe in the future, I'll turn this into an Android/iPhone app that will use pop up alerts (Is that what they're called?) instead of a text message system.
* I'd like to include more weather APIs and perhaps even produce some sort of average to go off of.
