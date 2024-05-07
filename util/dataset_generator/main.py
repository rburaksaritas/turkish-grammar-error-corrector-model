from utils.extract_sentences import separate_sentences
from generators.de_da_te_ta_generator import process_sentences as ps1
from generators.mi_mu_generator import process_sentences as ps2
from utils.sentences_to_csv import create_csv, append_to_csv
from utils.shuffle_data import shuffle_data

# Example text
text = """Giriş bölümünde kelime işlemeyle ilgili bahsedilen çalışmaların yanında, cümleden anlam ve duygu çıkarılabilmesine yönelik çalışmalar da günümüzde ihtiyaç haline gelmiştir. İnsanlar giderek makinelerle daha fazla etkileşime girmektedir. Alpaslan Burak Eliaçık ve Nadia Erdoğan bu makalede anlatılan çalışmaya benzer duygu analizi çalışmasından bahsetmişlerdir[7]. Bu çalışmaya göre duygu sınıflandırması yöntemi iki ana dala ayrılmaktadır; makine öğrenmesi tabanlı yaklaşım ve sözlük tabanlı yaklaşım. Makine öğrenme tabanlı yaklaşım sınıflandırma sırasında makine öğrenme algoritmalarını ve dilbilimsel özellikleri kullanmaktadır. Sözlük tabanlı yaklaşım ise sınıflandırma sırasında önceden hazırlanmış duygu kavramlarından oluşan sözlüklerden yararlanmaktadır. Bazı çalışmalarda ise bu iki yönelimin melez bir yaklaşımı kullanılmaktadır.
Makinelerle insanların etkileşiminin önemi filmler aracılığıyla da görülmektedir. Makinelerle insanlar arasındaki savaş veya makinelerle insanların sesli iletişim kurduğu filmler oldukça ilgi çekmektedir. İlerleyen zamanlarda belki de insanlar için makineler birer arkadaş yerinde geçebilecektir. Bunun gerçekleşebilmesi için cümlenin ifade ettiği duyguyu bulabilmek gerekir.
Karar destek sistemleri, günümüzde önemli bir konu olmuştur. Tıp alanından örnekler verilebilir. “Tıbbi Karar Destek Sistemlerinin Yöntemsel Olarak Değerlendirilmesi Üzerine Bir Çalışma[8]” adlı makalede değişik hastalık tanılarına ilişkin olarak geliştirilmiş tıbbi karar destek sistemlerinin, içerdiği teknikler açısından incelemesi yapılmış ve bu tekniklerin performansları değerlendirilmiştir.
Cümlelerin işlenebilmesi karar destek sistemleri oluşturma konusuna da yardımcı olacaktır. Cümlelerden oluşan metinleri, cümleden çıkarılan anlama göre işleyebilen sistemler, istenilen alanda hem analitik sonuçlar elde etmeye yarayacak hem de gelecekle ilgili yapılacak tahminlere olanak sağlayacaktır."""

text2 = """Gece çok mu geç oldu, gökyüzüne bakıp yıldızları saymak için sessizce dışarı çıktın mı, etraf bu kadar sessizken içinde bir huzur mu buluyorsun, 
yoksa yalnızlık mı hissediyorsun? Ay ışığı altında dolaşırken, eski zamanlardaki gibi mektup yazmayı düşündün mü hiç, kelimelerin kağıda dokunuşu seni 
heyecanlandırır mı, yoksa bu eski moda bir yöntem mi geldi sana? Günümüzde elektronik postalar ve anlık mesajlarla iletişim kurmak çok mu kolay, bu yüzden mi 
gerçek bağlantıları kurmakta zorlanıyoruz, insanlar arasındaki samimiyet azaldı mı sence de? Teknoloji ilerledikçe, doğaya dönmek, ormanlarda yürüyüş yapmak, 
denizin kenarında oturmak, daha çok mu anlam kazanıyor, insan ruhu aslında sakinlik ve huzur mu arıyor? Şehir hayatının koşuşturması, stresi, gürültüsü seni de 
bunaltıyor mu, arada sırada kırsal kesimde bir kaçamak yapmak, temiz hava almak, yıldızların altında bir gece geçirmek, içindeki huzuru yeniden mi bulmana 
yardımcı oluyor? Yoksa sen, bu koşuşturmacanın içinde bir denge mi buldun, şehrin enerjisinden, hızından, dinamizminden güç alıyor musun, bu hızlı tempo senin 
doğan mı, yoksa ara sıra mola vermek, yavaşlamak, etrafına bakmak, yaşamı derinlemesine hissetmek istiyor musun?"""

