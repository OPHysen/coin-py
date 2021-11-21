import requests
from bs4 import BeautifulSoup
import lxml
import re
class movie_aap():
    
    def pop_movie():
        film_data = requests.get("https://www.imdb.com/chart/moviemeter/")
        soup = BeautifulSoup(film_data.content, "lxml")
        a = soup.find_all("td", attrs = {"class" : "titleColumn"})
        for x in a:
            index = x.find("a").text
            index2 = x.find("span").text
            print(index, index2)
        
    
    def coming_soon():
        film_data = requests.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")
        soup = BeautifulSoup(film_data.content, "lxml")
        a = soup.find_all("td", attrs = {"class" : "overview-top"})
        for x in a:
            index = x.find("a").text
            print(index)

    def top_news():
        film_data = requests.get("https://www.imdb.com/news/movie/?ref_=nv_nw_mv")
        soup = BeautifulSoup(film_data.content, "lxml")
        a = soup.find_all("h2", attrs = {"class" : "news-article__title"})
        for x in a:
            index = x.find("a").text
            print(index)
        

    def search_demo():
        while True:
            user_input1 = int(input("enter 1 for celebs or enter 2 for movies"))
            search_user = input("search something... ")
            film_data = requests.get("https://www.imdb.com/find?q="+search_user+"&ref_=nv_sr_sm")
            soup = BeautifulSoup(film_data.content, "lxml")
            a = soup.find_all("td", {"class": "result_text"})
            for x in a:
                index1 = x.text
                index = x.find("a").text
                print(index, index1)

#movie_aap.pop_movie()
#movie_aap.coming_soon()
#movie_aap.top_news()
#movie_aap.search_demo()
