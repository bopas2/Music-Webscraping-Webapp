import bs4, sys, requests, webbrowser, re, time

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def scrape_stuff(band_name):
    # Navigating to website with a list of the band's songs
    song_list_url = str("https://google.com/search?q=" + '"songfacts.com"+list+of+songs+by+' + '"' + str(band_name).replace(" ","+") + '"')
    res = requests.get(song_list_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('.r a')
    song_website_url = 'https://google.com' + linkElems[0].get('href')
    #webbrowser.open(song_website_url)

    # Scraping webpage of the band's songs' titles
    res = requests.get(song_website_url, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    potential_titles = soup.find_all('a')
    song_titles = [txt.string for txt in potential_titles if txt.parent.name == "li"]
    song_titles = song_titles[38:-13]

    for song in song_titles: 
    # url = str("https://google.com/search?q=" + "genius+lyrics+" + str(band_name).replace(" ","+"))
    # res = requests.get(url)
    # res.raise_for_status()
    # soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # linkElems = soup.select('.r a')

    # res = requests.get('https://google.com' + linkElems[0].get('href'))
    # print('https://google.com' + linkElems[0].get('href'))
    # res.raise_for_status()

    # soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # html_text = soup.select('.lyrics')[0].text
    # return html_text
    # html_text = re.sub("[\(\[].*?[\)\]]", "", html_text)
    
    # html_text = html_text.replace('\n', ' ')
    # words = html_text.split(' ')
    # words = list(filter(None, words))
    # words = [x.lower() for x in words]



# Way to get words from all songs that have ever existed
# Parse words
# Visualize based on frequency, or time
# Get the genre of the song?
# Website?