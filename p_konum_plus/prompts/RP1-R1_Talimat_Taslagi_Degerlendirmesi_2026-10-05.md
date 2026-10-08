# RP1-R1 talimat taslağı değerlendirmesi

**Tarih:** 2026-10-05  
**İncelenen dosya:** `Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_2026-10-05.md`

**Talimat, üç ana bulgumu kapatabilecek düzeltmeleri içeriyor; ancak bu haliyle imzalanmasını önermiyorum.** Bazı hükümler yeni bir B veya STOP doğurabilir. Bunlar için yeni tasarım döngüsü değil, aynı taslakta dar düzeltme yeterli.

Dosyanın SHA256’sını hesapladım; sidecar ile eşleşiyor:

```text
53b7921409e6c1d779392b83af1d2e5f903311a17649f00873585acf03dc1276
```

**Üç ana bulgunun karşılığı doğru:**

| Bulgu | Talimattaki karşılığı | Değerlendirme |
|---|---|---|
| RP1A-01: loader–hesaplama bağlantısı | R-1: gerçek tüketicide handoff ve context testi | Kapanış için uygun |
| RP1A-02: eksik QC testleri | R-2: eksik hata dalları ve hesaplanan test sonuçları | Kapanış için uygun; kapsamı gereksiz genişletilmiş |
| RP1A-03: eksik non-regression | R-3: üç dosyanın karşılaştırılması | Kapanış için uygun; E kuralları düzeltilmeli |

Bunlar **uygulama ve bağımsız doğrulama sonrasında** kapanabilir; talimatın imzalanmasıyla kapanmış sayılmaz.

**İmzadan önce düzeltilmesi gerekenler:**

1. **F1 dosyası okuma yasağı ile sidecar üretme emri çelişiyor — STOP riski.**  
   §0, F1 hash tablosunun açılmasını ve hash kontrolünü yasaklıyor; §6 aynı dosyanın baytlarından SHA256 hesaplanmasını istiyor. Hash hesaplamak da dosyayı okumaktır.  
   **Düzeltme:** Yalnız hash tablosunun custody amacıyla opak bayt olarak okunmasına açık istisna yazılmalı; tabloyu ayrıştırma, raw dosyalara erişme ve eligible manifest’i açma yasağı korunmalı. §9’daki “no F1 path” kontrolü de bu istisnayla uyumlu olmalı.

2. **Replay testi, restart sonrasında yeniden yanlış başarısızlık üretebilir — B riski.**  
   R-5, replay satırlarını “ilk fit’in yazdığı satırlar” ile eşitliyor. Oysa sıcak store’dan devam edildiğinde ilk fit de cache’den okuyabilir ve yeni satır yazmayabilir. Önceki attempt-3 kusurunun benzeri geri gelebilir.  
   **Düzeltme:** İkinci okumanın replay kayıtları, ilgili **stored unit’lerin kayıtlarıyla** karşılaştırılmalı; ilk fit’in taze hesaplama yapmış olması şart koşulmamalı. Cold ve warm durumları sınanmalı.

3. **E beyanlarının mutlaka bir fark üretmesi istenmemeli — gereksiz başarısızlık/B riski.**  
   R-3, beyan edilmiş ama gözlenmemiş farkı başarısızlık sayıyor. Ancak önceden belirtilen doğru beklenti `8 → 8` olabilir; bazı süre veya ortam alanları da aynı kalabilir.  
   **Düzeltme:** “Beyan edilen beklenti sağlandı mı?” kontrol edilmeli. `EQUAL`, `ADDITION`, belirli sayı geçişi ve belirli alanda izin verilen değişim ayrılmalı. Beyan dışı farklar U kalmalı.

4. **Executor hazırlık durumu ile auditor kapanışı birbirine bağlanmış — karşılanamayan önkoşul riski.**  
   §3, R42A-03’ün audit’e kadar OPEN kalmasını istiyor; §8 ise bu pakette kapanacak bütün ledger maddelerinin kapalı olmasını `PREPARED_PENDING_INDEPENDENT_AUDIT` şartı yapıyor.  
   **Düzeltme:** Executor aşamasında `IMPLEMENTED_PENDING_VERIFICATION`; auditor doğrulamasından sonra `CLOSED` ayrımı kullanılmalı. Executor’dan henüz yapılmamış audit’in sonucunu beklememeli.

**İki ek sadeleştirme öneriyorum:**

- **R-2’de bütün harness boyunca literal `passed=True` yasağını kaldırın.** Mevcut NR-01 kodunda önce gerçek assertion’lar çalışıyor, ardından `passed=True` dönüyor; bu tek başına sahte PASS değildir. Kural, yeni/değişen testlerde sonucun gözlenen davranışla kanıtlanmasına odaklansın.
- **R-4 prosedüründe custody/output/store izolasyonunu açıklaştırın.** Mevcut writer aynı custody dosyası varsa duruyor. Sadece `F3_REPO_ROOT` eklemek yeterli olmayabilir. Ayrıca farklı ortamda çalışabilmek, bilimsel sonuçların birebir eşit çıkacağını garanti etmez; S eşitliği şartı korunmalıdır.

**Önerim:** Bu dar düzeltmeler yapılsın, ardından final talimatın hash’i D-12’ye yazılsın. D-12 burada ekli olmadığı için imza, seçimler ve hash bağlantısını henüz doğrulamadım. Yeni bilimsel karar veya geniş bir yeniden inceleme istemiyorum.
