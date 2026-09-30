# v4(r2) + freeze-v0(r3) change report (2026-08-18)

**Bağlayıcı talimat:** `v4_freeze_v0_chatgpt_nihai_degerlendirme.md`
(SHA256 `f98694287bd320758f1225986556ace8c9dc196cc7507affdbf6bfaca480d41c`),
Öner tarafından bağlayıcı ilan edildi. **Statü:** freeze-v0 **ONAY
BEKLİYOR** — FROZEN yapılmadı; onay checkbox'ı işaretlenmedi. Dosya
adları korunarak yerinde revize edildi (belge-içi r2/r3 revizyon
notlarıyla); hash soyağacı aşağıda.

## Değişiklik tablosu

| # | Değişiklik | Önceki durum | Yeni durum (v4 r2 / freeze r3) | Gerekçe | Yeni yöntem/estimand? |
|---|---|---|---|---|---|
| 1 | **Self-hash prosedürü kaldırıldı** (MUST-FIX, governance) | Freeze §10, hesaplanan hash'in belge içindeki `FROZEN SHA256:` alanına yazılmasını öngörüyordu — H(D)=h yazılınca dosya D′ olur, H(D′)≠h; self-invalidating | Hash belge DIŞINDA: `sha256sum … > extension_decision_freeze_v0.md.sha256` → iki dosya birlikte commit (+tag); belge içinde yalnız değişmez cümle: *Freeze hash is stored externally in `extension_decision_freeze_v0.md.sha256`.* v4 FAZ 0.5 prosedür metni de aynı yapıya çevrildi; `FROZEN SHA256:` alanı silindi (denetim: 0 geçiş) | Provenance bütünlüğü; benim iki-aşamalı önceki çözümüm bundan zayıftı — kabul | Hayır |
| 2 | **Exact ICL tanımı ŞİMDİ pinlendi** (MUST-FIX, scientific pin; Seçenek A) | "Exact ICL formülü prereg'de yazılır" — bilimsel seçici tanımı freeze sonrasına kalıyordu | Freeze §5 + v4 FAZ 0.5'te DONUK: saklanan konvansiyon sklearn (BIC_stored=−2logL̂+p_k·log n, düşük-iyi); **ICL_stored(k)=BIC_stored(k)+2·E(k)**, E(k)=−ΣᵢΣ_c τ_ic·log τ_ic (doğal log; 0·log0:=0; τ=yakınsamış en-iyi fit'in `predict_proba`'sı); yön her ikisinde **argmin**; k̂ seçimi native 1..10 / restricted 2..10; bağ → en küçük k (donmuş isclose toleransı rtol=1e-10/atol=1e-12). Birim test sonra; tanım freeze sonrası seçilemez. (Biernacki, Celeux & Govaert 2000 → düşük-iyi eşleme) | k̂_ICL tanıma bağlıdır; RNG/çıktı-adı sınıfı bir uygulama detayı değildir | Hayır (mevcut seçicinin tanım kesinleştirmesi) |
| 3 | **§9 normatif/bilgilendirici ayrımı** (CLEANUP) | Tek bölümde tam-hash normatif kayıtlarla kısa-hash tarihsel kayıtlar ve normatif dosyaların kısa-hash TEKRARLARI karışıktı | **§9.1 Normative frozen dependencies:** yalnız 4 tam-64-karakter kayıt (protokol · sapma eki · manifest · v4 r2). **§9.2 Informational provenance references (non-normative):** kısa-hash tarihsel kayıtlar + iki bağlayıcı talimat. Normatif kısa-hash tekrarları silindi (denetim: 9.1 içinde 0) | Normatif pin ile provenance/history ayrışır | Hayır |
| 4 | **source_status şeması** (schema cleanup) | t₅ ve FPCA/B-spline satırlarında `source_status = —` | Enum genişletildi: `verified|pending|not_applicable`; t₅ → not_applicable, FPCA/B-spline → not_applicable (ikisi de dış-kaynak teyit iddiası taşımaz; FPCA'nın kapısı kaynak değil, ayrı-kol ön-kaydıdır) | Machine-readable governance; "—" bırakılmaz | Hayır |

## Denetim (grep-tabanlı; her iki dosya)

`FROZEN SHA256:` geçişi: **0** — PASS · ICL exact formül her iki
belgede — PASS · §9.1/§9.2 başlıkları mevcut, 9.1 içinde kısa-hash
normatif tekrar **0** — PASS · `not_applicable` her iki belgede
(freeze: tablo satırları + enum; v4: enum + günlük) — PASS · harici
`.sha256` prosedürü her iki belgede — PASS · `ONAY BEKLİYOR` duruyor,
checkbox işaretsiz — PASS. Kapsam disiplini: yeni yöntem yok, yeni null
ailesi yok, Friedman/GLMM kararlarına dokunulmadı, yeni EK döngüsü
açılmadı — PASS.

## Hash soyağacı

```
530fc762…  yol_haritasi_v4_FINAL_2026-08-18.md (r1)  → YERİNİ ALDI:
0c80c1894ebe5cba00ed9e76d57aa5131c564365fbcfea1815db31fff39e3915  v4 r2
fe50dfe5…  extension_decision_freeze_v0.md (r2)      → YERİNİ ALDI:
e45b4486181fa833657fe6059ad066dd8ae95c118238a9b6e04d8ccab5714ce5  freeze r3 (ONAY BEKLİYOR)
```
Not: freeze r3 hash'i yalnız bu raporun soyağacı içindir; nihai freeze
hash'i, Öner onayı ve varsa onay-alanı doldurma SONRASINDA harici
`.sha256` dosyasında üretilecektir (belge içine yazılmaz).

## Sonraki adım

ChatGPT hükmüyle uyumlu: **bilimsel omurga GO; freeze imzası bu dört
kalem kapandığı için artık açık** → Öner üç dosyayı inceler → onay →
`sha256sum … > .sha256` + commit(+tag) → FROZEN → FAZ 1.
