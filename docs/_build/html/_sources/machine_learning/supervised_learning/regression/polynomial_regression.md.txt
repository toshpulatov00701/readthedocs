# Polynomial Regression

**Polynomial Regression** — kiruvchi alomatlar va sonli natija orasidagi
chiziqli bo‘lmagan bog‘liqlikni darajali hadlar yordamida ifodalovchi
regressiya usuli.

Oddiy chiziqli regressiya to‘g‘ri chiziq quradi:

$$
\hat{y}=b_0+b_1x
$$

Polynomial Regression esa modelga $x^2$, $x^3$ kabi yangi alomatlarni
qo‘shadi:

$$
\hat{y}=b_0+b_1x+b_2x^2+\cdots+b_dx^d
$$

Bu yerda:

- $\hat{y}$ — model bashorati;
- $x$ — kiruvchi alomat;
- $d$ — polynomial daraja;
- $b_0,b_1,\ldots,b_d$ — o‘rganiladigan koeffitsiyentlar.

Polynomial Regression egri chiziq hosil qilsa ham, koeffitsiyentlarga nisbatan
chiziqli bo‘lgani uchun Linear Regression oilasiga kiradi.

---

## 1. Nega Polynomial Regression kerak?

Ba’zi ma’lumotlarda $x$ o‘zgarganda $y$ bir xil tezlikda o‘zgarmaydi.

| $x$ | $y$ | Oldingi qiymatdan farqi |
| --: | --: | ----------------------: |
|   0 |   2 |                       2 |
|   1 |   6 |                       4 |
|   2 |  12 |                       6 |
|   3 |  20 |                       8 |
|   4 |  30 |                      10 |

$y$ qiymatlari orasidagi farq `4, 6, 8, 10` ko‘rinishida oshmoqda. Demak,
bog‘liqlik to‘g‘ri chiziq emas. Bunday holatda ikkinchi darajali model mos
kelishi mumkin:

$$
\hat{y}=b_0+b_1x+b_2x^2
$$

---

## 2. Polynomial alomatlar qanday hosil qilinadi?

Bitta $x$ alomatidan ikkinchi daraja uchun ikkita alomat olinadi:

$$
x,\qquad x^2
$$

Yuqoridagi dataset quyidagi ko‘rinishga keladi:

| $x$ | $x^2$ | $y$ |
| --: | ----: | --: |
|   0 |     0 |   2 |
|   1 |     1 |   6 |
|   2 |     4 |  12 |
|   3 |     9 |  20 |
|   4 |    16 |  30 |

Shunday qilib, Polynomial Regression ikki bosqichda ishlaydi:

1. Asl alomatlardan polynomial alomatlar yaratiladi.
2. Hosil bo‘lgan alomatlarga Linear Regression qo‘llanadi.

---

## 3. Koeffitsiyentlarni topish

Ikkinchi darajali model uchun design matrix:

$$
X=
\begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 1 \\
1 & 2 & 4 \\
1 & 3 & 9 \\
1 & 4 & 16
\end{bmatrix},
\qquad
y=
\begin{bmatrix}
2 \\
6 \\
12 \\
20 \\
30
\end{bmatrix}
$$

Birinchi ustundagi `1` qiymatlari $b_0$ uchun, qolgan ustunlar esa $x$ va
$x^2$ uchun kerak.

Koeffitsiyentlar eng kichik kvadratlar usuli bilan topiladi. $X^TX$ teskari
matritsaga ega bo‘lsa, normal tenglama quyidagicha yoziladi:

$$
\beta=(X^TX)^{-1}X^Ty,
\qquad
\beta=
\begin{bmatrix}
b_0 \\
b_1 \\
b_2
\end{bmatrix}
$$

Ushbu dataset uchun:

$$
X^TX=
\begin{bmatrix}
5 & 10 & 30 \\
10 & 30 & 100 \\
30 & 100 & 354
\end{bmatrix},
\qquad
X^Ty=
\begin{bmatrix}
70 \\
210 \\
714
\end{bmatrix}
$$

Hosil bo‘lgan tenglamalar sistemasi:

