import requests
from bs4 import BeautifulSoup

class LinkTraverser():
    rootURL: str
    max_hrefs: int                # default 200

    def __init__(self, rootURL: str, max_hrefs = 200):
        self.rootURL = rootURL.rstrip('/')
        if not self.isURLReachable(rootURL):
            err = requests.exceptions.RequestException
            raise err
        self.max_hrefs = max_hrefs


    def get_href_list(self):
        page = requests.get(self.rootURL)
        soup = BeautifulSoup(page.content, 'html.parser')
        href_list = []
        for a in soup.find_all('a'):
            href = a.get("href")
            if href is None:
                continue
            if not ('.com' in href or '.vn' in href):           ## href is a subfolder in the webpage
                href = self.rootURL + '/' + href
            href = href.rstrip('/')
            if href == self.rootURL:
                continue
            if not self.isURLReachable(href):
                continue
            href_list.append(href)
            if len(href_list) >= self.max_hrefs:
                break
        return href_list

    def isURLReachable(self, url):
        try:
            page = requests.get(url)
            print("Valid URL. A Traverser object created.")

        except requests.exceptions.RequestException as err:
            print("URL {} is unreachable.".format(url))
            return False
            # raise err   # if not raising error here. An object with invalid URL will eventually cause exception later
        return True
        

    
##### MAIN ##### *to test this file 

# url = "https://fptshop.com.vn/"

# travser1 = LinkTraverser(rootURL = url, max = 23)
# list = travser1.get_href_list()
# if list is not None:
#     print(len(list))


# travser2 = LinkTraverser(rootURL = url)
# list = travser2.get_href_list()
# if list is not None:
#     print(len(list))        
#     print(list)
