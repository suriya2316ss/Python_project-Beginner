import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=10)
    r=requests.get(url,timeout=10)
    r.raise_for_status()
    soup=BeautifulSoup(r.text,"html.parser")
    titles=[t.get_text(strip=True) for t in soup.find_all(['h1','h2','h3'])]
    return titles[:30]

def main():
    url=input("URL to scrape:").strip()
    try:
        titles=fetch_titles(url)
        for i,t in enumerate(titles,1):
            print(i,t)
    except Exception as e:
        print("Error:",e)
if __name__=="__main__":
    main()