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

    for i in result:
        parent = i.findAll('a',title='Wikipedia:Citation needed')
        if parent: 
            paragraph = i.text
            partition = paragraph.split("[citation needed]")
            dictinery_for_citation = {
                                    "sentence": partition[0], 
                                    "paragraph": i.text
                                    }
            for i in dictinery_for_citation:
                print(f'{i} --->{dictinery_for_citation[i]}')
                print('*************************************************')
            # print(dictinery_for_citation)
            
      

  

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Arab_world'  
    get_citations_needed_count(url) 
    get_citations_needed_report(url) 
    
    