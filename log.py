import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("reddit_client_id"),
    client_secret=os.getenv("reddit_client_secret"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_password"),
    user_agent="test_script by /u/your_reddit_username",
)

# Test fetching your account details
print(f"Logged in as: {reddit.user.me()}")
