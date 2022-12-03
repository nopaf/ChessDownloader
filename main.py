# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import zipfile
import io


def download_and_extract(link1, i, link2, folder_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(link1 + str(i) + link2, headers=headers)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./" + folder_name)


def download_all_theweekinchess_zips():
    # "https://theweekinchess.com/zips/twic1448g.zip"
    link1 = "https://theweekinchess.com/zips/twic"
    link2 = "g.zip"
    for i in range(920, 1463):
        download_and_extract(link1, i, link2, 'pngs')


def download_theweekinchess_next_pgn(start_week, end_week, folder_name):
    link1 = "https://theweekinchess.com/zips/twic"
    link2 = "g.zip"
    # if end_week - start_week > 0:
    for i in range(start_week, end_week):
        download_and_extract(link1, i, link2, 'new_png')
    else:
        download_and_extract(link1, start_week, link2, 'new_png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # download_all_theweekinchess_zips()
    download_theweekinchess_next_pgn(1464, 1464, 'new_pngs')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
