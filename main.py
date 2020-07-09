from typing import Optional

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
import json
import urllib.request as url

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def Gallery(request: Request):
    """
    displays the gallery on homepage
    """
    response = requests.get(
        "https://api.unsplash.com/search/photos?query=ireland&page=1&per_page=20&client_id"
        "=2ec7WhtR7mQIuxbRBKTqv5HC9sk1RfcnKKWirbOockU")

    data = response.json()

    # file_names = []
    # cnt = 1
    # for img_data in data['results']:
    #     if cnt > 4: break
    #     file_names.append("img" + str(cnt) + ".jpg")
    #     img_url = img_data['urls']['small']
    #     url.urlretrieve(img_url, file_names[cnt-1])
    #     cnt += 1

    URL = []
    cnt = 0
    for images in data['results']:
        if cnt > 14: break
        URL.append(images['urls']['small'])
        cnt += 1

    return templates.TemplateResponse("home.html", {
        "request": request,
        "URL1": URL[0],
        "URL2": URL[1],
        "URL3": URL[2],
        "URL4": URL[3],
        "URL5": URL[4],
        "URL6": URL[5],
        "URL7": URL[6],
        "URL8": URL[7],
        "URL9": URL[8],
        "URL10": URL[9],
        "URL11": URL[10],
        "URL12": URL[11],
        "URL13": URL[12],
        "URL14": URL[13],
        "URL15": URL[14],
    })
