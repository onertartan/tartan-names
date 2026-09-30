# Claude Chat — F3 STEP2 prompt DRAFT v5: §16 için son dar düzeltme

## Görev ve inceleme sonucu

Bu geri bildirim belge yazarı **Claude Chat** içindir. Yalnızca execution promptunun §16 dispatch tablosunu mevcut §2–§3 kurallarıyla tutarlı hale getir ve ayrı bir **DRAFT v6** üret. Uygulama veya qualification koşumu başlatma; S/T seçeneği seçme.

C-01 ve C-02 kapanmıştır:

- Audit r6, gerçek fit yolunda erişilemezlik iddiasını doğru biçimde daraltıyor.
- Prompt v5, editorial correction adaylarını kabul edilmiş audit olarak sunmuyor.
- Dosyalar arası hash atıfları, geri bildirim hash’i ve aktarılan Kimi v4 review hash’i eşleşiyor.

U-set semantiğini, replay bankasını veya kapanmış diğer maddeleri yeniden açma. Audit r6 ve reconciliation r5 dosyalarını bu görev nedeniyle yeniden revize etme.

## Kaynak dosyalar

| Dosya | Hesaplanan SHA256 |
|---|---|
| Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v5.md | a0fbbb1b3c0ba33654ea50f9241c655b4af8e1e98274355ae255cda81e6c8866 |
| f3_step2_independent_audit_DRAFT_r6_editorial_correction_candidate.md | 12c1532216f3da9e4b64b51b1e5426d9d77d13de9d6fa6cb44fa43374667ed94 |
| f3_step2_cross_auditor_reconciliation_r5_editorial_correction_candidate.md | 377d70405d975daaa5f486cbe2298863b43e74e3a7ea100772ae2b6afcd68b15 |

Yüklenen adlarda `(1)` eki bulunabilir; içerik kimliğini gerçek dosya baytlarından doğrula. Kaynak prompt yoksa veya hash uyuşmazsa eşdeğer dosya üretme; durumu bildir. Bu incelemeye sidecar’lar verilmediğinden dış sidecar eşleşmesi doğrulanmamıştır. Harness veya qualification koşumu yapılmamıştır.

## S16-01 — Tablo satırlarını mevcut kurallarla eşleştir

§16’nın giriş açıklaması doğru ayrımı yapıyor; bazı satırlar ise yanlış grupta. Aşağıdaki değişiklikleri uygula:

| Mevcut satır | Gerekli işlem | Dayanak |
|---|---|---|
| R1 koşumunun v5 §15 end-of-task tablosu; “lineage only” | A’daki zorunlu girdilerden B’deki kayıt/iletim işlerine taşı. | Tarihsel kayıt niteliği; yokluğu tek başına yeni dispatch engeli değildir. |
| ADDENDUM A r1 ve eski v2–v4 promptları | B’ye taşı; varsa byte-exact import ve kayıt işini koru. | §2.3 record-class statüsü. Tablo başlığıyla yeni STOP şartı yaratma. |
| Dispatch-time observed hash of this prompt | B’den A’ya taşı. Yalnız hash’in kaydedilmesini değil, P-4’teki eşleşme kontrolünü doğru yansıt. | §3 P-4: gözlenen prompt hash’i, PI’nın dispatch için kaydettiği değerle eşleşmelidir. |
| T-5 | Zorunlu alanlardan ayrı bir “isteğe bağlı alan” notunda göster veya A içinde istisna niteliğini başlık düzeyinde açıklaştır. | Boş/eksik T-5 izin verilen statükodur; PENDING veya tek başına STOP değildir. |
| Eksik r1 sidecar’lar | Bunların dispatch öncesinde koşulsuz teslim edilmesi gerekiyormuş izlenimini kaldır; mevcut istisnayı açıkça yaz. | §2.2 item 19 ve P-1: eksik sidecar tek başına STOP değildir; mevcut fakat uyuşmayan sidecar ise mismatch’tir. Eksik sidecar ancak önkoşullar geçtikten sonra izin verilen custody aşamasında oluşturulur. |

Bu değişiklikler yeni gereksinim koymaz ve mevcut zorunlu kontrolleri gevşetmez. §16, §2–§3’ü özetlemeli; onlardan farklı bir yürütme kuralı üretmemelidir.

## S16-02 — Güncel inceleme geçmişini düzelt

§16’daki `external review of this draft` satırında kalan “this v4” ve “further review … as v5” ifadelerini gerçek geçmişe uygun güncelle:

- v4 paketi: Kimi v4 incelemesi ve ChatGPT dar geri bildirimi.
- v5 paketi: C-01/C-02 uygulanmış; bu geri bildirimde kapanışları kontrol edilmiş.
- Yeni v6: yalnız §16 sınıflandırması ve ilgili sürüm/atıf düzeltmeleri.

Bunu otomatik olarak yeni kapsamlı audit turu veya ek PI onayı talebine dönüştürme. Belge incelemesini uygulama yeterliliğinin bağımsız doğrulanmasıyla karıştırma.

## Teslimat ve doğrulama

1. Mevcut v5 dosyasını değiştirmeden `Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md` oluştur.
2. Başlık, prompt_id, draft_revision ve parent alanlarını güncelle; doğrudan parent v5’in yukarıdaki hash’ini koru. Tarihsel v5 atıflarını topluca değiştirme.
3. Audit r6 ve reconciliation r5 atıfları aynı dosyalara ve aynı hash’lere işaret etmeye devam etsin.
4. Diff’i yalnız §16, bu düzeltmenin kısa kapanış kaydı ve gerekli sürüm/lineage alanlarıyla sınırla.
5. Son v6 baytlarından dış `.sha256` sidecar üret. Belgeye kendi nihai hash’ini gömme.
6. Yanıtta S16-01/S16-02 kapanışını ve yeni prompt hash’ini kısa biçimde bildir.

Hedef v6 zaten mevcutsa üzerine yazma; ayrı çocuk revizyon adı kullan ve bildir. Audit ve reconciliation için yeni dosya üretme.

## Korunacak sınırlar

```text
revision_scope = DOCUMENT_ONLY
implementation_executed = false
independent_requalification_performed = false
S_T_decisions_selected = false
F2 = CLOSED
F3_STEP1 = FROZEN
prompt_status = DRAFT_NOT_FOR_EXECUTION_DISPATCH
F3_EXECUTION_READY = false
commit = false
```

Son dosyanın yazarı Claude Chat’tir; `Claude_Code_` öneki gelecekteki muhatabı belirtir. Bu belge düzeltmesinin tamamlanması, PI kararları ve zorunlu dispatch girdilerinin tamamlandığı anlamına gelmez. Dosyayı teslim et; uygulama koşumuna geçme.
