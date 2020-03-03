import logging
import requests
import os
import threading
from datetime import datetime

def download_gambar(url=None,name = None):
    if (url is None):
        return False
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = name
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi},Diunduh pada waktu = {current_time} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    threads = []
    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg','gambar1',))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=('https://img.antaranews.com/cache/800x533/2020/01/27/grafik_20200127071108_1.png', 'gambar2',))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQDEt8ShL-rT569PnbWaGgKE0yuyPTqNAH2RpYnAYdo-VAgiwdv','gambar3',))
    threads.append(t)

    for thr in threads:
        thr.start()
