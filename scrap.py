from usp.tree import sitemap_tree_for_homepage
from langchain_community.document_loaders import WebBaseLoader
import json, requests
from bs4 import BeautifulSoup 
import nltk
from nltk.tokenize import sent_tokenize
import pickle as pkl

# tree = sitemap_tree_for_homepage("https://www.angelone.in/")

def extract_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove unwanted sections like footers, navigation, etc.
    for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'noscript']):
        tag.decompose()

    # Optionally remove repetitive elements by class or id
    for tag in soup.find_all(attrs={"class": ["footer", "nav", "header", "app-download", "contact-bar"]}):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else ""
    
    # Only take relevant body paragraphs
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

    # return {'title': title, 'content': content}
    return content

def find_page(tree):
    all_data = []
    for page in tree.all_pages():
        if '/support/' in page.url:
            data = extract_page_content(page.url)
            all_data.append(data)
            

    return all_data


# all_data = find_page(tree)
# with open('angel_data.pkl','wb') as f:
#     pkl.dump(all_data,f)



def chunks(text,max_token=400):
    nltk.download('punkt')

    sentences = sent_tokenize(text)
    chunk,curr = [] , []
    total_tokens = 0

    for sentence in sentences:
        total_len = len(sentence.split(' '))
        if total_len + total_tokens > max_token:
            chunk.append(''.join(curr))
            curr = [sentence]
            total_tokens = total_len
        else:
            curr.append(sentence)
            total_tokens += total_len

    if curr:
        chunk.append(''.join(curr))

    return chunk


