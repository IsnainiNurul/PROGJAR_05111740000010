import shelve
import uuid
import socket
import os
import base64

class Dire:
    def __init__(self):
        if not os.path.exists("file"):
            os.makedirs("file")
    def upload_data(self,nama=None,file=None):

        makan = file
        print("halo")
        print(base64.decodestring(makan))
        f = open("file/"+nama,"wb")
        f.write(base64.decodestring(makan))
        print("asd")
        
        return True
    def download_data(self,nama=None):
        # ======Membaca file download =====
        are = []
        f = open("file/" + nama, "rb")
        l =f.read()
        f.close()
        print(l)
        hasil = base64.encodestring(l)
        print(hasil)
        are.append(hasil.decode())
        print(are)
        return are

    def list_data(self):
        file_list = os.listdir("file")
        f = []
        for filename in file_list:
            f.append(filename)
        return f
        
if __name__=='__main__':
    dire = Dire()
    input = "pesan.txt"
    
