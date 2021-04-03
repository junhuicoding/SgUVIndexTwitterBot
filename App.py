from Services.MessageGenerator import generateUVTweetNow
from Services.Twitter import auth
import schedule
import time

auth()
schedule.every().hours.at(":05").do(generateUVTweetNow)

while 1:
    print("Wake up to check scheduler")
    schedule.run_pending()
    time.sleep(1800)
