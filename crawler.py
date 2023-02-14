import optparse
import requests

def discover_subdomains_and_urls(target):
    subdomains = []
    urls = []

    def request(url):
        try:
            return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
            pass

    with open("subdomains-wordlist.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + target
            response = request(test_url)
            if response:
                subdomains.append(test_url)

    with open("files-and-dirs-wordlist.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = target + "/" + word
            response = request(test_url)
            if response:
                urls.append(test_url)

    return subdomains, urls
