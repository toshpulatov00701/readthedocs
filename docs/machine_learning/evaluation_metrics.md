# Baholash metrikalari

**Baholash metrikalari (*evaluation metrics*)** — klassifikatsiya modelining ishlash sifatini o'lchaydigan ko'rsatkichlar. Model bashoratlari haqiqiy javoblar bilan solishtiriladi, metrika esa solishtirish natijasini **bitta songa** aylantiradi.

Har bir metrika alohida savolga javob beradi:

- "Jami nechta javob to'g'ri?" → Accuracy
- "Model 'kasal' desa, javobga ishonsa bo'ladimi?" → Precision
- "Kasallarning nechtasi topildi?" → Recall
- "Model tasodifiy taxmindan yaxshiroqmi?" → Cohen's Kappa, MCC

*! Bitta metrikaga qarash yetarli emas, ayniqsa sinflar **nomutanosib** bo'lganda.*

---

<h2>Misol dataset</h2>

Model 100 ta bemorni 3 sinfga ajratadi:

| Sinf | Haqiqiy soni | Ulushi |
|---|---|---|
| Sog'lom | 80 | 80% |
| Gripp | 15 | 15% |
| Kovid | 5 | 5% |

**Nomutanosib (*imbalanced*) dataset** — bitta sinf boshqa sinflardan ancha ko'p bo'lgan dataset. Misolda sog'lomlar 80 ta, Kovid bemorlari esa atigi 5 ta. Hayotda nomutanosiblik juda ko'p uchraydi: kasallik, firibgarlik, spam, nosozlik har doim kam bo'ladi.

Sahifadagi barcha hisob-kitoblar yuqoridagi dataset va quyidagi confusion matrix asosida bajariladi. Misoldagi model keyingi bo'limlarda **asosiy model** deb ataladi.

---

<h2>Confusion matrix (chalkashlik matritsasi)</h2>

**Confusion matrix** — model qayerda to'g'ri topganini va qaysi sinfni qaysi sinf bilan adashtirganini ko'rsatadigan jadval.

- **Qatorlar** — bemorning **haqiqiy** sinfi.
- **Ustunlar** — model **bashorat qilgan** sinf.

| Haqiqiy ↓ / Bashorat → | Sog'lom | Gripp | Kovid | **Jami (haqiqiy)** |
|---|---|---|---|---|
| **Sog'lom** | **74** | 4 | 2 | 80 |
| **Gripp** | 5 | **8** | 2 | 15 |
| **Kovid** | 1 | 1 | **3** | 5 |
| **Jami (bashorat)** | 80 | 13 | 7 | **100** |

Jadvalni o'qish tartibi:

- **Diagonal** (qalin sonlar) — to'g'ri javoblar: 74 + 8 + 3 = **85**.
- **Diagonaldan tashqaridagi sonlar** — xatolar. Jami 15 ta.
- "Gripp" qatori va "Sog'lom" ustunidagi **5** soni: 5 ta gripp bemori model tomonidan "sog'lom" deb topilgan.
- "Kovid" qatoridagi 1 + 1 = 2 ta bemor boshqa sinfga kiritilgan, ya'ni o'tkazib yuborilgan.

---

<h2>TP, FP, FN, TN</h2>

Barcha metrikalar to'rtta sondan quriladi: TP, FP, FN va TN. Ko'p sinfli masalada har bir sinf navbat bilan **"tanlangan sinf"** va **"qolgan barcha sinflar"** ko'rinishida qaraladi. Usul nomi — **One-vs-Rest**.

To'rtta tushuncha (Kovid sinfi misolida):