text3 = """Gelecek hafta sonu için hava tahminleri güncellendi mi, yoksa hala değişken mi? Arkadaşlarla buluşmak için hangi gün uygun, cuma mı, yoksa cumartesi mi? 
Piknik için gideceğimiz yer belirlendi mi, yoksa hala kararsız mıyız? Yemeği kimin yapacağına karar verdik mi, yoksa hala kararsız mıyız? Alışveriş için ne 
alacağımızı listeledik mi, yoksa spontane mi bir alışveriş yapacağız? Araba yolculuğu için kimin arabasını kullanacağımıza karar verdik mi, yoksa hala tartışma mı 
içindeyiz? Yolda mola verecek miyiz, yoksa direkt mi gitmeyi planlıyoruz? Hava nasıl olacak diye sürekli kontrol ediyor muyuz, yoksa sadece güneşli mi olacak diye 
umut ediyoruz? Varış noktasına vardığımızda herkesin keyfi yerinde mi, yoksa yorgun mu? Hava kararınca ateş yakıp etrafında oturmayı planladık mı, yoksa başka bir 
aktivite mi düşünüyoruz? Gece kamp kuracak mıyız, yoksa otel mi tercih edeceğiz? Sabah kahvaltı için ne yiyeceğimize karar verdik mi, yoksa spontane mi karar 
vereceğiz? Geri dönerken trafik olacak mı, yoksa rahat mı bir yolculuk yapacağız? Araba mı kullanacağız, yoksa yürüyerek mi gideceğiz? Deniz kenarında mı tatil 
yapmalıyız, yoksa dağlarda mı? Klasik tarzı mobilyalar mı tercih etmeliyiz, yoksa modern olanları mı? Kışın mı doğum günümüzü kutlamalıyız, yoksa yazın mı?
 Hangi renk duvar kağıdını seçmeliyiz, yoksa desenli mi olmalı? Evde mi yemek yemeliyiz, yoksa dışarıda mı? Tatlı mı atıştırmalıkları tercih etmeliyiz, yoksa 
 tuzlu mu? Film mi izlemeliyiz, yoksa kitap mı okumalıyız? Dijital mi kitapları tercih etmeliyiz, yoksa basılı mı? Klasik müzik mi dinlemeliyiz, yoksa pop 
 müzik mi? Tatil için sahil mi tercih etmeliyiz, yoksa dağlar mı? Akşam yemeği olarak balık mı yemeliyiz, yoksa tavuk mu? Spor yaparken açık havada mı olmalıyız, 
 yoksa kapalı alanda mı?
"""

text4 = """Gökyüzü her zaman bu kadar mavi mi? Sen de bu kitabı çok seviyor musun? Bu filmi izlerken gözyaşlarını tutabildin mi? Bahçedeki çiçekler ne zaman açtı? 
Deniz her zaman bu kadar mı güzel? Yeni açılan kafeyi sen de beğendin mi? Akşam yemeğinde ne yemeyi düşünüyorsun? O şarkıyı dinlerken hüzünleniyor musun? 
Bu oyunu oynarken zamanın nasıl geçtiğini hissediyor musun? Yıldızları izlerken kendini kaybediyor musun? Bu kadar çok kitap okumak seni yoruyor mu? Kahve 
içmek günün en güzel anı mı? O şiiri okurken duygulandın mı? Yeni telefonun beklentilerini karşılıyor mu? Spor yapmak seni daha enerjik mi yapıyor? Resim yaparken 
renklerle oynamaktan hoşlanır mısın? Yeni bir dil öğrenmek seni heyecanlandırıyor mu? Sabahları erken kalkmak zor mu geliyor? Akşamları dışarı çıkmak hoşuna 
gidiyor mu? Hafta sonları ne yapmayı tercih edersin? Seyahat etmek senin için bir tutku mu? Yemek yaparken yeni tarifler denemeyi sever misin? Kitap okurken 
kahve eşlik etmesi şart mı? Müzik dinlerken genellikle ne tür şarkılar seçersin? Arkadaşlarınla vakit geçirmek seni mutlu eder mi? Hava sıcak mı sıcak, serin bir 
gölge aramak lazım!
Kahve demlendi mi, bir fincanın keyfine varırız.
Kitap güzel mi güzel, bir solukta bitiverir.
Film sürükleyici mi sürükleyici, gözlerimi ekrandan alamadım.
Müzik ritmik mi ritmik, ayaklarım kendiliğinden dans ediyor.
Yemek lezzetli mi lezzetli, tabakları sıyırırız.
Akşam serin mi serin, hafif bir hırka gerek.
Çocuklar mutlu mu mutlu, parkta koşturup duruyorlar.
Deniz soğuk mu soğuk, ayaklarımızı bile sokmak istemeyiz.
Oyun heyecanlı mı heyecanlı, kalbim duracak gibi.
Manzara güzel mi güzel, fotoğraflamadan edemeyiz.
Tatil dinlendirici mi dinlendirici, tüm yorgunluğumuzu attık.
Kitaplık dolu mu dolu, yeni bir kitap için yer yok.
Bahçe yeşil mi yeşil, her köşesi ayrı bir cennet.
Pasta tatlı mı tatlı, şekerimiz fırlayacak neredeyse.
Gece sessiz mi sessiz, yaprak kımıldamıyor.
Kış soğuk mu soğuk, evden çıkmak istemezsin.
Yaz sıcak mı sıcak, gölgede durmak bile yetmiyor.
Sonbahar hüzünlü mü hüzünlü, yapraklar yavaşça düşüyor.
İlkbahar renkli mi renkli, her yan çiçek açmış.
Şehir kalabalık mı kalabalık, adım atacak yer yok.
Orman sessiz mi sessiz, sadece kuş sesleri duyuluyor.
Yol uzun mu uzun, gitmek gitmek bitmiyor.
Film uzun mu uzun, ara vermeden izlenmez.
Şarkı hüzünlü mü hüzünlü, gözyaşlarımızı tutamıyoruz."""


# # Split the sentences
# correct = separate_sentences(text)

# # Generate variations
# wrong = ps1(correct)

# # Display both original and transformed sentences
# for i, (correct_s, wrong_s) in enumerate(zip(correct, wrong), start=1):
#     print(f"source {i}: {wrong_s.strip()}")
#     print(f"target {i}: {correct_s.strip()}")
#     print()

# create_csv(wrong, correct, "dataset/de_da_te_ta_errors.csv")

# text = open("dataset/mixed_errors.csv", "r").read()
# wrong = separate_sentences(text)
# create_csv(wrong, wrong, "dataset/mixed_errors.csv")

# shuffle_data("dataset/mixed_errors.csv", "dataset/mi_mu_errors.csv")