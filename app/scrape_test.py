import bs4, sys, requests, webbrowser, re

def scrape_stuff(band_name):
    url = str("https://google.com/search?q=" + "genius+lyrics+" + str(band_name).replace(" ","+"))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('.r a')

    print(linkElems)

    res = requests.get('https://google.com' + linkElems[0].get('href'))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    html_text = soup.select('.lyrics')[0].text
    return html_text
    html_text = re.sub("[\(\[].*?[\)\]]", "", html_text)
    
    # html_text = html_text.replace('\n', ' ')
    # words = html_text.split(' ')
    # words = list(filter(None, words))
    # words = [x.lower() for x in words]



# Way to get words from all songs that have ever existed
# Parse words
# Visualize based on frequency, or time
# Get the genre of the song?
# Website?