from flask import Flask, jsonify, request
import requests
import json
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/Home/", methods=["GET"])   
def get_ReadManga():
    session = requests.Session()
    readmanga = session.get('https://readm.org/')
    soup = BeautifulSoup(readmanga.content,'html.parser')
    ReadManga = []
    for item in soup.findAll('div', id="router-view"):
      Read_Manga = dict()
      item1 = item.find_all('div', class_='segment-title')
      for item11 in item1:
        Read_Manga['title'] = item11.text
        ReadManga.append(Read_Manga.copy())
      Hot_Manga = dict()  
      item2 = item.find_all('div', class_='item')
      for item22 in item2:
        Hot_Manga['Hot_Manga_link'] ='https://readm.org' + item22.find('a').get('href')
        Hot_Manga['Hot_Manga_name'] =item22.find('a').get('title')
        Hot_Manga['Hot_Manga_img'] ='https://readm.org' + item22.find('a').find('img').get('src')
        Hot_Manga['Hot_Manga_bookmark'] = item22.find('a').find('div').find('span', class_='subscribe-count').text
        Hot_Manga['Hot_Manga_like'] = item22.find('a').find('div').find('span', class_='favorite-count').text
        ReadManga.append(Hot_Manga.copy()) 
      Popular_Manga = dict()
      item3 = item.find_all('ul',id="latest_trailers")
      for item33 in item3:
        item333 = item33.find_all('li')
        for item31 in item333:
          Popular_Manga['Popular_Manga_link'] ='https://readm.org' + item33.find('a').get('href')
          Popular_Manga['Popular_Manga_name'] =item33.find('a').get('title')
          Popular_Manga['Popular_Manga_img'] ='https://readm.org' + item33.find('a').find('div').find('img').get('data-src')
          Popular_Manga['Popular_Manga_watch_now'] =item33.find('a').find('div').find('span').text
          Popular_Manga['Popular_Manga_chapter'] =item33.find('a').find('a').text
          Popular_Manga['Popular_Manga_chapter_link'] ='https://readm.org' + item33.find('a').find('a').get('href')
          ReadManga.append(Popular_Manga.copy())   
      Latest_Updates = dict()
      item4 = item.find_all('div', class_="poster poster-xs")
      for item41 in item4:
        Latest_Updates['Latest_Updates_link'] ='https://readm.org' + item41.find('div').find('h2').find('a').get('href')
        Latest_Updates['Latest_Updates_name'] =item41.find('div').find('h2').find('a').text
        Latest_Updates['Latest_Updates_time'] =item41.find('span',class_="date").text
        item411 = item41.find_all('ul', class_='chapters')
        for iwe in item411:
          item42 = iwe.find_all('li')
          for item43 in item42:
            Latest_Updates['Latest_Updates_chapter_link'] ='https://readm.org' + item43.find('a').get('href')
            Latest_Updates['Latest_Updates_chapter'] =item43.find('a').text
            ReadManga.append(Latest_Updates.copy())      
      Recently_Choice = dict()
      item5 = item.find_all('div',class_="poster poster-md")
      for item51 in item5:
        Recently_Choice['Recently_Choice_link'] ='https://readm.org' + item51.find('div', class_="poster-media").find('a').get('href')
        Recently_Choice['Recently_Choice_name'] = item51.find('div', class_="poster-media").find('a').find('img').get('alt')
        Recently_Choice['Recently_Choice_img'] ='https://readm.org' + item51.find('div', class_="poster-media").find('a').find('img').get('data-src')
        Recently_Choice['Recently_Choice_bookmark'] = item51.find('span', class_="item rating").text
        Recently_Choice['Recently_Choice_like'] = item51.find('span', class_="item year").text
        ReadManga.append(Recently_Choice.copy())
      return ReadManga
    
