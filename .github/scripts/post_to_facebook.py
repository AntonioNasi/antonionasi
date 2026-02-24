print("VERSÃO CORRETA ATIVA")

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

    namespace = {'atom': 'http://www.w3.org/2005/Atom'}

    entry = root.find('atom:entry', namespace)

    if entry is None:
        raise Exception("Nenhum post encontrado no feed.")

    title = entry.find('atom:title', namespace).text
    link = entry.find('atom:link', namespace).attrib['href']

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