import requests
import logging
from bs4 import BeautifulSoup
import markdownify

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

def main():
    URL = "https://en.wikipedia.org/wiki/String_Theory"
    r = requests.get(URL)

    soup  = BeautifulSoup(r.content, "html.parser")

    tags = ["h1", "h2", "h3", "h4", "h5", "p"]

    processed_s = list()

    for tag in soup.find_all(tags):

        if tag.text.strip().startswith("Notes"):
            break
        if tag.text.strip() != "Contents":
            processed_s.append(f"<{tag.name}>{tag.text.strip()}</{tag.name}>")
    
    # with open("data/output1.html", "w", encoding='utf-8') as file:
    #     file.write("\n".join(processed_s))

    h = markdownify.markdownify("\n".join(processed_s), heading_style="ATX")
    with open("data/output1.md", "w", encoding='utf-8') as file:
        file.write(h)



if __name__ == '__main__':
    main()