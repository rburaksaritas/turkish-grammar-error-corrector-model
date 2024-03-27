from utils.extract_sentences import separate_sentences
from generators.de_da_te_ta_generator import process_sentences

# Example text
text = """Giriş bölümünde kelime işlemeyle ilgili bahsedilen çalışmaların yanında, cümleden anlam ve duygu çıkarılabilmesine yönelik çalışmalar da günümüzde ihtiyaç haline gelmiştir. İnsanlar giderek makinelerle daha fazla etkileşime girmektedir. Alpaslan Burak Eliaçık ve Nadia Erdoğan bu makalede anlatılan çalışmaya benzer duygu analizi çalışmasından bahsetmişlerdir[7]. Bu çalışmaya göre duygu sınıflandırması yöntemi iki ana dala ayrılmaktadır; makine öğrenmesi tabanlı yaklaşım ve sözlük tabanlı yaklaşım. Makine öğrenme tabanlı yaklaşım sınıflandırma sırasında makine öğrenme algoritmalarını ve dilbilimsel özellikleri kullanmaktadır. Sözlük tabanlı yaklaşım ise sınıflandırma sırasında önceden hazırlanmış duygu kavramlarından oluşan sözlüklerden yararlanmaktadır. Bazı çalışmalarda ise bu iki yönelimin melez bir yaklaşımı kullanılmaktadır.
Makinelerle insanların etkileşiminin önemi filmler aracılığıyla da görülmektedir. Makinelerle insanlar arasındaki savaş veya makinelerle insanların sesli iletişim kurduğu filmler oldukça ilgi çekmektedir. İlerleyen zamanlarda belki de insanlar için makineler birer arkadaş yerinde geçebilecektir. Bunun gerçekleşebilmesi için cümlenin ifade ettiği duyguyu bulabilmek gerekir.
Karar destek sistemleri, günümüzde önemli bir konu olmuştur. Tıp alanından örnekler verilebilir. “Tıbbi Karar Destek Sistemlerinin Yöntemsel Olarak Değerlendirilmesi Üzerine Bir Çalışma[8]” adlı makalede değişik hastalık tanılarına ilişkin olarak geliştirilmiş tıbbi karar destek sistemlerinin, içerdiği teknikler açısından incelemesi yapılmış ve bu tekniklerin performansları değerlendirilmiştir.
Cümlelerin işlenebilmesi karar destek sistemleri oluşturma konusuna da yardımcı olacaktır. Cümlelerden oluşan metinleri, cümleden çıkarılan anlama göre işleyebilen sistemler, istenilen alanda hem analitik sonuçlar elde etmeye yarayacak hem de gelecekle ilgili yapılacak tahminlere olanak sağlayacaktır."""

# Split the sentences
original = separate_sentences(text)

# Generate variations
modified = process_sentences(original)

# Display both original and transformed sentences
for i, (original, transformed) in enumerate(zip(original, modified), start=1):
    print(f"Sentence {i} (I): {original.strip()}")
    print(f"Sentence {i} (O): {transformed.strip()}")
    print()
