# Data Science SQL Project 1

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-project-2.

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

# Questions
1. Completed siparişlerin listesini gösteren bir VIEW oluştur.
2. Electronics kategorisindeki ürünleri gösteren bir VIEW oluştur.
3. Her müşterinin toplam harcamasını WITH kullanarak hesapla.
4. Sipariş ve ürün detaylarını birleştirerek toplam tutar (price * quantity) hesapla.
5. Email adresinde '@' karakteri olmayan müşterileri bul.
6. NULL email veya boş email adresi olan müşterileri bul.
7. Müşteri isimlerinden sadece soyisimleri çek. (SUBSTR, RIGHT kullanımı)
8. İsim ve email'i CONCAT ile birleştirip yeni bir kolon oluştur.
9. Price'ı CAST ile INTEGER yaparak listele.
10. Email içinde 'example' kelimesi geçmeyen müşterileri listele (STRPOS + COALESCE).
