import os
import praw
from groq import Groq
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("reddit_client_id"),
    client_secret=os.getenv("reddit_client_secret"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_password"),
    user_agent="reddit_bot"
)
groq_api_key = os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)

# Configure logging
logging.basicConfig(filename="bot.log", level=logging.INFO)

def generate_content(prompt):
    """Generates content using Groq AI."""
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="Llama3-8b-8192",
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        return "Error generating content."

def post_to_reddit():
    """Posts AI-generated content to Reddit."""
    try:
        subreddit = reddit.subreddit("test")  # Replace 'test' with your subreddit
        title = "Daily AI-Generated Post"
        content = generate_content("Write an engaging Reddit post about AI.")
        subreddit.submit(title=title, selftext=content)
        logging.info("Post successful!")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")
