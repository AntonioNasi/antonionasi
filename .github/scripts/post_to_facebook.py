import requests
import xml.etree.ElementTree as ET
import os

FEED_URL = "https://antonionasi.com.br/feed.xml"
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
PAGE_TOKEN = os.getenv("FACEBOOK_PAGE_TOKEN")
GRAPH_VERSION = "v18.0"

def get_latest_post():
    response = requests.get(FEED_URL)
    root = ET.fromstring(response.content)

    item = root.find(".//item")
    title = item.find("title").text
    link = item.find("link").text

    return title, link

def publish_post(title, link):
    url = f"https://graph.facebook.com/{GRAPH_VERSION}/{PAGE_ID}/feed"

    payload = {
        "message": f"{title}\n\nLeia mais:",
        "link": link,
        "access_token": PAGE_TOKEN
    }

    response = requests.post(url, data=payload)
    print(response.json())

if __name__ == "__main__":
    title, link = get_latest_post()
    publish_post(title, link)
