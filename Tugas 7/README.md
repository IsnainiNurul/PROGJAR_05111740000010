**TUGAS 7**
**Performance Test sederhana hanya bisa dilakukan di linux/unix based**
- Menggunakan apachebenchark, dengan command ab
- Mengetest server kita dengan : ab -n <jumlahrequest> -c <concurecy> http://127.0.0.1:10001/
- Dengan menggunakan parameter sebagai berikut :
  <table>
 	  <tr>
 		  <td> Nomor </td>
 		  <td> Jumlah request</td>
      <td> Konkurensi</td>
 	  </tr>
 	  <tr>
 		  <td> 1 </td>
 		  <td> 10 </td>
      <td> 1,5,10 </td>
 	  </tr>
    <tr>
      <td> 2 </td>
      <td> 50 </td>
      <td> 1,10,30,50 </td>
    </tr>
     <tr>
      <td> 3 </td>
      <td> 100 </td>
      <td> 1,10,50,100 </td>
    </tr>
   </table>
  Concurrency melambangkan user yang mengakses secara bersamaan, concurency berbeda dengan paralel, concurency adalah bagaimana satu resource dibagi ke sekian banyak request yang meminta layanan

- Sehingga diperoleh untuk hasil performance test 1:
  ![1](https://user-images.githubusercontent.com/36990780/79036263-d8546b00-7bf0-11ea-8c34-6e8d1c325a33.png)
  ![1_lanjutan](https://user-images.githubusercontent.com/36990780/79036268-e1453c80-7bf0-11ea-90b7-0cf43085668b.png)

- Sehingga diperoleh untuk hasil performance test 2 :
  ![2](https://user-images.githubusercontent.com/36990780/79036275-f1f5b280-7bf0-11ea-90ca-780186ebd56b.png)
  ![2_lanjutan](https://user-images.githubusercontent.com/36990780/79036279-f9b55700-7bf0-11ea-8961-dbb575c16dc8.png)
  
- Sehingga diperoleh untuk hasil performance test 3 :
  ![3](https://user-images.githubusercontent.com/36990780/79036285-0afe6380-7bf1-11ea-9dbb-6c60d5e31ea1.png)
  ![3_lanjutan](https://user-images.githubusercontent.com/36990780/79036289-13569e80-7bf1-11ea-9270-8f88f6395a15.png)
