import requests
from bs4 import BeautifulSoup

class LinkTraverser():
    rootURL = None
    
    def __init__(self, rootURL):
        self.rootURL = rootURL
        try:
            page = requests.get(url)
            print("Valid URL. A Traverser object created.")
        except requests.exceptions.RequestException as err:
            print("Invalid URL. Cannot reach page.")
            raise err   # if not raising error here. An object with invalid URL will eventually cause exceptions later



    def get_href_list(self):
        page = requests.get(self.rootURL)
        soup = BeautifulSoup(page.content, 'html.parser')
        href_list = []
        for a in soup.find_all('a'):
            href = a.get("href")
            if href is None:
                continue
            if not ('.com' in href or '.vn' in href):           ## in case href is a subfolder in the webpage
                href = self.rootURL+href
            href_list.append(href)

        href_list = list(dict.fromkeys(href_list))              ## convert to a dict then convert back, to remove duplicates
        return href_list



##### MAIN #####

url = "https://fptshop.com.vn/"
# url = "https://tiki.vn/"        # no link found inside tiki ? why --> 403 forbidden error

travser = LinkTraverser(rootURL = url)

list = travser.get_href_list()

if list is not None:
    print("list of links in the page:\n", list)
