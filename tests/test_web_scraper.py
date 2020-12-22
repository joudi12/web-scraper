from web_scraper import __version__


def test_version():
    assert __version__ == '0.1.0'


from web_scraper.scraper import *

def test_count():

    URL = 'https://en.wikipedia.org/wiki/Arab_world' 
    assert get_citations_needed_count(URL) == 3  

def test_citations():
    URL = 'https://en.wikipedia.org/wiki/Arab_world' 
    actuall = ['According to UNESCO, the average rate of adult literacy (ages 15 and older) in this region is 76.9%. In Mauritania and Yemen, the rate is lower than the average, at barely over 50%. Syria, Lebanon, Palestine and Jordan record a high adult literacy rate of over 90%.[citation needed] The average rate of adult literacy shows steady improvement, and the absolute number of adult illiterates fell from 64 million to around 58\xa0million between 1990 and 2000–2004. Overall, the gender disparity in adult literacy is high in this region, and of the illiteracy rate, women account for two-thirds, with only 69 literate women for every 100 literate men. The average GPI (Gender Parity Index) for adult literacy is 0.72, and gender disparity can be observed in Egypt, Morocco, and Yemen. Above all, the GPI of Yemen is only 0.46 in a 53% adult literacy rate.[35] According to a UN survey, in the Arab world, the average person reads four pages a year and one new title is published each year for every 12,000 people.[36] The Arab Thought Foundation reports that just above 8% of people in Arab countries aspire to get an education.[36]\n', 
            'The Lebanese Civil War was a multifaceted civil war in Lebanon, lasting from 1975 to 1990 and resulting in an estimated 120,000 fatalities. Another one million people (a quarter of the population) were wounded,[citation needed] and today approximately 76,000 people remain displaced within Lebanon. There was also a mass exodus of almost one million people from Lebanon.\n', 'As of 2006, the Arab world accounts for two-fifths of the gross domestic product and three-fifths of the trade of the wider Muslim world.[citation needed]\n']
    expected = get_citations_needed_report(URL)
    assert actuall==expected