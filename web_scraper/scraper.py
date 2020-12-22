import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    count = soup.findAll('a',title='Wikipedia:Citation needed')
    # print(len(count))
    return len(count)

             
                    

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.findAll('p')
    finall = []
    for i in result:
        parent = i.findAll('a',title='Wikipedia:Citation needed')
        if parent: 
            paragraph = i.text
            find_sentence = paragraph.split("[citation needed]")
            print(f'The sentense----> :{find_sentence[0]}')
            print(f'The paragraph ------>:{paragraph}')
            print('*************************************************')
            finall.append(paragraph)
            
   
    return finall

            
      

  

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Arab_world'  
    get_citations_needed_count(url) 
    get_citations_needed_report(url) 
    
    