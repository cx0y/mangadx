import os
import requests
#import json

def get_manga_id(manga_name):
    base_url = "https://api.mangadex.org"
    r = requests.get(
        f"{base_url}/manga",
        params={"title": manga_name}
    )
    if r.status_code == 200:
       #print(r.json())
       title = r.json()["data"][0]["attributes"]["title"]["en"].replace(" ", "_")
       #alltitle = r.json()["data"][0]["attributes"]["altTitles"]
       #print(json.dumps(r.json()["data"][0]["attributes"], indent=4))
       a = [manga["id"] for manga in r.json()["data"]][0]
       return [a,title]
    else:
        print("Manga Not Found")

def get_chapters(id):
    base_url = "https://api.mangadex.org"
    languages = ["en"]
    a = []
    r = requests.get(
        f"{base_url}/manga/{id}/feed",
        params={"translatedLanguage[]": languages},
    )
    get_data = r.json()["data"]
    for i in range(len(get_data)):
        a.append([ get_data[i]["id"], get_data[i]['attributes']['chapter']])
    return a

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
            download_image(image_url, os.path.join(save_path, f"{i+1}.{file_ext}"))
            print(f"... img {i+1}")
    else:
        print(f"Failed to fetch chapter {chapter_id}")

def download_image(url, path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

if __name__ == "__main__": 
      #manga_name = "beat and motion"
      #manga_id = get_manga_id(manga_name)
      #print(manga_id[1])
      #chap_list = get_chapters(manga_id[0])
      #print(chap_list[0][0])
      #save_path = "./manga"
      #os.makedirs(save_path, exist_ok=True)
      #download_manga_chapter("51e47658-3d0f-43bd-91fa-ccaac1e21fc8", save_path)
      #for i in range(len(chap_list)):
      #    next_path = save_path + f"/chap{i}"
      #    os.makedirs(next_path, exist_ok=True)
      #    download_manga_chapter(chap_list[i][0], save_path)
      #print("Done")
      url = input("Enter Chapter Url:").replace("https://mangadex.org/chapter/", "")
      path = input("Save Path:").replace(" ", "_")
      save_path = f"./{path}"
      os.makedirs(save_path, exist_ok=True)
      download_manga_chapter(url, save_path)