$$
\begin{aligned}
5b_0+10b_1+30b_2 &= 70, \\
10b_0+30b_1+100b_2 &= 210, \\
30b_0+100b_1+354b_2 &= 714.
\end{aligned}
$$

Yechim:

$$
b_0=2,\qquad b_1=3,\qquad b_2=1
$$

Yakuniy model:

$$
\boxed{\hat{y}=2+3x+x^2}
$$

Amaliy kutubxonalar koeffitsiyentlarni topishda teskari matritsani bevosita
hisoblash o‘rniga barqarorroq sonli usullardan foydalanadi.

---

## 4. Modelni tekshirish va bashorat qilish

| $x$ | Haqiqiy $y$ | Bashorat $\hat{y}=2+3x+x^2$ | Xato $y-\hat{y}$ |
| --: | ----------: | ---------------------------: | ----------------: |
|   0 |           2 |                            2 |                 0 |
|   1 |           6 |                            6 |                 0 |
|   2 |          12 |                           12 |                 0 |
|   3 |          20 |                           20 |                 0 |
|   4 |          30 |                           30 |                 0 |

Masalan, $x=5$ uchun:

$$
\hat{y}=2+3\cdot5+5^2=42
$$

Model $42$ qiymatini bashorat qiladi. Jadvaldagi xatolarning nolga tengligi
faqat ushbu sun’iy dataset modelga aynan mos kelganini bildiradi. Yangi
ma’lumotlarda ham shunday natija chiqishi kafolatlanmaydi.

---

## 5. Bir nechta alomatli Polynomial Regression

Polynomial Regression faqat bitta alomat bilan cheklanmaydi. Ikki alomat
$x_1$ va $x_2$ bo‘lsa, ikkinchi darajali o‘zgartirish quyidagi alomatlarni
hosil qiladi:

$$
x_1,\quad x_2,\quad x_1^2,\quad x_1x_2,\quad x_2^2
$$

Model ko‘rinishi:

$$
\hat{y}=
b_0+b_1x_1+b_2x_2+b_3x_1^2+b_4x_1x_2+b_5x_2^2
$$

Masalan:

- $x_1$ — o‘qish soati;
- $x_2$ — yechilgan testlar soni;
- $y$ — test bali.

| $x_1$ | $x_2$ | $x_1^2$ | $x_1x_2$ | $x_2^2$ |
| ----: | ----: | --------: | ---------: | --------: |
|     1 |     1 |         1 |          1 |         1 |
|     2 |     1 |         4 |          2 |         1 |
|     2 |     2 |         4 |          4 |         4 |
|     3 |     2 |         9 |          6 |         4 |
|     4 |     3 |        16 |         12 |         9 |

Ikki asl alomat polynomial o‘zgartirishdan keyin beshta alomatga aylanadi.
Intercept qo‘shilganda design matrix oltita ustundan iborat bo‘ladi:

$$
X=
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 1 \\
1 & 2 & 1 & 4 & 2 & 1 \\
1 & 2 & 2 & 4 & 4 & 4 \\
1 & 3 & 2 & 9 & 6 & 4 \\
1 & 4 & 3 & 16 & 12 & 9
\end{bmatrix}
$$

---

## 6. Interaction term nima?

$x_1x_2$ — **interaction term**, ya’ni ikki alomatning birgalikdagi ta’siri.

Masalan, o‘qish soati va test yechish soni alohida ta’sir ko‘rsatishi mumkin.
Ikkala faoliyat birga bajarilganda qo‘shimcha ta’sir paydo bo‘lsa, $x_1x_2$
hadi shu bog‘liqlikni ifodalaydi.

- $x_1^2$ — birinchi alomatdagi egri chiziqli ta’sir;
- $x_2^2$ — ikkinchi alomatdagi egri chiziqli ta’sir;
- $x_1x_2$ — ikki alomatning birgalikdagi ta’siri.

Interaction term mavjudligi sabab-natija bog‘lanishini avtomatik ravishda
isbotlamaydi. U faqat ma’lumotdagi birgalikdagi statistik ta’sirni ifodalaydi.

