# Sherlock

a spider with bruteforcing tool that unleashes the power of web created in python 3.10

# features

1- spider

2- crawler

3- bruteforce tool

#examples of use

#discovering subdomains
import discover_subdomains_and_urls

subdomains, urls = discover_subdomains_and_urls("example.com")
print(subdomains)
print(urls)

#brute forcing
import brute_force_password

password = brute_force_password("http://example.com/login.php", "passwords.txt")
print(password)

#crawling urls
import crawl

crawl("http://example.com")
