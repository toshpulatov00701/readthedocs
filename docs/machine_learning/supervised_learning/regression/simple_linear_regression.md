# Simple Linear Regression

**Simple Linear Regression** — bu bitta kiruvchi belgi `x` orqali
bitta chiqish qiymati `y` ni bashorat qilish usuli.

Masalan:

> `x` — talabaning o‘qish soati
>
> `y` — testdan olgan bali

Maqsad: o‘qish soati oshsa, test bali qanday o‘zgarishini chiziqli model orqali
topish.

---

## 1. Asosiy formula

$$
y = b_0 + b_1x
$$

Bu yerda:

- `y` — haqiqiy qiymat yoki bashorat qilinadigan natija
- `x` — kiruvchi alomat     
- `b0` — intercept, ya’ni chiziqning boshlang‘ich nuqtasi
- `b1` — slope, ya’ni `x` 1 birlikka oshganda `y` qancha o‘zgarishi

Amalda model quyidagicha yoziladi:

$$
\hat{y} = b_0 + b_1x
$$

Bu yerda $\hat{y}$ — model bashorati.

---

## 2. Kichik test dataset

| Talaba | O‘qish soati `x` | Test bali `y` |
| ------ | ---------------: | ------------: |
| 1      |                1 |            50 |
| 2      |                2 |            55 |
| 3      |                3 |            65 |
| 4      |                4 |            70 |
| 5      |                5 |            75 |

Biz shu dataset orqali model quramiz.

---

## 3. O‘rtacha qiymatlarni topamiz

$$
\bar{x} = \frac{1+2+3+4+5}{5} = 3
$$

$$
\bar{y} = \frac{50+55+65+70+75}{5} = 63
$$

Demak:

$$
\bar{x}=3,\qquad \bar{y}=63
$$

---

## 4. `b1` koeffitsiyentini topamiz

Formula:

$$
b_1 = \frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sum (x_i-\bar{x})^2}
$$

Hisoblaymiz:

| `x` | `y` | $(x_i-\bar{x})$ | $(y_i-\bar{y})$ | Ko‘paytma | Kvadrat |
| --: | --: | --------------: | --------------: | --------: | ------: |
|   1 |  50 |              -2 |             -13 |        26 |       4 |
|   2 |  55 |              -1 |              -8 |         8 |       1 |
|   3 |  65 |               0 |               2 |         0 |       0 |
|   4 |  70 |               1 |               7 |         7 |       1 |
|   5 |  75 |               2 |              12 |        24 |       4 |

$$
\sum (x_i-\bar{x})(y_i-\bar{y}) = 65
$$

$$
\sum (x_i-\bar{x})^2 = 10
$$

Shuning uchun:

$$
b_1 = \frac{65}{10} = 6.5
$$

Demak, **o‘qish soati 1 soatga oshsa, test bali o‘rtacha 6.5 ballga oshadi**.

---

## 5. `b0` ni topamiz

Formula:

$$
b_0 = \bar{y} - b_1\bar{x}
$$

Qiymatlarni qo‘yamiz:

$$
b_0 = 63 - 6.5 \cdot 3
$$

$$
b_0 = 63 - 19.5 = 43.5
$$

Demak:

$$
b_0 = 43.5
$$

---

## 6. Yakuniy regression modeli

$$
\hat{y} = 43.5 + 6.5x
$$

Bu model shuni anglatadi:

> Talaba 0 soat o‘qisa, model taxminan 43.5 ball beradi.
>
> Har bir qo‘shimcha 1 soat o‘qish test balini taxminan 6.5 ballga oshiradi.

---

## 7. Bashorat qilish

Masalan, talaba **6 soat** o‘qisa:

$$
\hat{y} = 43.5 + 6.5 \cdot 6
$$

$$
\hat{y} = 43.5 + 39 = 82.5
$$

Demak, model bashorati:

$$
\hat{y} = 82.5
$$

Ya’ni 6 soat o‘qigan talaba taxminan **82.5 ball** olishi mumkin.

---

## 8. Model xatoligini ko‘rish

Endi har bir `x` uchun model bashoratini hisoblaymiz:

| `x` | Haqiqiy `y` | Bashorat $\hat{y}$ | Xato $(y-\hat{y})$ |
| --: | ----------: | -----------------: | -----------------: |
|   1 |          50 |                 50 |                  0 |
|   2 |          55 |               56.5 |               -1.5 |
|   3 |          65 |                 63 |                  2 |
|   4 |          70 |               69.5 |                0.5 |
|   5 |          75 |                 76 |                 -1 |

Model xatolari juda katta emas. Demak, bu kichik datasetda chiziqli regressiya
yaxshi ishlayapti.

---

## 9. `R²` orqali sifatni baholash

Regressionda ko‘p ishlatiladigan baholash metrikasi:

$$
R^2 = 1 - \frac{SSE}{SST}
$$

Bu yerda:

$$
SSE = \sum (y_i-\hat{y}_i)^2
$$

$$
SST = \sum (y_i-\bar{y})^2
$$

Bizning misolda:

$$
SSE = 7.5
$$

$$
SST = 430
$$

$$
R^2 = 1 - \frac{7.5}{430}
$$

$$
R^2 \approx 0.9826
$$

Demak, model ma’lumotlardagi o‘zgarishning taxminan **98.26%** qismini
tushuntiryapti. Bu juda yaxshi natija.

---

## 10. Simple Linear Regression qachon ishlatiladi?

Simple Linear Regression quyidagi holatlarda ishlatiladi:

1. Kiruvchi belgi faqat bitta bo‘lsa.
2. `x` va `y` orasida chiziqli bog‘liqlik bo‘lsa.
3. Natija sonli qiymat bo‘lsa.
4. Maqsad bashorat qilish yoki bog‘liqlikni tushuntirish bo‘lsa.

Masalan:

| `x`              | `y`          |
| ---------------- | ------------ |
| O‘qish soati     | Test bali    |
| Reklama xarajati | Sotuv hajmi  |
| Uy maydoni       | Uy narxi     |
| Tajriba yili     | Ish haqi     |
| Harorat          | Elektr sarfi |

---

## 11. Muhim xulosa

Simple Linear Regressionning asosiy g‘oyasi juda oddiy:

> Berilgan nuqtalarga eng yaqin o‘tuvchi to‘g‘ri chiziq topiladi va shu chiziq
> orqali yangi qiymatlar bashorat qilinadi.

Bizning misolda model:

$$
\hat{y} = 43.5 + 6.5x
$$

Bu modelga ko‘ra, o‘qish soati qancha oshsa, test bali ham shuncha oshadi.
Lekin real hayotda bog‘liqlik har doim bunday ideal bo‘lmaydi. Shuning uchun
regressiondan oldin datasetni grafikda ko‘rish, xatoliklarni tekshirish va
model sifati metrikalarini hisoblash kerak.
