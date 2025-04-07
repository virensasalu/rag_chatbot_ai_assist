import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import faiss
import openai
import numpy as np
import re
from IPython.display import Markdown, display



class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string.strip() if soup.title else "No title found"
        

        for irrelevant in soup(["script", "style", "img", "input", "noscript", "footer", "header", "nav", "form"]):
            irrelevant.decompose()

        self.soup = soup
        raw_text = soup.get_text(separator="\n", strip=True)
        self.text = re.sub(r'\n{2,}', '\n\n', raw_text)

    def export_as_markdown(self, file_path="output.md"):
        def tag_to_markdown(tag):
            if tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(tag.name[1])
                return f"{'#' * level} {tag.get_text(strip=True)}\n"
            elif tag.name == "p":
                return f"{tag.get_text(strip=True)}\n"
            elif tag.name == "ul":
                return '\n'.join([f"- {li.get_text(strip=True)}" for li in tag.find_all("li")]) + "\n"
            elif tag.name == "ol":
                return '\n'.join([f"{i+1}. {li.get_text(strip=True)}" for i, li in enumerate(tag.find_all("li"))]) + "\n"
            else:
                return ""

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {self.title}\n\n")
            for tag in self.soup.body.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol"], recursive=True):
                markdown = tag_to_markdown(tag)
                if markdown.strip():
                    f.write(markdown + "\n")

ed_about = Website("https://jeevatrials.com/about/")
ed_serve = Website("https://jeevatrials.com/who-we-serve/")
ed_journey= Website("https://jeevatrials.com/customer-journey/")
#print(ed.title)
#print(ed.text)


#ed_about.export_as_markdown("knowledge_base/about.md")
#ed_serve.export_as_markdown("knowledge_base/serve.md")
#ed_journey.export_as_markdown("knowledge_base/journey.md")