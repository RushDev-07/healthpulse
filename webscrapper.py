from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.request import Request, urlopen


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'span', 'div']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)
    return u"\n ".join(t.strip() for t in visible_texts)


file1=open(r"C:\Users\Rushabh\localGPT\SOURCE_DOCUMENTS\myfile.txt","w",encoding="utf-8") # Opening the file in which the data will be stored
file2=open("C:\Users\Rushabh\localGPT\Link_url.txt","r") #Opening the file in which the website url will be stored
data=file2.read()
data_into_list=data.split("\n")
i=0
if(data_into_list[i][0]=='h' or data_into_list[i][0]=='w'):
    for i in range(len(data_into_list)):
        root_url=data_into_list[i]
        req = Request(root_url,headers={'User-Agent': 'Mozilla/5.0'})
        html_page = urlopen(req)

        soup = BeautifulSoup(html_page, "lxml")

        links = []
        for link in soup.findAll('root_url'):
            links.append(link.get('href'))
        for i in range(len(links)):
            if(links[i]== None):
                continue
            if(links[i][0]=='h'): #The full link will be sent here 
                final_url=links[i]
                html = urllib.request.urlopen(final_url).read()
                file1.writelines(text_from_html(html))
                print(final_url)
            if(links[i][0]=='/'): #partial links will be here to be joined with the root_url
                final_url = root_url + links[i]

                print(final_url)

                html = urllib.request.urlopen(final_url).read()
                file1.writelines(text_from_html(html))

file1.close()
file2.close()