@app.route("/PopularManga/<int:index>", methods=["GET"])  
# index 1->10 
def get_Popular_Manga(index):
  PopularManga = []
  session = requests.Session()
  popularmanga = session.get('https://readm.org/popular-manga/' +str(index))
  soup = BeautifulSoup(popularmanga.content,'html.parser')
  for item in soup.findAll('ul', class_="filter-results"):
    Popular_Manga = dict()
    item1=item.find_all('li', class_="mb-lg")
    for item2 in item1:
      Popular_Manga['Popular_Manga_name']  = item2.find('div').find('a').get('title')
      Popular_Manga['Popular_Manga_link']  = 'https://readm.org' + item2.find('div').find('a').get('href')
      Popular_Manga['Popular_Manga_img']  ='https://readm.org' +  item2.find('div').find('a').find('img').get('src')
      Popular_Manga['Popular_Manga_content'] = item2.find('p', class_='desktop-only excerpt').text
      PopularManga.append(Popular_Manga.copy())  
    item3 = item.find_all('span', class_="genres")
    Popular_title = dict()
    for item31 in item3:
      ite = item31.find_all('a')
      for iteme in ite:
        Popular_title['Popular_title:'] = iteme.get('title')
        Popular_title['Popular_title_link:'] ='https://readm.org' + iteme.get('href')
        PopularManga.append(Popular_title.copy())    
    item4 = item.find_all('td')
    Popular_detail = dict()
    for item41 in item4:
      item42 = item41.find_all('div')
      for item43 in item42:
        Popular_detail['Popular_detail_title'] = item41.text
      item44 = item41.find_all('a')
      for item45 in item44:
        Popular_detail['Popular_detail_chapter_list_link'] ='https://readm.org' + item45.get('href')
        PopularManga.append(Popular_detail.copy())
  return PopularManga

@app.route("/LatestUpdates/<int:index>", methods=["GET"])  
# index 1->10 
def get_Latest_Releases(index):
  LatestUpdates = []
  session = requests.Session()
  latestupdates = session.get('https://readm.org/latest-releases/' +str(index))
  soup = BeautifulSoup(latestupdates.content,'html.parser')
  for item in soup.findAll('ul', class_='clearfix latest-updates'):
    item4 = item.find_all('div', class_="poster poster-xs")
    Latest_Updates = dict()
    for item41 in item4:
        Latest_Updates['Latest_Updates_link'] ='https://readm.org' + item41.find('div').find('h2').find('a').get('href')
        Latest_Updates['Latest_Updates_name'] =item41.find('div').find('h2').find('a').text
        Latest_Updates['Latest_Updates_time'] =item41.find('span',class_="date").text
        item411 = item41.find_all('ul', class_='chapters')
        for iwe in item411:
          item42 = iwe.find_all('li')
          for item43 in item42:
            Latest_Updates['Latest_Updates_chapter_link'] ='https://readm.org' + item43.find('a').get('href')
            Latest_Updates['Latest_Updates_chapter'] =item43.find('a').text
            LatestUpdates.append(Latest_Updates.copy())
    return LatestUpdates
  
@app.route("/Recently-Added-Manga/<int:index>", methods=["GET"])  
# index 1->691(692 -> 1036 chưa có gì) 
def get_Recently_Added_Manga(index):
  NewManga = []
  session = requests.Session()
  newmanga = session.get('https://readm.org/new-manga/' +str(index))
  soup = BeautifulSoup(newmanga.content,'html.parser')
  for item in soup.findAll('ul', class_='clearfix mb-0'):
      New_Manga = dict()
      item5 = item.find_all('div',class_="poster poster-md")
      for item51 in item5:
        New_Manga['New_Manga_link'] ='https://readm.org' + item51.find('div', class_="poster-media").find('a').get('href')
        New_Manga['New_Manga_name'] = item51.find('div', class_="poster-media").find('a').find('img').get('alt')
        New_Manga['New_Manga_img'] ='https://readm.org' + item51.find('div', class_="poster-media").find('a').find('img').get('data-src')
        New_Manga['New_Manga_bookmark'] = item51.find('span', class_="item rating").text
        New_Manga['New_Manga_like'] = item51.find('span', class_="item year").text
        NewManga.append(New_Manga.copy())
      return NewManga
    
