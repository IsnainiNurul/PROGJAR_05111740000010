 *Berikut ini adalah Laporan Tugas 9 :*
  <a href="https://github.com/IsnainiNurul/PROGJAR_05111740000010/blob/master/Tugas%209/Laporan%20Tugas%209_Isnaini%20Nurul%20KurniaSari_05111740000010.pdf"> Laporan Tugas 9 Isnaini 05111740000010</a> 

 *Berikut ini adalah hasil Performance Test untuk Server Async*
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
   
   *Berikut ini adalah hasil Performance Test untuk Server Thread*
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
   
   **Kesimpulan**
   
   Dapat dlihat pada hasil performance test pada kedua macam tabel tersebut, server asynchronous lebih memiliki peforma yang lebih baik jika dibandingkan dengan server thread, maka dari itu server asynchronous bekerja lebih cepat jika dibandingkan dengan server thread.
