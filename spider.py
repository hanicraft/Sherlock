import optparse
import requests
import re
import urlparse

def crawl(target):
    target_links = []
    
    def extract_links(url):
        response = requests.get(url)
        return re.findall("(?:href=\")(.*?)\"", response.content)
    
    def crawl_recursively(url):
        links = extract_links(url)
        for link in links:
            link = urlparse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            if target in link and link not in target_links:
                target_links.append(link)
                print(link)
                crawl_recursively(link)

    crawl_recursively(target)
