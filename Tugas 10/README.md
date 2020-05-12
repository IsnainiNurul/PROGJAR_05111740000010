 **Laporan Tugas 10 :**
  <a href="https://github.com/IsnainiNurul/PROGJAR_05111740000010/blob/master/Tugas%2010/Laporan%20Tugas%2010_Isnaini%20Nurul%20KurniaSari_05111740000010.pdf"> Laporan Tugas 10 Isnaini 05111740000010</a> 
 <br>
 <br>

- Pull Update Terbaru
- Menjalankan async_server.py dengan port 9002, 9003, 9004, 9005 dengan menggunakan WSL <br> dengan perintah :<br>
 `python3 async_server.py 9002 & python3 async_server.py 9003 & python3 async_server.py 9004 & python3 async_server.py 9005 &`
    ![gambar1](https://user-images.githubusercontent.com/36990780/81701878-c76b7380-9494-11ea-85dd-8e4773fa7967.png)
 - Menjalankan file lb.py dan menjalankan di port 44444: <br> dengan perintah  <br>
 `python3 lb.py`
    ![gambar2](https://user-images.githubusercontent.com/36990780/81701888-c9353700-9494-11ea-82d6-af2d604b11b0.png)
 - Mengakses http://localhost:44444/page.html pada browser 
    ![gambar3](https://user-images.githubusercontent.com/36990780/81701891-c9cdcd80-9494-11ea-9733-7430ee0c6182.png)
 - Mengecek dan melihat proses di log program bahwa setiap request akan dilayani oleh backend secara bergantian
    <img width="1000" alt="gambar4" src="https://user-images.githubusercontent.com/36990780/81702770-e7e7fd80-9495-11ea-8a0b-d31b5fb2db98.png">

 - Melakukan performance test seperti tugas 9, dan membandingkan penggunaan antara load balancer dengan async_server dengan server_thread_http pada folder progjar Tugas5 <br> Dengan parameter sebagai berikut : <br> Jumlah request 	:  1000 <br> Konkurensi	:  1,50, 100,500,1000 <br>
 
 - **Berikut ini adalah hasil Performance Test untuk Asyncronus Server :**
 <table>
 	  <tr>
 		  <td> Nomor </td>
 		  <td> Concurrency level </td>
      <td> Time taken for test </td>
      <td> Complete request </td>
      <td> Failed request </td>
      <td> Total transferred </td>
      <td> Request per second </td>
      <td> Time per request </td>
      <td> Transfer rate </td>
 	  </tr>
 	  <tr>
 		  <td> 1. </td>
      <td> 1 </td>
 		  <td> 2.168 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes </td>
      <td> 461.26 [#/sec] (mean) </td>
      <td> 2.168  [ms] </td>
      <td> 54.95 [Kbytes/sec] </td>
 	  </tr>
    <tr>
      <td> 2. </td>
      <td> 50 </td>
      <td> 59.397 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes </td>
      <td> 16.84 [#/sec] (mean)</td>
      <td> 59.397 [ms] </td>
      <td> 2.01 [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 3.  </td>
      <td> 100 </td>
      <td> 59.985 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 16.84 [#/sec] (mean) </td>
      <td> 59.397 [ms] </td>
      <td>  2.01 [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 4.  </td>
      <td> 500 </td>
      <td> 60.406 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 16.55  [#/sec] (mean) </td>
      <td> 60.406   [ms] </td>
      <td>  1.97  [Kbytes/sec] </td>
    </tr>
      <tr>
      <td> 5.  </td>
      <td> 1000 </td>
      <td>  62.970  seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 15.88   [#/sec] (mean) </td>
      <td> 62.970    [ms] </td>
      <td>  1.89   [Kbytes/sec] </td>
    </tr>
   </table>
   <br>
   <br>
   
- **Berikut ini adalah hasil Performance Test untuk Multithread Server :**
 <table>
 	  <tr>
 		  <td> Nomor </td>
 		  <td> Concurrency level </td>
      <td> Time taken for test </td>
      <td> Complete request </td>
      <td> Failed request </td>
      <td> Total transferred </td>
      <td> Request per second </td>
      <td> Time per request </td>
      <td> Transfer rate </td>
 	  </tr>
 	  <tr>
 		  <td> 1. </td>
      <td> 1 </td>
 		  <td>  483.745 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td>  122000 bytes </td>
      <td> 2.07 [#/sec] (mean) </td>
      <td> 483.745 [ms] </td>
      <td> 0.25 [Kbytes/sec] </td>
 	  </tr>
    <tr>
      <td> 2. </td>
      <td> 50 </td>
      <td> 422.244 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes </td>
      <td> 2.37 [#/sec] (mean)</td>
      <td> 422.244 [ms] </td>
      <td> 0.28  [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 3.  </td>
      <td> 100 </td>
      <td> 492.146 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 2.03  [#/sec] (mean) </td>
      <td> 492.146 [ms] </td>
      <td>  0.24  [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 4.  </td>
      <td> 500 </td>
      <td> 471.756 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 2.12   [#/sec] (mean) </td>
      <td> 471.756 [ms] </td>
      <td> 0.25 [Kbytes/sec] </td>
    </tr>
      <tr>
      <td> 5.  </td>
      <td> 1000 </td>
      <td> 442.227 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 122000 bytes</td>
      <td> 2.26 [#/sec] (mean) </td>
      <td> 442.227 [ms] </td>
      <td> 0.27 [Kbytes/sec] </td>
    </tr>
   </table>
  <br> 
  <br>
   
   
  
 - **Berikut ini adalah hasil Performance Test untuk Asyncronus Server Dengan Load Balancer :**
 <table>
 	  <tr>
 		  <td> Nomor </td>
 		  <td> Concurrency level </td>
      <td> Time taken for test </td>
      <td> Complete request </td>
      <td> Failed request </td>
      <td> Total transferred </td>
      <td> Request per second </td>
      <td> Time per request </td>
      <td> Transfer rate </td>
 	  </tr>
 	  <tr>
 		  <td> 1. </td>
      <td> 1 </td>
 		  <td> 1.579  seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 0 bytes </td>
      <td> 633.48 [#/sec] (mean) </td>
      <td> 1.579 [ms] </td>
      <td> 0.00 [Kbytes/sec] </td>
 	  </tr>
    <tr>
      <td> 2. </td>
      <td> 50 </td>
      <td> 1.580 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 0 bytes </td>
      <td> 632.86 [#/sec](mean)</td>
      <td> 1.580 [ms] </td>
      <td> 0.00 [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 3.  </td>
      <td> 100 </td>
      <td> 1.614 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 0 bytes</td>
      <td> 619.41[#/sec] (mean) </td>
      <td> 1.614 [ms] </td>
      <td> 0.00 [Kbytes/sec] </td>
    </tr>
     <tr>
      <td> 4.  </td>
      <td> 500 </td>
      <td> 2.285 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 0 bytes</td>
      <td> 437.65 [#/sec] (mean) </td>
      <td> 2.285 [ms] </td>
      <td> 0.00 [Kbytes/sec] </td>
    </tr>
      <tr>
      <td> 5.  </td>
      <td> 1000 </td>
      <td> 1.698 seconds </td>
      <td> 1000 </td>
      <td> 0 </td>
      <td> 0 bytes</td>
      <td> 558.81 [#/sec] (mean) </td>
      <td> 1.698 [ms] </td>
      <td> 0.00 [Kbytes/sec] </td>
    </tr>
   </table>
  <br>
  <br>
  
   
   **Kesimpulan :**
   
   Dari ketiga table performance test diatas, dapat kita lihat bahwa asyncronus server yang menggunakan load balancer memproses lebih cepat jika dibandingkan dengan asyncronus server biasa dan multithread server yang menandakan bahwa performa asyncronus server lebih baik dibandingkan dengan asyncronus biasa dan multithread server. Load balancer bertugas untuk mendistribusikan request ke backend yag didefinisikan di class BackendList. Di dalam load balancer terdapat fungsi getserver pada class BackendList yang akan membuat backend dipilih secara round robin atau bergantian secara fair sehingga setiap request akan dilayani oleh backend yang bergantian. 
   
   
