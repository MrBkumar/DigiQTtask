from bs4 import BeautifulSoup
import requests
import extruct
from w3lib.html import get_base_url

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'html.parser')
movies_table_list = soup.find("table", class_="chart full-width")

movies_table_body = movies_table_list.find("tbody", class_="lister-list")

movie_tr = movies_table_body.find_all('tr')
movie_dict , data = {}, []
count = 1

def get_html(url):
    """Get raw HTML from a URL."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers=headers)
    return req.text

def get_metadata(html: bytes, url: str):
    """Fetch JSON-LD structured data."""
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=['json-ld'],
        uniform=True
    )['json-ld']
    return metadata

for context in movie_tr:
    try:
        movie_poster_image = context.find('td', class_="posterColumn").find('a').find('img').attrs

        movie_name = context.find('td', class_="titleColumn").find('a').text
        movie_dict['movie_name'] = movie_name
        movie_rating = context.find('td', class_="ratingColumn imdbRating").find('strong').text
        movie_dict['movie_rating'] = movie_rating
        
        middle_href = context.find('td', class_="posterColumn").find('a')['href']
        detail_url = 'https://www.imdb.com'+middle_href+'?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=MV9P6PVNXABE35B9XSE2&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_'+ str(count)
        html = get_html(detail_url)
        metadata = get_metadata(html, detail_url)[0]
        movie_dict['release_date'] = metadata['datePublished']
        movie_dict['movie_duration'] = metadata['duration']
        movie_dict['movie_description'] = metadata['description']
        data.append(movie_dict)
        movie_dict= {}
        count+=1
    except:
        print('outer error.......................................')

print(data)