---

## 7. Uchta alomat va undan yuqori darajalar

Uchta alomat va ikkinchi daraja uchun interceptsiz polynomial alomatlar:

$$
\begin{aligned}
&x_1,\ x_2,\ x_3,\\
&x_1^2,\ x_2^2,\ x_3^2,\\
&x_1x_2,\ x_1x_3,\ x_2x_3.
\end{aligned}
$$

Uchta asl alomat to‘qqizta polynomial alomatga aylanadi.

Ikki alomat va uchinchi daraja uchun esa quyidagi alomatlar hosil bo‘ladi:

$$
\begin{aligned}
&x_1,\ x_2,\\
&x_1^2,\ x_1x_2,\ x_2^2,\\
&x_1^3,\ x_1^2x_2,\ x_1x_2^2,\ x_2^3.
\end{aligned}
$$

Daraja oshgani sari alomatlar soni tez ko‘payadi.

---

## 8. Polynomial alomatlar soni

$m$ ta asl alomat va $d$ daraja uchun intercept bilan birga ustunlar soni:

$$
\binom{m+d}{d}
$$

Interceptsiz polynomial alomatlar soni:

$$
\binom{m+d}{d}-1
$$

| Asl alomatlar soni $m$ | Daraja $d$ | Interceptsiz alomatlar | Intercept bilan ustunlar |
| ----------------------: | ----------: | ---------------------: | -----------------------: |
|                       1 |           2 |                      2 |                        3 |
|                       2 |           2 |                      5 |                        6 |
|                       3 |           2 |                      9 |                       10 |
|                       5 |           2 |                     20 |                       21 |
|                       2 |           3 |                      9 |                       10 |
|                       3 |           3 |                     19 |                       20 |

Alomatlar sonining tez o‘sishi hisoblash xarajatini va overfitting xavfini
oshiradi.

---

## 9. Darajani tanlash

Polynomial daraja modelning egiluvchanligini belgilaydi:

| Daraja | Model ko‘rinishi | Geometrik ma’nosi |
| -----: | ---------------- | ----------------- |
|      1 | $b_0+b_1x$ | To‘g‘ri chiziq |
|      2 | $b_0+b_1x+b_2x^2$ | Parabola |
|      3 | $b_0+b_1x+b_2x^2+b_3x^3$ | Murakkabroq egri chiziq |

Juda kichik daraja murakkab bog‘liqlikni ifodalay olmaydi. Bu holat
**underfitting** deyiladi.

Juda katta daraja esa trening ma’lumotidagi tasodifiy shovqinni ham o‘rganib
olishi mumkin. Bu holat **overfitting** deyiladi. Overfitting kuzatilganda
trening natijasi yaxshi, test natijasi esa yomon bo‘ladi.

Daraja quyidagicha tanlanadi:

1. Ma’lumot train va test qismlariga ajratiladi yoki cross-validation
   qo‘llanadi.
2. Bir nechta daraja, masalan `1`, `2` va `3`, sinab ko‘riladi.
3. Har bir model MAE, RMSE yoki $R^2$ orqali baholanadi.
4. Test ma’lumotida yaxshi ishlaydigan eng sodda daraja tanlanadi.

Alomat qiymatlari katta darajaga oshirilganda sonlar juda kattalashishi
mumkin. Shu sababli ko‘p alomatli yoki yuqori darajali modellarda
standartlashtirish hamda Ridge yoki Lasso regularizatsiyasi foydali bo‘ladi.

---

## 10. Python orqali bitta alomatli misol

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[0], [1], [2], [3], [4]])
y = np.array([2, 6, 12, 20, 30])

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

print(poly.get_feature_names_out(["x"]))
print("b0:", model.intercept_)
print("b1, b2:", model.coef_)
print("MAE:", mean_absolute_error(y, y_pred))
print("R2:", r2_score(y, y_pred))

