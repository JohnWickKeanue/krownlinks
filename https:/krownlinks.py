
import time
import requests
from bs4 import BeautifulSoup 
print("Everything Looks Good! Lets Continue.")

url = "https://krownlinks.me/HRcoQ2Sl"  #@param {type:"string"}



def bypass(url):
    client = requests.session()
    
    DOMAIN = "https://go.exozed.com"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"

    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("

# ---------------------------------------------------------------------------------------------------------------------

print(bypass(url))
