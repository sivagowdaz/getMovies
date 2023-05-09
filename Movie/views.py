from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

recent_movie_list = []


def get_recent_movie():
    BASE_URL = "https://ww2.5movierulz.mx/?s="
    print("inside the get_recent_movie function")

    request_data = requests.get(BASE_URL)
    data = request_data.text
    print("THE DATA IS ", data)
    soup = BeautifulSoup(data, "html.parser")

    recent_movie = soup.find(
        "li", {"class": "widget widget_movie_recent_post_widget"})
    recent_movie_links = recent_movie.find_all("a")

    for removielink in recent_movie_links:
        removieli = removielink.get("href")
        redata = requests.get(removieli)
        redata = redata.text
        resoup = BeautifulSoup(redata, "html.parser")
        retitle = resoup.find("h2", {"class": "entry-title"}).text
        reimage = resoup.find(
            "div", {"class": "entry-content"}).find("img").get("src")
        recent_movie_list.append((removieli, reimage, retitle[0:40]))


def getNewMovie(request):
    BASE_URL = "https://ww2.5movierulz.mx/?s="
    search_word = str(request.POST.get("search"))

    if search_word:
        if len(search_word.split(" ")) > 1:
            search_word = search_word.replace(" ", "+")
        FINAL_URL = BASE_URL + search_word
    else:
        FINAL_URL = BASE_URL

    request_data = requests.get(FINAL_URL)

    data = request_data.text
    soup = BeautifulSoup(data, "html.parser")

    movie_listings = soup.find_all("div", {"class": "boxed film"})
    recent_movie = soup.find(
        "li", {"class": "widget widget_movie_recent_post_widget"})
    print("all movie list", recent_movie)
    recent_movie_links = recent_movie.find_all("a")

    # recent_movie_list = []
    final_movie_list = []

    for movie in movie_listings:
        movie_title = movie.text
        req_movie = movie.find("div", {"class": "cont_display"})
        movie_img = req_movie.find("img").get("src")
        movie_link = req_movie.find("a").get("href")
        final_movie_list.append((movie_link, movie_img, movie_title[0:45]))

    for removielink in recent_movie_links:
        removieli = removielink.get("href")
        print(removieli)
        redata = requests.get(removieli)
        redata = redata.text
        resoup = BeautifulSoup(redata, "html.parser")
        retitle = resoup.find("h2", {"class": "entry-title"}).text
        reimage = resoup.find(
            "div", {"class": "entry-content"}).find("img").get("src")
        recent_movie_list.append((removieli, reimage, retitle[0:40]))

    stuff_for_frontend = {
        "search": search_word,
        "final_list": final_movie_list[2:],
        "recent_movie_list": recent_movie_list,
    }

    return render(request, "movie/home.html", stuff_for_frontend)


def getKannadaMovie(request):
    BASE_URL_DICTIONARY = {
        "featured": "https://ww2.5movierulz.mx/featured/",
        "kannada": "https://ww2.5movierulz.mx/kannada-movie/",
        "tamil": "https://ww2.5movierulz.mx/tamil-movie-free/",
        "malayalam": "https://ww2.5movierulz.mx/malayalam-movie-online/",
        "telugu": "https://ww2.5movierulz.mx/telugu-movie/",
        "bollywood": "https://ww2.5movierulz.mx/bollywood-movie-free/",
        "hollywood": "https://ww2.5movierulz.mx/hollywood-movie-2021/",
        "adult": "https://ww2.5movierulz.mx/adult-movie/",
        "dvdrip": "https://ww2.5movierulz.mx/dvdrip/",
    }

    GENRE_URL = "https://ww2.5movierulz.mx/tag/"

    INTRESTED_SEARCH = ""

    if request.POST.get("language"):
        BASE_URL = BASE_URL_DICTIONARY[request.POST.get("language")]
        INTRESTED_SEARCH = request.POST.get("language")
    else:
        BASE_URL = BASE_URL_DICTIONARY["featured"]

    if request.POST.get("genre"):
        BASE_URL = GENRE_URL + request.POST.get("genre") + "/"
        INTRESTED_SEARCH = request.POST.get("genre")

    if request.POST.get("new_page"):
        turn_type, page_no, prev_url = request.POST.get("new_page").split(" ")
    else:
        turn_type = page_no = None

    if page_no:
        PAGE_COUNT = int(page_no)
        BASE_URL = prev_url

    if turn_type == "next_page" and PAGE_COUNT:
        PAGE_COUNT += 1
        FINAL_URL = BASE_URL + "page/" + str(PAGE_COUNT)
    elif turn_type == "prev_page" and PAGE_COUNT != 1:
        PAGE_COUNT -= 1
        FINAL_URL = BASE_URL + "/page/" + str(PAGE_COUNT)
    else:
        FINAL_URL = BASE_URL
        PAGE_COUNT = 1

    request_data = requests.get(FINAL_URL)

    data = request_data.text
    soup = BeautifulSoup(data, "html.parser")

    movie_listings = soup.find_all("div", {"class": "boxed film"})

    final_movie_list = []

    for movie in movie_listings:
        movie_title = movie.text
        req_movie = movie.find("div", {"class": "cont_display"})
        movie_img = req_movie.find("img").get("src")
        movie_link = req_movie.find("a").get("href")
        final_movie_list.append((movie_link, movie_img, movie_title[:40]))

    if recent_movie_list == []:
        get_recent_movie()

    stuff_for_frontend = {
        "final_list": final_movie_list[2:],
        "page_number": str(PAGE_COUNT),
        "url": BASE_URL,
        "recent_movie_list": recent_movie_list,
        "intrested_search": INTRESTED_SEARCH,
    }

    print(stuff_for_frontend["recent_movie_list"])
    return render(request, "movie/kannadaMovie.html", stuff_for_frontend)


def downloadMovie(request):
    requested_data = requests.get(
        "https://ww2.5movierulz.mx/konda-polam-2021-hdrip-telugu-full-movie-watch-online-free/"
    )
    data = requested_data.text
    soup = BeautifulSoup(data, "html.parser")
    movie_links = []
    download_links = soup.find_all("a", {"class": "mv_button_css"})

    for links in download_links:
        movie_links.append(links.get("href"))
    stuff_for_frontend = {"links": movie_links}
    return render(request, "movie/testing.html", stuff_for_frontend)
