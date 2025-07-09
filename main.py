import os
import time
import json
import random
import requests
from PIL import Image, ImageDraw, ImageFont

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

HEADERS = {'User-agent': config["reddit_user_agent"]}

def get_reddit_post():
    url = f'https://www.reddit.com/r/{config["subreddit"]}/top.json?limit=20&t=day'
    response = requests.get(url, headers=HEADERS)
    posts = response.json()["data"]["children"]
    chosen = random.choice(posts)
    return chosen["data"]["title"], chosen["data"]["permalink"]

def create_carousel(text):
    width, height = 1080, 1080
    image = Image.new("RGB", (width, height), color=(30, 30, 30))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 48)
    draw.text((100, height//2), text, fill="white", font=font)

    filename = "carousel1.jpg"
    image.save(filename)
    return filename

def post_to_instagram(image_path):
    print(f"Posting {image_path} to Instagram...")
    # Placeholder for real Instagram API call
    time.sleep(2)
    print("Posted successfully!")

if __name__ == "__main__":
    print("Fetching Reddit post...")
    title, link = get_reddit_post()
    print("Creating carousel...")
    image_file = create_carousel(title)
    print("Uploading to Instagram...")
    post_to_instagram(image_file)
