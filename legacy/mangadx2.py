#!/usr/bin/env python3

import requests as req
import os
import sys

def savePath(url, path):
    #saving_image_any_path
    res = req.get(url, stream=True)
    if res.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in res.iter_content(1024):
                file.write(chunk)
    else:
        print('Faild to Fetch Data!')

class dex:
    def __init__(self):
        self.api_url = "https://api.mangadex.org"

        #self.url = url
        #self cdn_url = url.replace("https://mangadex.org/chapter/", "")
        pass

    def getId(self, manga_name):
        #getting_manga_id
        res = req.get(
        f"{self.api_url}/manga",
        params={"title": manga_name}
        )
        if res.status_code == 200:
            title = res.json()["data"][0]["attributes"]["title"]["en"].replace(" ", "_")
            id_manga = [manga["id"] for manga in res.json()["data"]][0]
            self.id = id_manga
            self.title = title
            return [id_manga, title]
        else:
            print("Manga Not Found")
        pass

    def chapters(self):
        #getting_chapter_list
        languages = ["en"]
        chapters = []
        res = req.get(
            f"{self.api_url}/manga/{self.id}/feed",
            params={"translatedLanguage[]": languages},
            )
        get_data = res.json()["data"]
        for i in range(len(get_data)):
            chapters.append([ get_data[i]["id"], get_data[i]['attributes']['chapter']])
        self.chapters = chapters
        return chapters
        pass

    def save(self):
        url = f"https://api.mangadex.org/at-home/server/{chapter_id}"


if __name__ == "__main__":
    down = dex()
    c = down.getId("GTO")
    d = down.chapters()
    print(c, d)
    #print(sys.argv)
