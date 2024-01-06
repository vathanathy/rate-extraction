import requests 
from bs4 import BeautifulSoup
import requests
import json
from dotenv import load_dotenv
import os


#Load env variables
load_dotenv()

def rate_extract(): 
    URL = "https://www.google.com/finance/quote/EUR-USD?sa=X&ved=2ahUKEwiC6KjN38mDAxWuTqQEHS3hCYEQmY0JegQIBhAr"
    r = requests.get(URL) 
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    result = soup.find('div', attrs = {'class':'YMlKec fxKbKc'})
    return result.text

def pushbullet_noti(title, body):
 
    TOKEN = os.environ.get("api-token")  # Pass your Access Token here
    # Make a dictionary that includes, title and body
    msg = {"type": "note", "title": title, "body": body}
    # Sent a posts request
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:  # Check if fort message send with the help of status code
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')
 
if __name__ == "__main__":
    pushbullet_noti("Current rate", rate_extract())