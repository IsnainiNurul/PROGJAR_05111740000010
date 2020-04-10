**Tugas 6**
- Membuat multithread server, dengan membuka port 10001 di ip adress 127.0.0.1, dengan ketentuan yaitu :
- Dapat melayani request dalam bentuk string seperti (GET spasi / spasi HTTP/1.0)
- Tanda akhir request adalah "\r\n\r\n"
- Jika tanda akhir request diterima, maka balas dengan string <h1>SERVER HTTP</h1>
- Mencoba dengan telnet pada port 10001, dengan cara mengirimkan string GET<spasi>/<spasi>HTTP/1.0<enter><enter> Harusnya mereply dengan yang sama pada point nomor 4
- Membuka chrome web browser, aktifkan developer mode, bagian network
- Membuka alamat http://127.0.0.1:10001
  
  **Penjelasan :**
- Menjalankan program server_thread_http.py
  ![server_thread_py](https://user-images.githubusercontent.com/36990780/79015124-618a8400-7b96-11ea-834a-4973269acf6e.png)
- Menjalankan program http.py
  ![httpnya](https://user-images.githubusercontent.com/36990780/79015233-94cd1300-7b96-11ea-8971-3e7803866e26.png)
- Membuka chrome web browser dan mengaktifkan developer mode pada bagian network kemudian membuka alamat http://127.0.0.1:10001
  ![server http](https://user-images.githubusercontent.com/36990780/79015295-b0381e00-7b96-11ea-8e8f-f5bb6c072ee9.png)
  