| Belgi | To'liq nomi | Sodda ma'nosi | Kovid uchun |
|---|---|---|---|
| **TP** | True Positive | Bemor Kovid edi, model ham **Kovid** dedi | **3** |
| **FN** | False Negative | Bemor Kovid edi, model **boshqa sinf** dedi (o'tkazib yuborildi) | 1 + 1 = **2** |
| **FP** | False Positive | Bemor Kovid emas edi, model **Kovid** dedi (yolg'on xavotir) | 2 + 2 = **4** |
| **TN** | True Negative | Bemor Kovid emas edi, model ham **Kovid emas** dedi | 100 − 3 − 2 − 4 = **91** |

Matritsadan tez topish usuli:

- **TP** — diagonaldagi son.
- **FN** — sinf **qatoridagi** qolgan sonlar yig'indisi (haqiqiy sinf to'g'ri, bashorat boshqa).
- **FP** — sinf **ustunidagi** qolgan sonlar yig'indisi (haqiqiy sinf boshqa, bashorat tanlangan sinf).
- **TN** — jami − TP − FN − FP.

Barcha sinflar uchun:

| Sinf | TP | FP | FN | TN |
|---|---|---|---|---|
| Sog'lom | 74 | 5 + 1 = 6 | 4 + 2 = 6 | 14 |
| Gripp | 8 | 4 + 1 = 5 | 5 + 2 = 7 | 80 |
| Kovid | 3 | 2 + 2 = 4 | 1 + 1 = 2 | 91 |

*! Keyingi barcha hisob-kitoblar yuqoridagi jadvaldan olinadi.*

---

## Accuracy (umumiy to'g'rilik)

To'g'ri klassifikatsiya qilingan obyektlar sonining jami obyektlar soniga nisbati.

Savol: jami javoblarning qanchasi to'g'ri?

$$
\text{Accuracy} = \frac{\text{to'g'ri javoblar}}{\text{jami}} = \frac{74+8+3}{100} = \mathbf{0.85}
$$

Ikki sinfli masalada formula quyidagi ko'rinishni oladi:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Sodda ma'nosi: 100 bemordan 85 tasining sinfi to'g'ri topildi.

Kamchiligi: 85% yaxshi ko'rinadi, lekin to'g'ri javoblarning katta qismi (74 tasi) sog'lomlar. Sog'lomlarni topish oson, chunki sog'lomlar ko'pchilikni tashkil qiladi. Accuracy kichik sinflardagi yomon natijani **yashiradi**. Batafsil tushuntirish "Accuracy va Balanced Accuracy farqi" hamda "Nomutanosiblik tuzog'i" bo'limlarida berilgan.

Qachon ishlatiladi: faqat sinflar taxminan teng bo'lganda.

---

## Precision (aniqlik, ishonchlilik)

Model tanlangan sinf deb aytgan obyektlarning qancha qismi haqiqatan ham tanlangan sinfga tegishli?

$$
\text{Precision} = \frac{TP}{TP + FP} = \frac{\text{to'g'ri topilganlar}}{\text{model tanlangan sinf deb aytgan barcha obyektlar}}
$$

| Sinf | Hisob | Natija |
|---|---|---|
| Sog'lom | 74 / (74 + 6) | 0.925 |
| Gripp | 8 / (8 + 5) | 0.615 |
| Kovid | 3 / (3 + 4) | 0.429 |

Sodda ma'nosi (Kovid): model 7 kishiga "Kovid" dedi. 7 kishidan faqat 3 tasi haqiqatan Kovid edi. Demak, modelning "Kovid" degan javobiga faqat 43% ishonish mumkin.

Hayotiy misol: spam filtri. Precision past bo'lsa, muhim xatlar spam papkasiga tushib ketadi. Yolg'on xavotir qimmatga tushadigan joyda precision muhim.

---

## Recall / Sensitivity (qamrov, sezgirlik)

Haqiqatan tanlangan sinfga tegishli obyektlarning qancha qismini model topa oldi?

$$
\text{Recall} = \frac{TP}{TP + FN} = \frac{\text{to'g'ri topilganlar}}{\text{haqiqatan tanlangan sinfga tegishli barcha obyektlar}}
$$

| Sinf | Hisob | Natija |
|---|---|---|
| Sog'lom | 74 / 80 | 0.925 |
| Gripp | 8 / 15 | 0.533 |
| Kovid | 3 / 5 | 0.600 |

Sodda ma'nosi (Kovid): haqiqatda 5 ta Kovid bemori bor edi. Model 3 tasini topdi, 2 tasini o'tkazib yubordi. O'tkazib yuborilgan bemor davolanmasdan uyga ketadi.

Hayotiy misol: tibbiyot, firibgarlikni aniqlash. Kasalni yoki firibgarni o'tkazib yuborish yolg'on xavotirdan ancha qimmatga tushadi.

Precision va recall farqi:

- **Precision** — "Model aytgan javoblarning qanchasi to'g'ri?"
- **Recall** — "Mavjud holatlarning qanchasi topildi?"

*! Precision va recall ko'pincha qarama-qarshi harakat qiladi. Model hamma bemorga "Kovid" desa, recall 1.0 bo'ladi (birorta ham Kovid bemori o'tkazib yuborilmaydi), lekin precision keskin tushib ketadi.*

---

## Specificity (o'ziga xoslik)

Tanlangan sinfga tegishli bo'lmagan obyektlarning qancha qismini model to'g'ri rad etdi?

$$
\text{Specificity} = \frac{TN}{TN + FP}
$$

| Sinf | Hisob | Natija |
|---|---|---|
| Sog'lom | 14 / (14 + 6) | 0.700 |
| Gripp | 80 / (80 + 5) | 0.941 |
| Kovid | 91 / (91 + 4) | 0.958 |

Sodda ma'nosi (Kovid): Kovid bo'lmagan 95 kishidan 91 tasiga model to'g'ri "Kovid emas" dedi.

Recall bilan farqi:

- **Recall** — "Kasallar topildimi?"
- **Specificity** — "Sog'lomlar bekorga kasal deyilmadimi?"

*! Kichik sinflarda specificity doim yuqori chiqadi, chunki "tanlangan sinf emas" obyektlar juda ko'p va TN katta bo'ladi. Kovid uchun 0.958 natija aldamasligi kerak: Kovid bemorlarining 40 foizi baribir o'tkazib yuborilgan. Specificity yolg'iz holda yetarli xulosa bermaydi.*

---

## F1-score

Precision va recall orasidagi balansni o'lchaydi (**garmonik o'rtacha**).

$$
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}
$$

Oddiy o'rtachadan farqi: precision yoki recall past bo'lsa, F1 ham past chiqadi. Masalan, precision = 1.0 va recall = 0.1 bo'lsa, oddiy o'rtacha 0.55, F1 esa atigi 0.18.

| Sinf | Hisob | Natija |
|---|---|---|
| Sog'lom | 2·74 / (148 + 6 + 6) | 0.925 |
| Gripp | 2·8 / (16 + 5 + 7) | 0.571 |
| Kovid | 2·3 / (6 + 4 + 2) | 0.500 |

Sodda ma'nosi: F1 "model sinfni topishda ham, ishonchli javob berishda ham qanchalik yaxshi" degan savolga javob beradi. Sog'lom uchun natija yaxshi, Gripp va Kovid uchun o'rtacha.

Nega alohida ko'rsatkich yetarli emas?

- Faqat precision yuqori bo'lsa, recall past bo'lishi mumkin (ko'p haqiqiy holatlar o'tkazib yuboriladi).
- Faqat recall yuqori bo'lsa, precision past bo'lishi mumkin (ko'p yolg'on xavotir chiqadi).
- F1-score ikkala ko'rsatkichni garmonik o'rtacha orqali baholaydi va bir tomonga og'ib ketishning oldini oladi.

---

<h2>O'rtacha olish usullari: Macro, Weighted, Micro</h2>

Precision, recall, F1 va Jaccard har bir sinf uchun alohida hisoblanadi. Bitta umumiy son olishning 3 usuli bor.

**Macro (oddiy o'rtacha)** — har bir sinf **teng** hisoblanadi, sinf hajmidan qat'i nazar.

$$
\text{Macro-F1} = \frac{0.925 + 0.571 + 0.500}{3} = 0.665
$$

**Weighted (tortilgan o'rtacha)** — har bir sinf **hajmga qarab** tortiladi. Sog'lom 80% vaznga, Kovid 5% vaznga ega.

$$
\text{Weighted-F1} = 0.80 \cdot 0.925 + 0.15 \cdot 0.571 + 0.05 \cdot 0.500 = 0.851
$$

**Micro (bitta umumiy hisob)** — barcha sinflarning TP, FP va FN qiymatlari qo'shiladi va formulaga bir marta qo'yiladi.

$$
\text{Micro-F1} = \frac{2 \cdot 85}{2 \cdot 85 + 15 + 15} = \frac{170}{200} = 0.85
$$

*! Har bir obyektga faqat bitta sinf beriladigan ko'p sinfli masalada Micro-F1 har doim accuracy'ga teng.*

| | Macro | Weighted | Micro |
|---|---|---|---|
| Precision | 0.656 | 0.854 | 0.85 |
| Recall | 0.686 | 0.85 | 0.85 |
| F1 | **0.665** | 0.851 | 0.85 |

Xulosa: weighted va micro natijalari 0.85 atrofida, chunki natijani Sog'lom sinfi ko'tarib turibdi. Macro esa 0.67 atrofida, chunki Gripp va Kovid ham teng ovozga ega. **Nomutanosib datasetda macro eng adolatli usul.**

---

## Balanced Accuracy (muvozanatlangan to'g'rilik)

Har bir sinf recall qiymatlarining oddiy o'rtachasi.

Savol: har bir sinfga teng e'tibor berilsa, model o'rtacha qanchalik yaxshi?

$$
\text{Balanced Accuracy} = \frac{\text{Recall}_1 + \text{Recall}_2 + \text{Recall}_3}{3} = \frac{0.925 + 0.533 + 0.600}{3} = \mathbf{0.686}
$$

Sodda ma'nosi: model har bir sinfning o'rtacha 69 foizini to'g'ri topadi.

---

<h2>Accuracy va Balanced Accuracy farqi</h2>

Asosiy modelda accuracy **0.85**, balanced accuracy esa **0.686**. Farqning ma'nosi: **model katta sinfda (Sog'lom) yaxshi ishlaydi, kichik sinflarda (Gripp, Kovid) yomon ishlaydi, accuracy esa kamchilikni yashirib qo'yadi.**

<h3>Nima uchun natijalar har xil chiqadi?</h3>

Ikkala metrika ham har bir sinfning recall qiymatidan hisoblanadi. Farq faqat o'rtacha olish usulida.

| Sinf | Recall | Sinf ulushi |
|---|---|---|
| Sog'lom | 0.925 | 80% |
| Gripp | 0.533 | 15% |
| Kovid | 0.600 | 5% |

**Accuracy** recall qiymatlarini sinf hajmiga qarab tortadi:

$$
0.80 \cdot 0.925 + 0.15 \cdot 0.533 + 0.05 \cdot 0.600 = 0.74 + 0.08 + 0.03 = \mathbf{0.85}
$$

Sog'lom sinfi 80% vaznga ega va natijani deyarli yolg'iz belgilaydi. Kovid atigi 5% vaznga ega, natijada Kovid sinfidagi yomon ko'rsatkich deyarli sezilmaydi.

**Balanced accuracy** har bir sinfga teng vazn beradi:

$$
\frac{0.925 + 0.533 + 0.600}{3} = \mathbf{0.686}
$$

Kovid ham, Sog'lom ham 1/3 vaznga ega. Kichik sinflardagi zaiflik natijani pastga tortadi.

Demak:

- **Accuracy 0.85** — "100 bemordan 85 tasi to'g'ri topildi." Natija rost, lekin to'g'ri topilgan bemorlarning ko'pi sog'lomlar.
- **Balanced accuracy 0.686** — "har bir sinfning o'rtacha 69 foizi topildi."

<h3>Ideal holat</h3>

Ideal holatda accuracy va balanced accuracy **yaqin** chiqadi. Yaqin natija model barcha sinflarda bir xil darajada yaxshi ishlayotganini bildiradi.

Masalan, boshqa bir model har bir sinfning 80 foizini to'g'ri topgan bo'lsin:

| Sinf | To'g'ri topildi | Recall |
|---|---|---|
| Sog'lom | 64 / 80 | 0.80 |
| Gripp | 12 / 15 | 0.80 |
| Kovid | 4 / 5 | 0.80 |

- Accuracy = (64 + 12 + 4) / 100 = **0.80**
- Balanced accuracy = (0.80 + 0.80 + 0.80) / 3 = **0.80**

Natijalar teng chiqdi, chunki model hech bir sinfni "unutmagan". Ikkinchi modelning accuracy qiymati pastroq (0.80 < 0.85), lekin kasallarni asosiy modelga qaraganda **yaxshiroq** topadi.

<h3>Katta farq — yomon belgi</h3>

| Model | Accuracy | Balanced Accuracy | Farq | Ma'nosi |
|---|---|---|---|---|
| Teng ishlaydigan model | 0.80 | 0.80 | 0 | Barcha sinflar teng o'rganilgan |
| Asosiy model | 0.85 | 0.686 | 0.16 | Kichik sinflar zaif |
| Har doim "Sog'lom" deydigan model | 0.80 | 0.333 | 0.47 | Kichik sinflar umuman o'rganilmagan |

*! Accuracy va balanced accuracy orasida katta farq bo'lsa, recall qiymatlarini sinflar bo'yicha alohida tekshirish kerak. Odatda kichik sinflardan birida muammo bo'ladi.*

---

## Cohen's Kappa

Model tasodifiy taxmindan qanchalik yaxshiroq ekanini o'lchaydi.

G'oyasi: to'g'ri javoblarning bir qismini ko'r-ko'rona taxmin ham bera oladi. Masalan, bemorlarning 80 foizi sog'lom bo'lsa, tasodifiy "sog'lom" degan javob ko'pincha to'g'ri chiqadi. Kappa **tasodifan olingan to'g'ri javoblarni chiqarib tashlaydi** va faqat modelning haqiqiy hissasini o'lchaydi.

$$
\kappa = \frac{p_o - p_e}{1 - p_e}
$$

- $p_o$ — kuzatilgan moslik, ya'ni oddiy accuracy.
- $p_e$ — tasodifan kutiladigan moslik.

Hisob-kitob:

1. $p_o$ = accuracy = **0.85**

2. $p_e$ qiymatini topish uchun har bir sinfning (qator jami × ustun jami) ko'paytmalari qo'shiladi va yig'indi $N^2$ ga bo'linadi:

$$
p_e = \frac{80 \cdot 80 + 15 \cdot 13 + 5 \cdot 7}{100^2} = \frac{6400 + 195 + 35}{10000} = \frac{6630}{10000} = 0.663
$$

Ma'nosi: model haqiqiy javoblarga qaramasdan, faqat bashoratlar nisbatini saqlagan holda tasodifiy javob berganda ham taxminan 66% javob to'g'ri chiqqan bo'lardi.

3. Kappa qiymati:

$$
\kappa = \frac{0.85 - 0.663}{1 - 0.663} = \frac{0.187}{0.337} = \mathbf{0.555}
$$

Sodda ma'nosi: tasodif bilan mukammallik orasidagi yo'lning **55 foizi** bosib o'tilgan. 85% accuracy'ning katta qismini tasodif ham bera olar edi.

Baholash shkalasi (Landis va Koch):

| Kappa | Baho |
|---|---|
| 0 dan past | Tasodifdan ham yomon |
| 0.00 – 0.20 | Juda zaif |
| 0.21 – 0.40 | Zaif |
| **0.41 – 0.60** | **O'rtacha** ← asosiy model |
| 0.61 – 0.80 | Yaxshi |
| 0.81 – 1.00 | Deyarli mukammal |

Qayerda ishlatiladi: modellarni baholashda, shuningdek ikki shifokor yoki ikki annotator javoblari qanchalik mos kelishini o'lchashda.

---

## MCC (Matthews Correlation Coefficient)

Haqiqiy va bashorat qilingan sinflar orasidagi **korrelyatsiya**.

Savol: model bashorati haqiqat bilan qanchalik bog'liq?

G'oyasi: MCC confusion matrix'ning **barcha** kataklarini hisobga oladi. Natijada MCC nomutanosiblikka eng chidamli metrikalardan biri hisoblanadi.

Ko'p sinfli formula:

$$
MCC = \frac{c \cdot s - \sum_k p_k t_k}{\sqrt{(s^2 - \sum_k p_k^2)(s^2 - \sum_k t_k^2)}}
$$

Belgilar:

- $c$ — to'g'ri javoblar soni = **85**
- $s$ — jami namunalar soni = **100**
- $t_k$ — har bir sinfning haqiqiy soni (qator jamilari) = **80, 15, 5**
- $p_k$ — har bir sinf necha marta bashorat qilingani (ustun jamilari) = **80, 13, 7**

Hisob-kitob:

Surat:

$$
85 \cdot 100 - (80 \cdot 80 + 15 \cdot 13 + 5 \cdot 7) = 8500 - 6630 = 1870
$$

Maxrajdagi 1-qavs:

$$
10000 - (80^2 + 13^2 + 7^2) = 10000 - (6400 + 169 + 49) = 3382
$$

Maxrajdagi 2-qavs:

$$
10000 - (80^2 + 15^2 + 5^2) = 10000 - (6400 + 225 + 25) = 3350
$$

Natija:

$$
MCC = \frac{1870}{\sqrt{3382 \cdot 3350}} = \frac{1870}{3366.0} = \mathbf{0.556}
$$

<h3>Natijani tushunish</h3>

MCC qiymatini o'lchov chizig'ida tasavvur qilish qulay:

```
 -1 ──────────── 0 ──────────── +0.556 ──── +1
 Hammasi        Tasodifiy        Asosiy       Mukammal
 teskari        taxmin           model        model
```

- **+1** — model hamma bemorni to'g'ri topadi.
- **0** — model hech narsa o'rganmagan, tanga tashlagandek ishlaydi.
- **−1** — model har doim teskari javob beradi. Amalda deyarli uchramaydi.

Asosiy model 0 dan +1 gacha bo'lgan yo'lning yarmidan sal o'tgan: **tasodifdan aniq yaxshiroq, lekin mukammallikdan ancha uzoq.**

| MCC | Baho (taxminiy) |
|---|---|
| 0 atrofida | Foydasiz, tasodifdan farqi yo'q |
| 0.1 – 0.3 | Zaif |
| 0.3 – 0.5 | O'rtacha |
| **0.5 – 0.7** | **Yaxshi, lekin kamchiliklar bor** ← asosiy model |
| 0.7 – 0.9 | Kuchli |
| 0.9 dan yuqori | Juda kuchli |

*! Jadvaldagi chegaralar qat'iy qoida emas, umumiy mo'ljal xolos. Tibbiyotda talab odatda yuqoriroq bo'ladi.*

<h3>Nega accuracy 0.85, MCC esa atigi 0.556?</h3>

Imtihon misoli: testdagi 100 ta savolning 80 tasida to'g'ri javob "A". Bir o'quvchi darsga tayyorlanmasdan hamma savolga "A" belgilaydi va **80 ball** oladi.

- **Accuracy** o'quvchiga 80% beradi va "yaxshi o'quvchi" deb ko'rsatadi.
- **MCC** o'quvchiga **0** beradi, chunki o'quvchi faqat ko'pchilik javobni takrorlagan.

MCC tasodifan yoki "ko'pchilikka ergashib" olingan to'g'ri javoblar uchun ball bermaydi. Faqat model **haqiqatan o'rganib** topgan javoblar hisobga olinadi.

Asosiy modelda ham holat o'xshash:

- 85 ta to'g'ri javobning katta qismi sog'lomlar. Sog'lomlarni "hamma bemor sog'lom" deydigan model ham topa olardi.
- Gripp va Kovidni topishda model ancha qiynalgan.
- MCC ikkala holatni hisobga oladi va "haqiqiy bilim darajasi"ni taxminan 0.56 deb baholaydi.

Accuracy 0.85 model ishni yaxshi bajarayotgandek taassurot qoldiradi. MCC 0.556 esa haqiqiy holatni ko'rsatadi: model ma'lum darajada o'rgangan, lekin kichik sinflarda hali ko'p xato qiladi.

<h3>Kappa va MCC nega yaqin chiqdi (0.555 va 0.556)?</h3>

Kappa ham, MCC ham bitta g'oyaga asoslangan: model tasodifdan qanchalik yaxshi ekanini o'lchash. Ko'p hollarda natijalar yaqin chiqadi. MCC nazariy jihatdan biroz ishonchliroq hisoblanadi, chunki juda nomutanosib yoki g'ayrioddiy matritsalarda ham barqaror natija beradi.

---

## Jaccard Score (IoU, Intersection over Union)

Bashorat va haqiqat kesishmasining birlashmaga nisbati.

Savol: tanlangan sinfga aloqador barcha obyektlarning qancha qismida model javobi va haqiqat mos keldi?

$$
J = \frac{TP}{TP + FP + FN} = \frac{\text{kesishma}}{\text{birlashma}}
$$

Kovid misolida ikki guruh bor:

- **A guruh** — model "Kovid" degan kishilar: **7** kishi.
- **B guruh** — haqiqatan Kovid bo'lgan kishilar: **5** kishi.

```
      Model "Kovid" dedi            Haqiqatan Kovid
        ┌────────────┬───────┬────────────┐
        │            │       │            │
        │  4 kishi   │   3   │  2 kishi   │
        │ (yolg'on   │ kishi │ (o'tkazib  │
        │  xavotir)  │       │ yuborilgan)│
        │    FP      │  TP   │    FN      │
        └────────────┴───────┴────────────┘
              Jami aloqador: 4 + 3 + 2 = 9 kishi
```

- O'rtadagi **3 kishi** ikkala guruhda ham bor: Kovid to'g'ri topilgan.
- Chapdagi **4 kishi** sog'lom yoki gripp bo'lgan, lekin model "Kovid" degan.
- O'ngdagi **2 kishi** Kovid bo'lgan, lekin model topa olmagan.

$$
J = \frac{3}{9} = 0.333
$$

Ma'nosi: "Kovid" masalasiga aloqador 9 kishidan faqat 3 tasida model to'g'ri ishlagan. Qolgan 6 tasida xato qilgan: yo bekorga Kovid degan, yo Kovidni o'tkazib yuborgan.

Har bir sinf natijasi:

| Sinf | Hisob | Jaccard | Sodda ma'nosi |
|---|---|---|---|
| Sog'lom | 74 / (74 + 6 + 6) | 0.860 | 86 kishidan 74 tasida mos keldi. Yaxshi |
| Gripp | 8 / (8 + 5 + 7) | 0.400 | 20 kishidan 8 tasida mos keldi. Zaif |
| Kovid | 3 / (3 + 4 + 2) | 0.333 | 9 kishidan 3 tasida mos keldi. Zaif |

Jaccard qiymatini foiz kabi o'qish mumkin: 1 bo'lsa, ikki guruh to'liq ustma-ust tushgan; 0 bo'lsa, guruhlar umuman kesishmaydi.

Umumiy sonlar:

- **Macro** = (0.860 + 0.400 + 0.333) / 3 = **0.531** — har bir sinf teng hisoblanganda, model javobi va haqiqat o'rtacha yarmidan sal ko'proq mos keladi. Kichik sinflardagi zaiflik aynan macro qiymatda ko'rinadi.
- **Weighted** = 0.80 · 0.860 + 0.15 · 0.400 + 0.05 · 0.333 = **0.765** — natija Sog'lom sinfi hisobiga ko'tarilgan va accuracy kabi kichik sinflardagi muammoni yashiradi.
- **Micro** = 85 / (85 + 15 + 15) = **0.739**.

<h3>Nega Jaccard F1'dan past chiqadi?</h3>

Kovid uchun F1 = 0.500, Jaccard esa 0.333. Sababi:

- **F1** to'g'ri topilganlarni **ikki marta** hisoblaydi: $\frac{2 \cdot 3}{2 \cdot 3 + 4 + 2} = \frac{6}{12} = 0.5$
- **Jaccard** to'g'ri topilganlarni **bir marta** hisoblaydi: $\frac{3}{3 + 4 + 2} = \frac{3}{9} = 0.333$

Demak, Jaccard xatolarga nisbatan qattiqroq. F1 va Jaccard orasida aniq bog'liqlik bor:

$$
J = \frac{F1}{2 - F1} \qquad \text{masalan: } \frac{0.5}{2 - 0.5} = 0.333
$$

F1 va Jaccard doim bir xil yo'nalishda harakat qiladi: F1 o'ssa, Jaccard ham o'sadi. Modellarni solishtirishda ikkala metrika bir xil xulosa beradi, faqat Jaccard sonlari pastroq bo'ladi.

Qayerda ishlatiladi: ko'proq rasm segmentatsiyasida. Segmentatsiyada "model belgilagan soha haqiqiy soha bilan qanchalik ustma-ust tushdi" degan savol aynan Jaccard ma'nosiga to'g'ri keladi. Multi-label masalalarda ham ishlatiladi.

---

<h2>Nomutanosiblik tuzog'i: "dangasa" model</h2>

"Dangasa" model hech narsa o'rganmagan va **har doim "Sog'lom"** deb javob beradi. Dangasa modelning confusion matrix'i:

| Haqiqiy ↓ / Bashorat → | Sog'lom | Gripp | Kovid |
|---|---|---|---|
| **Sog'lom** | 80 | 0 | 0 |
| **Gripp** | 15 | 0 | 0 |
| **Kovid** | 5 | 0 | 0 |

| Metrika | Asosiy model | Dangasa model | Dangasa model fosh bo'ldimi? |
|---|---|---|---|
| Accuracy | 0.85 | **0.80** | Yo'q, model yaxshi ko'rinadi |
| Weighted-F1 | 0.851 | 0.711 | Yo'q, farq kichik |
| Balanced Accuracy | 0.686 | 0.333 | Ha |
| Macro-F1 | 0.665 | 0.296 | Ha |
| Macro Jaccard | 0.531 | 0.267 | Ha |
| Cohen's Kappa | 0.555 | **0** | Ha, "tasodifdan yaxshi emas" |
| MCC | 0.556 | **0** | Ha, "tasodifdan yaxshi emas" |

*! Dangasa model **bitta ham kasalni topmaydi**, lekin accuracy 80% chiqadi. Nomutanosib datasetda accuracy'ga ishonmaslik kerakligining sababi aynan dangasa model misolida ko'rinadi.*

---

<h2>Yakuniy jadval</h2>

| Metrika | Asosiy model natijasi | Sodda savol | Qachon foydali |
|---|---|---|---|
| Accuracy | 0.85 | Nechta javob to'g'ri? | Faqat sinflar muvozanatli bo'lsa |
| Precision (macro) | 0.656 | "Kasal" degan javobga ishonsa bo'ladimi? | Yolg'on xavotir qimmat bo'lsa (spam filtri) |
| Recall (macro) | 0.686 | Kasallarning nechtasi topildi? | O'tkazib yuborish xavfli bo'lsa (tibbiyot, firibgarlik) |
| Specificity (macro) | 0.866 | Sog'lomlar bekorga kasal deyilmadimi? | Sog'lomlarni to'g'ri rad etish muhim bo'lsa |
| F1 (macro) | 0.665 | Precision va recall birgalikda qanday? | Precision va recall'ni muvozanatlash kerak bo'lsa |
| Balanced Accuracy | 0.686 | Har bir sinf o'rtacha qanday topildi? | Nomutanosib datasetda accuracy o'rniga |
| Cohen's Kappa | 0.555 | Tasodifdan qanchalik yaxshi? | Tasodifdan farqni o'lchash, annotatorlar kelishuvi |
| MCC | 0.556 | Bashorat haqiqat bilan qanchalik bog'liq? | Nomutanosib datasetda eng ishonchli yagona son |
| Jaccard (macro) | 0.531 | Bashorat va haqiqat qanchalik ustma-ust tushdi? | Segmentatsiya, multi-label masalalar |

---

<h2>Metrika tanlash bo'yicha yo'riqnoma</h2>

1. **Sinflar teng bo'lsa** — accuracy yetarli.
2. **Sinflar nomutanosib bo'lsa** — accuracy o'rniga **MCC**, **balanced accuracy** yoki **macro-F1**.
3. **Kasalni o'tkazib yuborish xavfli bo'lsa** — asosiy e'tibor **recall** qiymatiga qaratiladi.
4. **Yolg'on xavotir qimmat bo'lsa** — asosiy e'tibor **precision** qiymatiga qaratiladi.
5. **Bitta son bilan baholash kerak bo'lsa** — **MCC**. "Hamma javobni bir xil aytish" kabi hiyla MCC'ni alday olmaydi.
6. **Har doim** har bir sinf bo'yicha alohida natijalar ham tekshiriladi. Umumiy son ba'zan muammoni yashiradi.

---

<h2>Python'da tekshirish</h2>

```python
from sklearn.metrics import (classification_report, balanced_accuracy_score,
                             cohen_kappa_score, matthews_corrcoef,
                             jaccard_score, confusion_matrix)
import numpy as np

# Confusion matrix'dan y_true va y_pred ni qayta tiklash
cm = np.array([[74, 4, 2],
               [5, 8, 2],
               [1, 1, 3]])
y_true = np.repeat([0,0,0,1,1,1,2,2,2], cm.flatten())
y_pred = np.repeat([0,1,2,0,1,2,0,1,2], cm.flatten())

names = ["Sog'lom", "Gripp", "Kovid"]
print(classification_report(y_true, y_pred, target_names=names, digits=3))
print("Balanced Acc:", balanced_accuracy_score(y_true, y_pred))
print("Kappa:       ", cohen_kappa_score(y_true, y_pred))
print("MCC:         ", matthews_corrcoef(y_true, y_pred))
print("Jaccard macro:", jaccard_score(y_true, y_pred, average="macro"))

# Specificity: sklearn'da tayyor funksiya yo'q, qo'lda hisoblanadi
cm = confusion_matrix(y_true, y_pred)
for i, name in enumerate(names):
    TP = cm[i, i]
    FN = cm[i, :].sum() - TP
    FP = cm[:, i].sum() - TP
    TN = cm.sum() - TP - FN - FP
    print(f"{name} specificity: {TN / (TN + FP):.3f}")
```

---

<h2>Qisqa xulosa</h2>

- **Confusion matrix** — qatorlar haqiqatni, ustunlar bashoratni ko'rsatadi, diagonal esa to'g'ri javoblar.
- **TP / FN / FP / TN** — FN qatordan, FP ustundan topiladi.
- **Accuracy** — nechta javob to'g'ri. Nomutanosib datasetda aldaydi.
- **Precision** — "model aytgan javoblarning qanchasi to'g'ri?"
- **Recall** — "mavjud holatlarning qanchasi topildi?"
- **Specificity** — "tanlangan sinfga tegishli bo'lmagan obyektlar to'g'ri rad etildimi?"
- **F1** — precision va recall'ning garmonik o'rtachasi.
- **Macro / Weighted / Micro** — macro sinflarni teng ko'radi va nomutanosiblikda eng adolatli.
- **Balanced Accuracy** — recall qiymatlarining oddiy o'rtachasi. Accuracy bilan farq katta bo'lsa, kichik sinflarda muammo bor.
- **Cohen's Kappa** — tasodifiy to'g'ri javoblar chiqarib tashlangandan keyingi natija.
- **MCC** — −1 dan +1 gacha korrelyatsiya, 0 tasodifni bildiradi. Nomutanosiblikda eng ishonchli yagona son.
- **Jaccard** — kesishma / birlashma. F1'ning qattiqroq versiyasi.
- **Dangasa model** accuracy'ni aldaydi, MCC va Kappa'ni alday olmaydi.
