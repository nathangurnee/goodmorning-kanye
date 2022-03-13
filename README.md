# goodmorning-kanye
 Randomly selects from a collection of memorable quotes from Kanye West, and with the help of the `smtplib` Python standard library, sends them to a cell phone using SMS messaging and an email client.
 
 Has the ability to be automated using an OS job scheduler. In this case, I used cron for Unix-based systems. Enter the following in your crontab file to be sent a brand new quote every morning at 10am:
 ```
 0 10 * * * /path_to_script.py
 ```