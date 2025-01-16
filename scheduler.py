import schedule
import time
from bot import post_to_reddit

def job():
    print("Executing job...")
    post_to_reddit()

# Test for the next minute or two
schedule.every().day.at("13:59").do(job)

print("Scheduler running...")

while True:
    schedule.run_pending()
    print("Waiting for the next scheduled job...")
    time.sleep(3)  # Check every minute
