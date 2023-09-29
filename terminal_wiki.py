import requests
import logging
import sys
from bs4 import BeautifulSoup
import markdownify

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

def scrape_wiki(text):
    URL = f"https://en.wikipedia.org/wiki/{text}"
    r = requests.get(URL)

    soup  = BeautifulSoup(r.content, "html.parser")

    tags = ["h1", "h2", "h3", "h4", "h5", "p"]

    processed_s = list()

    for tag in soup.find_all(tags):

        if tag.name != "p" and (tag.text.strip().startswith("Notes") or tag.text.strip().startswith("See also")):
            break
        if tag.text.strip() != "Contents":
            processed_s.append(f"<{tag.name}>{tag.text.strip()}</{tag.name}>")
    
    # with open("data/output1.html", "w", encoding='utf-8') as file:
    #     file.write("\n".join(processed_s))

    h = markdownify.markdownify("\n".join(processed_s), heading_style="ATX")
    # with open("data/output1.md", "w", encoding='utf-8') as file:
    #     file.write(h)
    
    print(h)

def main():
    scrape_wiki("_".join(sys.argv[1:]).title())


if __name__ == '__main__':
    main()