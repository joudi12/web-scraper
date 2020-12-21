from web_scraper import __version__


def test_version():
    assert __version__ == '0.1.0'


from web_scraper.scraper import *

def test_count():

    URL = 'https://en.wikipedia.org/wiki/Arab_world' 
    assert get_citations_needed_count(URL) == 3  

