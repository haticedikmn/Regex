# Regex <br>
## Regex ile Titanic Veri Setini Düzenleme :sunglasses: <br>

> #### Merhaba arkadaşlar bu projemde regex ile Titanic veri setinde ki Name ,Sex ve Age değişkenlerini veri setinden çekerek yeni bir csv dosyasına atadım. :cowboy_hat_face:
> Hadi gelin hep beraber regex nedir ve nasıl kullanılır ona bakalım ...

<img src="https://miro.medium.com/max/1400/0*vK6oDAIRqPo-xjFY" align="center" widht="400" height="250" >

## Regex Nedir ?
#### Regular Expressions (düzenli ifadeler; kısaca regex veya regexp)
- Bir metin içerisinden belirli kurallara uyan alt metinler elde etmek için kullanılan bir dildir. <br>
- Pattern(desen,kalıp) olan string verilerden karmaşık code refactoring işlemlerine kadar, Regex’in çok çeşitli kullanım alanları vardır. <br>
## Pattern Nedir ? <br>
-Gelen datanın belirli bir yapısı olması gerekir. <br>
-Kitap cümleleri gibi string verilerde herhangi bir pattern bulunmaz. <br>
## Patterns 

##### Aşağıdaki karakterler regex söz dizimi (syntax) içerisinde kullanılan özel karakterlerdir.
### Metacharacter <br>

- **"+" Bir önündeki ifadenin en az 1 defa ve daha fazla yakalanmasını sağlar.**

- **"-" Aralık belirtmede kullanılır**

- **"*" Hiç olmayabilir veya birden fazla tekrarlı kullanım**

- **"[]" Liste oluşturur. Listenin içindeki ifadeleri yakalar**

- **"{1,3}" Bir önündeki ifadenin en az ve en çok kaç defa yakalanmasını ifade eder {en az=1 , en 
çok=3**

- **"(?<=)"  Eşittir işaretinden sonra hangi karakter yada kelimeyi yazarsanız, oraya kadar 
yakalar ve imleci son karakterin sağ tarafına getirir**

- **"[^ ]" Tersi, negatifi anlamındadır**

- **"\" Kaçış karakteri**

- **"?" Opsiyonel (0 veya 1 kez tekrarlı) kullanım**

- **"." Boşluk olmayan tüm karakterler**

- **"$" Satır sonu**

- **"|" veya**

### Yazılmayan Karakterler

- **"\n" satır sonu (new line)**

- **"\r" satır kesme (break)**

- **"\t" sekme boşluk (tab)**

- **"\b" kelime sınırı (word boundary)**

### Tekrar Sayısı

- **"?" opsiyonel (0 veya 1 kez) kullanım**

- **"+" en az bir kez veya daha fazla kullanım**

- **"*" hiç olmayabilir veya birden fazla kullanım**

### Kısa Tanımlar

- **"\w" a dan z ye, A dan Z ye, 0123456789, _ karakterlerini yakalar [ a-zA-Z0-9_ ]**
- **"\W" a dan z ye, A dan Z ye, 0123456789, _ karakterleri hariç diğer karakterleri yakalar**
- **"\s" Boşluk, tab ve yeni satır karakterlerini yakalar [space\t\r\n]**
- **"\S" Boşluk, tab ve yeni satır karakterleri hariç yakalar [^space\t\r\n]**
- **"\d" Rakamları yakalar [0-9]**
- **"\D" Rakam olmayanları yakalar [^0-9]**

- **"[\d\D]" Digit yada digit olmayan yani noktanın yakalayamadığı yeni satır karakterini de 
yakalar**

> ### Regex hakkında bilgimiz oldu şimdi Titanic veri setinde ki Name ,Sex ve Age değişkenlerini veri setinden çekerek yeni bir csv dosyasına atama işlemini beraber yapalım.

1- İlk olarak işlem yapacağımız veri setinden veri örneğimizi alıyoruz .[regex.101](https://regex101.com/) sitesine giderek verimizi yapıştırarak regex komutlarıyla alt metinlerimizi
oluşturuyoruz . <br>

<img src="https://github.com/haticedikmn/Regex/blob/main/picture/regex1.png" align="center" widht="600" height="350" >

2- Code generetor kısmından kod dosyamızı kopyalıyoruz . <br>

<img src="https://github.com/haticedikmn/Regex/blob/main/picture/regex2.png" align="center" widht="600" height="350" >

3- Pycharm açarak titanic.py adında bir pycharm dosyası oluşturup kodlarımızı yapıştırıyoruz. <br>

<img src="https://github.com/haticedikmn/Regex/blob/main/picture/regex3.png" align="center" widht="600" height="350" >

4- titanic_linebyline.py dosyamızda regex kısmına regex kodumuzu yazarak çalıştırıyoruz ve çektiğimi verilerin new_titanic.csv dosyasında oluştugunu göreceksiniz. <br>

<img src="https://github.com/haticedikmn/Regex/blob/main/picture/regex4.png" align="center" widht="400" height="250" >

<br />


### Bu yazımda sizlere Regex komutlarından bahsetmeye çalıştım. :writing_hand:
### Çalışmalarımı yakından takip etmek ve iletişime geçmek için:

[<img width="22" src="https://cdn.jsdelivr.net/npm/simple-icons@v7/icons/linkedin.svg" align="left" />][linkedin]


[<img width="22" src="https://cdn.jsdelivr.net/npm/simple-icons@v7/icons/medium.svg" align="left" />][medium] <br>

### Bir sonraki yazımda görüşmek üzere… 	:hearts:
### Teşekkürler! 🌺  




<br />
<br />


[linkedin]: https://www.linkedin.com/in/haticedikmen/
[medium]: https://medium.com/@haticedikmen

 

