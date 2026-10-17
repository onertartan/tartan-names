# rp1-r3 attempt 2 — D-20 bekleme noktası

**Tam koşu başlatılmadı. Ayrı PI onayı bekleniyor.**

Hazırlanma zamanı (UTC): `2026-10-16T17:14:00.317770+00:00`. D-20 SHA256: `778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2`.

- Attempt-2 harness SHA256: `9ff48dbe6a5fdb6e4ae9d1952f1f7ecaba553eb84ef4e2a60de0be8258e8f96e`.
- Değişen W-3 yazıcısı SHA256: `822560025b80920431998005b647076348f4e3026546e42a852718ea1f082891`.
- C-3 sınıfları: NEW=39, PIN=23, HISTPATH=43, TEXT=73. Bekleyen HISTPATH restorasyonu=0.
- C-5: tarihsel karşılaştırmada yeni fark=0; Q4 10/10, Q5 51/51, Q6 23/23, RRS 2/2.
- Ayrı RRS koşusu=2/2; kontrol kopyasında W-3 pinleri=52/52.
- C-6: main dahil 108 fonksiyonun AST kaynak bölümü attempt-1 ile aynı. Gate tools, teknik testler ve launcher baytları korunuyor. Hiçbir expectation/declaration değişmedi.

C-3'teki iki gerçek F1 girdi yolu için dosya hash'i **NOT OBSERVED**: açık okuma/hash yasağı nedeniyle bu girdiler açılmadı. Kaynak literal karşılıkları listelenmiştir. Ayrıntılar C3_literal_listing.json içindedir.

Attempt-1'den kalan 15 TEXT farkı C-3 listesinde işaretlidir; bu açıklamalar düzeltilmedi. Carried kayıtların yanlış görünen eski açıklama metinleri de korunur; gerçek pin yolları ve hash'leri C-1'e göre doğrudur.

W-3 testi yalnız metadata dosyalarından oluşan ayrı kontrol kopyasında çalıştı. Ürettiği test custody dosyası aktif alana veya store'a alınmadı. Aktif attempt-2 W-3/launch kaydı ve store yok. Eski otomatik controller bu hazırlıkta çalıştırılmadı ve attempt-2 launch yöntemi olarak seçilmedi.

Tarihsel karşılaştırmada teslim edilmiş sonuçların karşılaştırmadan sonra eklenen alanlarına ait 25 önceki fark ayrıca kaydedildi; tam exception metninin getirdiği yeni fark yok. Son tam koşunun gerçek 0 U koşulunun yerine bu kontrol konmuyor.

C-5 ham test çıktıları dış kontrol dizinlerinde korunuyor; burada sonuç kayıtları, kod hash'leri ve yürütme custody kayıtları teslim ediliyor. Bilimsel sonuç dosyasına, test_evidence teslimatına veya store'a hiçbir kontrol çıktısı aktarılmadı.

**Onay kapsamı:** changed_file_hashes.csv tüm uygulama/girdi/kayıt değişikliklerini ve sidecar hash'lerini; all_code_hashes.csv değişmeyenler dahil yürütülen kod hash'lerini verir. Diff'lerin kendileri ve üretilmiş paket indeksleri manifestte hash'lenir; kendi diff'leri üretilmez. Her diff hunk'ının tek D-20 etiketi vardır.

Bu bekleme noktasından sonra dosyalarda bir bayt değişirse yeni bekleme noktası gerekir. Tam koşu, bu harness ve diğer değişen dosya hash'lerini adlandıran ayrı PI onayı olmadan başlamaz. Commit/push yapılmadı; defterde madde kapatılmadı.
