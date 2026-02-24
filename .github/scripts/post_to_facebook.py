import requests
import xml.etree.ElementTree as ET

FEED_URL = "https://antonionasi.com.br/feed.xml"

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
