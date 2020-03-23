from file import Dire
import json
import logging
import base64
'''
------ PROTOCOL FORMAT ------
string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter
------ FITUR ------
1. Upload File
   Untuk mengupload file ke folder 'file'
   Request : upload
   Parameter : namafile *spasi* isifile
   Response : jika berhasil -> ok
              jika gagal -> error
2. List File
   Untuk melihat list file di dalam folder 'file'
   Request : list
   Parameter: -
   Response: list file yang ada dalam folder 'file'
3. Download File
   Untuk mendownload file berdasarkan nama file
   Request : download
   Parameter : namafile yang ingin didownload
   Response: hasil download file
4. Jika command tidak dikenali akan merespon dengan ERRCMD
'''
p = Dire()
class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                file = cstring[2].strip()

                print(nama)
                print(file.encode())
                print("Masuk Upload")
                p.upload_data(nama,file.encode())
                print("Selesai Upload")
                print(nama)
               # print(file)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                print("masuk list")
                hasil = p.list_data()
                dict = {"status":"succes","data":hasil}
                return json.dumps(dict)
            elif (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                print("masuk")
                hasil = p.download_data(nama)
                return hasil[0]
            else:
                return "ERRCMD"
        except:
            return "ERROR"

if __name__=='__main__':
    pm = FileMachine()
    input = "pesan.txt"
    hasil = pm.proses("list")
    print(hasil)
