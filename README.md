# Data Science SQL Project - VIEWS AND WITH 

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
4. Sipariş ve ürün detaylarını birleştirerek toplam tutar (price * quantity) hesapla. WITH kullanarak yap.
5. En pahalı ürünü almış kişinin full name değerini döndüren sorguyu yazınız.
6. Sipariş durumu 'completed' olanlar 'Tamamlandı', 'cancelled' olanlar ise 'İptal Edildi' şeklinde değiştirilip, order_id, status ve status_description kolonlarını dönen sqli yazınız.
7. Ortalama fiyatın üzerindeki ürünleri bulunuz.(Sorgu sadece prodduct_name ve price kolonlarını dönsün)
8. Alışveriş sayısına göre en sadık müşterileri bulmak istiyoruz. Buna göre alışveriş sayısı 5'ten büyük olanlara 'Sadık Müşteri', 2 ile 5 arasında olanlara 'Orta Seviye' diğer müşterilere de 'Yeni Müşteri' diyecek şekilde tüm müşterilerin isimlerini ve ve bu yeni tagi 'customer_category' ismiyle dönen sorguyu yazınız.
9. Son 30 gün içinde sipariş veren müşterilerin isimlerini dönen sorguyu yazınız.
10. En çok sipariş verilen ürünü bulunuz.
11. Ürün fiyatlarına göre etiketleme yapmak istiyoruz. Fiyatı 1000'den fazla olan ürünler için 'Pahalı'. 500 ile 100 arasında olan ürünler 'Orta' diğer ürünler 'Ucuz'
olarak işaretleneceklerdir. Sorgu product_name,price ve yeni taglenmiş kısmı price_category ismiyle dönmelidir.