@app.route("/Caterogy/", methods=["GET"])  
def get_Caterogy():
  link_full = request.headers.get('link_full')
  CaterogyManga =[]
  session = requests.Session()
  caterogy = session.get(link_full)
  soup = BeautifulSoup(caterogy.content,'html.parser')
  for item in soup.findAll('div', class_='cat-tags'):
    Caterogy_Manga =dict()
    item1= item.find_all('a')
    for item11 in item1:
      Caterogy_Manga['Caterogy_Manga-name'] = item11.text
      Caterogy_Manga['Caterogy_Manga-link'] ='https://readm.org' + item11.get('href')
      CaterogyManga.append(Caterogy_Manga.copy())
  m=0
  for item2 in soup.findAll('ul', class_='filter-results'):
    Manga_name = dict()
    item22 = item2.find_all('div', class_='poster-with-subject')
    for item3 in item22:
      m=m+1
      Manga_name['Manga_name_id'] = m
      Manga_name['Manga_name_title'] = item3.find('a').get('title')
      Manga_name['Manga_name_link'] ='https://readm.org' + item3.find('a').get('href')
      Manga_name['Manga_name_img'] ='https://readm.org' + item3.find('a').find('img').get('data-src')
      Manga_name['Manga_name_content'] = item3.find('p', class_='desktop-only excerpt').text
      CaterogyManga.append(Manga_name.copy())
  n=0
  for item4 in soup.findAll('tr'):
    value = dict()
    item24 = item4.find_all('td')
    n=n+1
    for item25 in item24:
      value['id']=n
      value['valuate'] = item25.text
      CaterogyManga.append(value.copy())  
  return CaterogyManga

@app.route("/Detailmanga/", methods=["GET"])  
def get_Detailmanga():
  link_full = request.headers.get('link_full')
  Detailmanga =[]
  session = requests.Session()
  Detail = session.get(link_full)
  soup = BeautifulSoup(Detail.content,'html.parser')
  Detail_manga = dict()
  Detail_manga['Detail_manga_title'] = soup.find('div', id="series-tabs").find('a').text
  Detail_manga['Detail_manga_link'] = soup.find('div', id="series-tabs").find('a', id="share-dialog").get('data-url')
  Detail_manga['Detail_manga_img'] ='https://readm.org' + soup.find('a', class_="ui image").find('img').get('src')
  Detail_manga['Detail_manga_content'] = soup.find('p', id="tv-series-desc").find('p').text
  Detailmanga.append(Detail_manga.copy()) 
  for item in soup.findAll('div', class_="media-meta"):
    Detail_value = dict()
    item1 =item.find_all('td')
    for item2 in item1:
      Detail_value['Detail_geners_value'] = item2.text
      Detailmanga.append(Detail_value.copy()) 
  for item3 in soup.findAll('div', id="series-profile-content-wrapper"):
    Detail_genres = dict()
    item31 = item3.find_all('div', class_='item')
    for item41 in item31:
      item4 = item41.find_all('a')
      for item5 in item4:
        Detail_genres['genres'] = item5.text
        Detailmanga.append(Detail_genres.copy())
  for itme in soup.findAll('div', class_="sixteen wide tablet eleven wide computer column"):
    Chapter_list = dict()
    itme1 = itme.find_all('div',class_="ui tab")
    for itme2 in itme1:
      itme3 = itme2.find_all('h6',class_="truncate")
      for itme4 in itme3:
        Chapter_list['Chapter_list_link'] ='https://readm.org' + itme4.find('a').get('href')
        Chapter_list['Chapter_list_name'] ='https://readm.org' + itme4.find('a').text
        Detailmanga.append(Chapter_list.copy())
  return Detailmanga

@app.route("/Detail-chapter/", methods=["GET"])  
def get_Detailchapter():
  link_full = request.headers.get('link_full')
  Detailchapter =[]
  session = requests.Session()
  Detail = session.get(link_full)
  soup = BeautifulSoup(Detail.content,'html.parser')
  Detail_chapter = dict()
  Detail_chapter['Detail_chapter_title'] = soup.find('title').text
  Detail_chapter['Detail_chapter_date'] = soup.find('div',class_="media-date").find('span').text
  Detailchapter.append(Detail_chapter.copy())
  for item in soup.findAll('div', class_='ch-images ch-image-container'):
    item1 = item.find_all('img')
    Detail_chapter_image = dict()
    for item2 in item1:
      Detail_chapter_image['Detail_chapter_image_link'] ='https://readm.org' + item2.get('src')
      Detailchapter.append(Detail_chapter_image.copy())
  return Detailchapter
if __name__ == "__main__":
   app.run(host='0.0.0.0')
    