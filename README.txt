========================================================================
🚀 SAP ABAP Deep Structure Generator (Python Tool)
========================================================================

Bu araç, karmaşık JSON verilerini analiz ederek SAP ABAP için gerekli olan:
1. Deep Structure (TYPES) tanımlarını,
2. /ui2/cl_json=>deserialize metodunu,
3. Otomatik Mapping tablosunu (30 karakter sınırı ve özel karakterler için)
otomatik olarak oluşturur.

------------------------------------------------------------------------
📂 KLASÖR İÇERİĞİ
------------------------------------------------------------------------
Bu klasörde şu 3 dosyanın olduğundan emin olun:
1. app.py              (Arayüz kodu)
2. json_to_abap.py     (Mantık kodu)
3. requirements.txt    (Gerekli kütüphane listesi)

------------------------------------------------------------------------
🛠️ ADIM 1: GEREKLİ PROGRAMLARIN KURULUMU
------------------------------------------------------------------------
Eğer bilgisayarınızda Python yüklü değilse:

1. https://www.python.org/downloads/ adresine gidin.
2. "Download Python" butonuna basıp indirin.
3. Kurulum dosyasını çalıştırın.
⚠️ ÇOK ÖNEMLİ: Kurulum ekranının en altında "Add Python to PATH" kutucuğu vardır.
   Bunu MUTLAKA işaretleyin. İşaretlemezseniz komutlar çalışmaz.
4. "Install Now" diyerek kurulumu tamamlayın.

(Editör olarak Visual Studio Code önerilir ama zorunlu değildir, Not Defteri ile bile kodlara bakabilirsiniz.)

------------------------------------------------------------------------
⚙️ ADIM 2: KÜTÜPHANELERİN YÜKLENMESİ (Sadece ilk seferde)
------------------------------------------------------------------------
Bu aracın çalışması için "Streamlit" kütüphanesine ihtiyacı vardır.

1. Bu klasörün içine girin (Dosya Gezgini'nde).
2. Adres çubuğuna (klasör yolunun yazdığı yere) "cmd" yazın ve Enter'a basın.
   (Siyah bir komut ekranı açılacaktır).
3. Açılan siyah ekrana şu komutu yapıştırın ve Enter'a basın:

   pip install -r requirements.txt

   (Ekranda yazılar akacak ve yükleme tamamlanacaktır. "Successfully installed..." yazısını görünce kapatabilirsiniz.)

------------------------------------------------------------------------
▶️ ADIM 3: UYGULAMAYI ÇALIŞTIRMA
------------------------------------------------------------------------
Her kullanmak istediğinizde:

1. Klasörün içinde tekrar "cmd" yazıp siyah ekranı açın (veya VS Code terminalini kullanın).
2. Şu komutu yazın ve Enter'a basın:

   python -m streamlit run app.py

3. Tarayıcınız otomatik olarak açılacak ve uygulama karşınıza gelecektir.
   Sol tarafa JSON yapıştırın, sağ taraftan hazır ABAP kodunu alın.

------------------------------------------------------------------------
❓ SORUN GİDERME
------------------------------------------------------------------------
S: "'pip' veya 'python' is not recognized..." hatası alıyorum.
C: Python kurarken "Add to PATH" kutucuğunu işaretlemeyi unuttunuz. Python'ı silip tekrar kurun ve o kutuyu işaretleyin.

S: requirements.txt dosyası yok veya hata veriyor.
C: Sorun değil, manuel olarak da yükleyebilirsiniz. Komut satırına şunu yazın:
   pip install streamlit

İyi günlerde kullanın!