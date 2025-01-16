# AI-generated-content-to-Reddit-daily
a bot that posts AI-generated content to Reddit daily Use Groq API to generate engaging content Implement a basic scheduling system for automated posts


# Reddit AI Bot

This bot uses **Groq AI** to generate and post engaging content automatically to Reddit. It is designed to handle daily automated posting with minimal setup.

---

## Features
- AI-generated content using **Groq AI**.
- **Scheduled daily posting** to Reddit at user-specified times.
- Basic **error handling** and **logging** for better debugging.
- Extensible design for future enhancements like comment generation.

---

## Requirements
- Python 3.8 or higher
- Reddit account with script app credentials
- Groq API key


## Most IMP thing in this Project
## Create .env file and add this code

reddit_client_id=your_reddit_client_id <br>
reddit_client_secret=your_reddit_client_secret <br>
reddit_username=your_reddit_username <br>
reddit_password=your_reddit_password <br>
groq_api_key=your_groq_api_key <br>

to credeate reddit clint id visit -> https://www.reddit.com/prefs/apps <br>
Fill out the details: <br>
Name: Your bot's name. <br>
App Type: Choose "Script" (important!). <br>
Description: Optional, but you can describe your app.<br>
About URL: Optional. <br>
Redirect URI: Set this to http://localhost:8080 (or leave blank for script apps) <br>
<br>
and For Groq api visit -> https://console.groq.com/keys 
<br>
also attached a proof as Screentshot(94) so you can verfiy that!!!