x_new = np.array([[5]])
x_new_poly = poly.transform(x_new)
print("Prediction:", model.predict(x_new_poly))
```

Natija:

```text
['x' 'x^2']
b0: 2.0
b1, b2: [3. 1.]
MAE: 0.0
R2: 1.0
Prediction: [42.]
```

`include_bias=False` ishlatilgan, chunki `LinearRegression` interceptni
alohida hisoblaydi.

---

## 11. Python orqali bir nechta alomatli misol

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [3, 2],
    [4, 3],
])

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

print(poly.get_feature_names_out(["x1", "x2"]))
print(X_poly)
```

Feature nomlari:

```text
['x1' 'x2' 'x1^2' 'x1 x2' 'x2^2']
```

Hosil bo‘lgan matritsa:

```text
[[ 1.  1.  1.  1.  1.]
 [ 2.  1.  4.  2.  1.]
 [ 2.  2.  4.  4.  4.]
 [ 3.  2.  9.  6.  4.]
 [ 4.  3. 16. 12.  9.]]
```

Ushbu `X_poly` matritsasi keyin `LinearRegression` modeliga beriladi.
Yangi obyektlar uchun doim `fit_transform` emas, avval o‘rgatilgan `poly`
obyektining `transform` metodi ishlatiladi.

---

## 12. Regression turlarining farqi

| Model | Asosiy formula | Asosiy xususiyat |
| ----- | -------------- | ---------------- |
| Simple Linear Regression | $\hat{y}=b_0+b_1x$ | Bitta alomat va to‘g‘ri chiziq |
| Multiple Linear Regression | $\hat{y}=b_0+b_1x_1+\cdots+b_mx_m$ | Bir nechta alomat va chiziqli ta’sir |
| Polynomial Regression | $\hat{y}=b_0+b_1x+b_2x^2+\cdots$ | Darajali va interaction alomatlar |

Multiple Linear Regression bir nechta asl alomatning chiziqli ta’sirini
o‘rganadi. Polynomial Regression esa asl alomatlardan darajali va o‘zaro
ko‘paytma alomatlar yaratib, chiziqli bo‘lmagan bog‘liqlikni ifodalaydi.

---

## 13. Qachon ishlatiladi?

Polynomial Regression quyidagi holatlarda foydali:

- scatter plot egri chiziqli bog‘liqlikni ko‘rsatsa;
- oddiy chiziqli model underfitting qilsa;
- alomatlar ta’siri tezlashib yoki sekinlashib borsa;
- alomatlarning birgalikdagi ta’sirini modelga kiritish kerak bo‘lsa;
- dataset hajmi yaratiladigan polynomial alomatlar soniga nisbatan yetarli
  bo‘lsa.

Misollar:

| Masala | Kiruvchi alomat | Natija |
| ------ | --------------- | ------ |
| Tajriba va ish haqi | tajriba yili | ish haqi |
| Harorat va energiya sarfi | harorat | elektr sarfi |
| Tezlik va yoqilg‘i sarfi | tezlik | yoqilg‘i sarfi |
| Reklama samaradorligi | reklama xarajati | sotuv hajmi |
| Biologik jarayon | vaqt | o‘sish yoki susayish darajasi |

Juda murakkab, keskin o‘zgaruvchan yoki ko‘p o‘lchamli bog‘liqliklarda daraxt
asosidagi modellar, boosting yoki boshqa nochiziqli usullar qulayroq bo‘lishi
mumkin.

---

## 14. Muhim xulosa

Polynomial Regressionning asosiy g‘oyasi — asl alomatlardan darajali va
interaction alomatlar yaratib, chiziqli bo‘lmagan bog‘liqlikni Linear
Regression yordamida o‘rganish.

Bitta alomat va ikkinchi daraja uchun:

$$
\hat{y}=b_0+b_1x+b_2x^2
$$

Ikki alomat va ikkinchi daraja uchun:

$$
\hat{y}=
b_0+b_1x_1+b_2x_2+b_3x_1^2+b_4x_1x_2+b_5x_2^2
$$

Daraja va alomatlar soni oshganda model kuchliroq bo‘ladi, lekin alomatlar
soni, hisoblash xarajati va overfitting xavfi ham oshadi. Shu sababli model
sifati alohida test ma’lumotida yoki cross-validation orqali baholanadi.
