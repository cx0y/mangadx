# created by cx0y (https://github.com/cx0y)
import os
import requests
import argparse
import time
import sys

#import json
# def get_manga_id(manga_name):
#     base_url = "https://api.mangadex.org"
#     r = requests.get(
#         f"{base_url}/manga",
#         params={"title": manga_name}
#     )
#     if r.status_code == 200:
#        #print(r.json())
#        title = r.json()["data"][0]["attributes"]["title"]["en"].replace(" ", "_")
#        #alltitle = r.json()["data"][0]["attributes"]["altTitles"]
#        #print(json.dumps(r.json()["data"][0]["attributes"], indent=4))
#        a = [manga["id"] for manga in r.json()["data"]][0]
#        return [a,title]
#     else:
#         print("Manga Not Found")

# def get_chapters(id):
#     base_url = "https://api.mangadex.org"
#     languages = ["en"]
#     a = []
#     r = requests.get(
#         f"{base_url}/manga/{id}/feed",
#         params={"translatedLanguage[]": languages},
#     )
#     get_data = r.json()["data"]
#     for i in range(len(get_data)):
#         a.append([ get_data[i]["id"], get_data[i]['attributes']['chapter']])
#     return a

def dowloading_bar(i, total):
    bar = "#" * i + "-" * (total - i)
    percentage = (i / total) * 100
    sys.stdout.write(f"\r[{bar}] {percentage:.1f}% ")
    sys.stdout.flush()
    time.sleep(0.05)

def download_manga_chapter(chapter_id, save_path):
    url = f"https://api.mangadex.org/at-home/server/{chapter_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        base_url = "https://uploads.mangadex.org/data/"
        chapter_hash = data['chapter']['hash']
        page_filenames = data['chapter']['data']
        file_ext = page_filenames[0][-3:]

        for i in range(len(page_filenames)):
            image_url = f"{base_url}/{chapter_hash}/{page_filenames[i]}"
            if i < 9:
                download_image(image_url, os.path.join(save_path, f"0{i+1}.{file_ext}"))
            else:
                download_image(image_url, os.path.join(save_path, f"{i+1}.{file_ext}"))
            dowloading_bar(i+1, len(page_filenames))
        print("Done!")

    else:
        print(f"Failed to fetch chapter {chapter_id}")

def download_image(url, path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, required=True, help="Url of the chapter of manga")
    parser.add_argument("-d", "--dir", type=str, required=True, help="Chapter save path")
    args = parser.parse_args()
    url = args.url.replace("https://mangadex.org/chapter/", "")
    path = args.dir.replace(" ", "_")
    save_path = f"./{path}"
    os.makedirs(save_path, exist_ok=True)
    download_manga_chapter(url, save_path)
