# TUGAS 1
### Isnaini Nurul KurniaSari-05111740000010
* Menjalankan server server di 3 server yang berbeda dengan ip lain **(10.151.252.191)**, dengan masing-masing client connect ke server tersebut:
  
  - Kondisi awal server dengan port **(31000, 31001, 31002)**
    1. Port 31000 
        - server menunggu client
            ![server_menunggu_client1](https://user-images.githubusercontent.com/36990780/75626072-dca36680-5bf6-11ea-96d9-83bba804dce6.jpg)
        - client mengirim paket ke server
            ![client1 mengirim paket](https://user-images.githubusercontent.com/36990780/75626110-27bd7980-5bf7-11ea-98f9-641c3dc39a83.jpg)
        - server berhasil menerima paket dari client
            ![server1 menerima paket client1](https://user-images.githubusercontent.com/36990780/75626132-5a677200-5bf7-11ea-9857-12ed44c4f022.jpg)
            
     2. Port 31001
        - server menunggu client
          ![server 2 menunggu client2](https://user-images.githubusercontent.com/36990780/75626197-03ae6800-5bf8-11ea-8c88-c74b58e6e95d.jpg)
        - client mengirim paket ke server
          ![client 2 mengirim paket ke server2](https://user-images.githubusercontent.com/36990780/75626189-e11c4f00-5bf7-11ea-914f-c0418d30c183.jpg)
        - server menerima paket dari client
          ![server2 menerima paket client2](https://user-images.githubusercontent.com/36990780/75626203-17f26500-5bf8-11ea-8bf4-2df3246e393e.jpg)
          
     3. Port 31002
        - server menunggu client
          ![server3 menunggu client3](https://user-images.githubusercontent.com/36990780/75626223-67d12c00-5bf8-11ea-94c0-bf1f42afd95e.jpg)
        - client mengirim paket ke server
          ![client3 mengirim paket ke server3](https://user-images.githubusercontent.com/36990780/75626233-74ee1b00-5bf8-11ea-8740-8165290da3d4.jpg)
        - server berhasil menerima paket dari client
          ![client3 mengirim paket ke server3](https://user-images.githubusercontent.com/36990780/75626240-82a3a080-5bf8-11ea-8c7b-66120061bdfe.jpg)
 
 
### TUGAS 1A ###
Soal : MODIFIKASILAH program client.py dan server.py agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a)      
* Server dijalankan di komputer yang berbeda, client mencoba untuk mengirimkan file :
* Kondisi awal server di komputer yang berbeda dengan port 31001 **(ip= 10.151.252.191)**
          <img width="427" alt="gambar1" src="https://user-images.githubusercontent.com/36990780/75674556-e6d96980-5cb7-11ea-8419-ff42f2112486.png">
* Direktori ketika server belum menerima file
          <img width="427" alt="gambar1" src="https://user-images.githubusercontent.com/36990780/75673920-a3323000-5cb6-11ea-83de-4393112f5d22.png">
* server menunggu client
          ![1a_server menunggu client](https://user-images.githubusercontent.com/36990780/75626323-386eef00-5bf9-11ea-9fa6-4002444f32e8.jpg)
* client mengirimkan paket ke client 
      ![1a_client mengirim paket ke server](https://user-images.githubusercontent.com/36990780/75626347-7ec44e00-5bf9-11ea-85e1-b867390da108.jpg)
* server berhasil menerima paket dari client
      ![1a_client mengirim paket ke server](https://user-images.githubusercontent.com/36990780/75626347-7ec44e00-5bf9-11ea-85e1-b867390da108.jpg)
* Direktori ketika server sudah menerima file
    <img width="436" alt="gambar2" src="https://user-images.githubusercontent.com/36990780/75681581-7423ba80-5cc6-11ea-9dc4-96b030b5f541.png">
      
### TUGAS 1B ###
Soal : MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b)
* Server dijalankan di komputer yang berbeda, client mencoba untuk mengirimkan file :  
* Kondisi awal server di komputer yang berbeda dengan port 31001 **(ip= 10.151.252.191)**
* Direktori ketika server belum menerima file
      
      <img width="427" alt="gambar1" src="https://user-images.githubusercontent.com/36990780/75674351-7599b680-5cb7-11ea-93f7-dc36814ca2b3.png">
* server menunggu client
      ![1b_server menunggu client](https://user-images.githubusercontent.com/36990780/75674491-b5609e00-5cb7-11ea-8a2f-140a3113c081.jpg)
      3. client mengirimkan paket ke client
      ![1b_client mengirim paket ke server](https://user-images.githubusercontent.com/36990780/75674231-41be9100-5cb7-11ea-9132-41e9a2d950d9.jpg)
      4. server berhasil menerima paket dari client
      ![1b_server menerima paket ke client](https://user-images.githubusercontent.com/36990780/75674261-4daa5300-5cb7-11ea-909f-7a2fb3317fee.jpg)
      5. Direktori ketika server sudah menerima file
      
      <img width="436" alt="gambar2" src="https://user-images.githubusercontent.com/36990780/75674427-9235ee80-5cb7-11ea-84d7-d5b7ba6d04e3.png">

       
      
   
  
    
    

      
      
      
    



         
    

