import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread, Lock
from interface import database
import requests

class Crawler:
    def __init__(self, start_url, max_url, match_str, ignore, concurrency, max_depth):

        self.start_url = start_url
        self.max_url = max_url
        self.match_str = match_str
        self.ignore = ignore
        self.concurrency = concurrency
        self.max_depth = max_depth

    def fetch(self, start_url):
        try:
            response = requests.get(start_url, timeout=5)
            return response.text
        except Exception as e:
            print(f"[!] Error on fetching {start_url}:", e)

            return None

def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    urls = set()
    
    for a_tag in soup.find_all("a", href=True):
        url = urljoin(base_url, a_tag["href"])
        
        if urlparse(url).scheme in ["http", "https"]:
            urls.add(url)
    return urls

def filter_urls(urls, match_str="", ignore=[]):
    filtered = []

    for url in urls:
        if match_str and match_str not in url:
            continue
        if any(ign in url for ign in ignore):
            continue
        filter.append(url)

    return filtered

