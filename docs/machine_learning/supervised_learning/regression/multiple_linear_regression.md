# Multiple Linear Regression

**Multiple Linear Regression** — bu bir nechta kiruvchi belgilar orqali bitta
sonli natijani bashorat qilish usuli.

$$
\hat{y}=b_0+b_1x_1+b_2x_2+\cdots+b_nx_n
$$

Bu yerda:

- $\hat{y}$ — model bashorati
- $x_1, x_2, \ldots, x_n$ — kiruvchi alomatlar
- $b_0$ — intercept, ya’ni boshlang‘ich qiymat
- $b_1, b_2, \ldots, b_n$ — har bir alomatning ta’sir koeffitsiyenti

---

## 1. Oddiy misol

Masalan, talabaning test balini bashorat qilmoqchimiz.

- $x_1$ — o‘qish soati
- $x_2$ — yechilgan testlar soni
- $y$ — yakuniy test bali

Dataset:

| Talaba | O‘qish soati $x_1$ | Yechilgan testlar $x_2$ | Test bali $y$ |
| -----: | -----------------: | ----------------------: | ------------: |
|      1 |                  1 |                       1 |            52 |
|      2 |                  2 |                       1 |            58 |
|      3 |                  2 |                       2 |            63 |
|      4 |                  3 |                       2 |            68 |
|      5 |                  4 |                       3 |            78 |

Maqsad: $x_1$ va $x_2$ orqali $y$ ni bashorat qiluvchi model qurish.

---

## 2. Model ko‘rinishi

Bizda ikkita kiruvchi alomat bor. Shuning uchun model:

$$
\hat{y}=b_0+b_1x_1+b_2x_2
$$

Bu yerda:

- $b_0$ — boshlang‘ich qiymat
- $b_1$ — o‘qish soatining ta’siri
- $b_2$ — yechilgan testlar sonining ta’siri

---

## 3. Model koeffitsiyentlarini topish

Multiple Linear Regressionda koeffitsiyentlar odatda **Least Squares**, ya’ni
**eng kichik kvadratlar usuli** orqali topiladi.

Asosiy g‘oya:

> Haqiqiy $y$ bilan model bashorati $\hat{y}$ orasidagi xatoliklar kvadratlari
> yig‘indisi eng kichik bo‘lishi kerak.

Xatolik:

$$
e_i = y_i - \hat{y}_i
$$

Umumiy xatolik:

$$
SSE = \sum (y_i-\hat{y}_i)^2
$$

Model shu `SSE` qiymatini imkon qadar kichik qiladi.

---

## 4. Matrix ko‘rinish

Multiple Linear Regressionda hisoblashni matrix ko‘rinishda yozish qulay.

Datasetni quyidagicha yozamiz:

$$
X=
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 2 & 2 \\
1 & 3 & 2 \\
1 & 4 & 3
\end{bmatrix}
$$

Bu yerda birinchi ustun hammasi `1`. Chunki u $b_0$, ya’ni intercept uchun
kerak.

Natijalar vektori:

$$
y=
\begin{bmatrix}
52 \\
58 \\
63 \\
68 \\
78
\end{bmatrix}
$$

Koeffitsiyentlar vektori:

$$
\beta=
\begin{bmatrix}
b_0 \\
b_1 \\
b_2
\end{bmatrix}
$$

Asosiy formula:

$$
\beta=(X^TX)^{-1}X^Ty
$$

Bu formula orqali $b_0$, $b_1$ va $b_2$ topiladi.

---

## 5. Bizning dataset uchun natija

Endi Multiple Linear Regression koeffitsiyentlari qanday hisoblanishini aynan
shu formula ichidan ochib ko‘ramiz:

$$
\beta=(X^TX)^{-1}X^Ty
$$

Bu formula orqali quyidagi uchta qiymat topiladi:

$$
\beta=
\begin{bmatrix}
b_0 \\
b_1 \\
b_2
\end{bmatrix}
$$

Ya’ni $b_0$, $b_1$ va $b_2$ ni topamiz.

---

## 5.1. Avval `X` matritsani tuzamiz

Datasetda ikkita feature bor:

$$
x_1,\qquad x_2
$$

Lekin modelda yana $b_0$ ham bor. Shuning uchun `X` matritsaga boshidan `1`
lar ustuni qo‘shiladi.

$$
X=
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 2 & 2 \\
1 & 3 & 2 \\
1 & 4 & 3
\end{bmatrix}
$$

Bu yerda:

- 1-ustun — $b_0$ uchun
- 2-ustun — $x_1$
- 3-ustun — $x_2$

Natijalar vektori:

$$
y=
\begin{bmatrix}
52 \\
58 \\
63 \\
68 \\
78
\end{bmatrix}
$$

---

## 5.2. $X^T$ ni topamiz

$X^T$ — bu `X` matritsaning transponirlangan ko‘rinishi. Ya’ni satrlar ustunga,
ustunlar satrga aylanadi.

$$
X=
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 2 & 2 \\
1 & 3 & 2 \\
1 & 4 & 3
\end{bmatrix}
$$

Demak:

$$
X^T=
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
1 & 2 & 2 & 3 & 4 \\
1 & 1 & 2 & 2 & 3
\end{bmatrix}
$$

---

## 5.3. Endi $X^TX$ ni hisoblaymiz

Formula bo‘yicha birinchi kerakli qism:

$$
X^TX
$$

Ya’ni:

$$
X^T \cdot X
$$

Hisoblash natijasi:

$$
X^TX=
\begin{bmatrix}
5 & 12 & 9 \\
12 & 34 & 25 \\
9 & 25 & 19
\end{bmatrix}
$$

Bu qayerdan chiqdi?

$$
5 = 1^2+1^2+1^2+1^2+1^2
$$

$$
12 = 1+2+2+3+4
$$

$$
9 = 1+1+2+2+3
$$

Shu tarzda ustunlar bir-biriga ko‘paytirib yig‘iladi.

---

## 5.4. Endi $X^Ty$ ni hisoblaymiz

Ikkinchi kerakli qism:

$$
X^Ty
$$

Ya’ni:

$$
X^T \cdot y
$$

$$
X^T=
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
1 & 2 & 2 & 3 & 4 \\
1 & 1 & 2 & 2 & 3
\end{bmatrix}
$$

$$
y=
\begin{bmatrix}
52 \\
58 \\
63 \\
68 \\
78
\end{bmatrix}
$$

Natija:

$$
X^Ty=
\begin{bmatrix}
319 \\
810 \\
606
\end{bmatrix}
$$

Buni ochib ko‘rsak:

$$
319 = 52+58+63+68+78
$$

$$
810 = 1\cdot52+2\cdot58+2\cdot63+3\cdot68+4\cdot78
$$

$$
606 = 1\cdot52+1\cdot58+2\cdot63+2\cdot68+3\cdot78
$$

---

## 5.5. Tenglamalar sistemasini hosil qilamiz

Aslida quyidagi formula:

$$
\beta=(X^TX)^{-1}X^Ty
$$

shuni anglatadi:

$$
X^TX\beta=X^Ty
$$

Ya’ni:

$$
\begin{bmatrix}
5 & 12 & 9 \\
12 & 34 & 25 \\
9 & 25 & 19
\end{bmatrix}
\begin{bmatrix}
b_0 \\
b_1 \\
b_2
\end{bmatrix}
=
\begin{bmatrix}
319 \\
810 \\
606
\end{bmatrix}
$$

Buni oddiy tenglamalar ko‘rinishida yozamiz:

$$
5b_0+12b_1+9b_2=319
$$

$$
12b_0+34b_1+25b_2=810
$$

$$
9b_0+25b_1+19b_2=606
$$

Endi masala oddiylashdi. Biz mana shu 3 ta tenglamadan 3 ta noma’lumni topamiz:

$$
b_0,\qquad b_1,\qquad b_2
$$

---

## 5.6. Tenglamalar sistemasini yechamiz

Sistema:

$$
5b_0+12b_1+9b_2=319
$$

$$
12b_0+34b_1+25b_2=810
$$

$$
9b_0+25b_1+19b_2=606
$$

Yechim:

$$
b_0=42.2
$$

$$
b_1=5.4
$$

$$
b_2=4.8
$$

Demak:

$$
\beta=
\begin{bmatrix}
42.2 \\
5.4 \\
4.8
\end{bmatrix}
$$

---

## 5.7. Yakuniy model

Endi koeffitsiyentlarni modelga qo‘yamiz:

$$
\hat{y}=b_0+b_1x_1+b_2x_2
$$

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

Mana shu — bizning Multiple Linear Regression modeli.

---

## 5.8. Eng muhim tushuncha

Quyidagi formula bir qarashda murakkab ko‘rinadi:

$$
\beta=(X^TX)^{-1}X^Ty
$$

Lekin ichki ma’nosi oddiy:

1. Datasetdan `X` matritsa tuziladi.
2. `X` transponirlanadi: $X^T$.
3. $X^TX$ hisoblanadi.
4. $X^Ty$ hisoblanadi.
5. Quyidagi tenglamalar sistemasi yechiladi:

$$
X^TX\beta=X^Ty
$$

6. Natijada $b_0$, $b_1$ va $b_2$ topiladi.

---

## 5.9. Nega $(X^TX)^{-1}$ kerak?

Oddiy algebra esingda bo‘lsa:

$$
2x=10
$$

Bu yerda:

$$
x=\frac{10}{2}=5
$$

Matrixlarda esa bo‘lish amali yo‘q. Shuning uchun matrixlarda “bo‘lish”
o‘rniga teskari matritsa, ya’ni **inverse**, ishlatiladi.

Shuning uchun:

$$
X^TX\beta=X^Ty
$$

dan:

$$
\beta=(X^TX)^{-1}X^Ty
$$

kelib chiqadi.

Oddiy qilib aytganda, $(X^TX)^{-1}$ matrixlarda bo‘lish vazifasini bajaradi.

---

## 6. Modelni tushunamiz

Model:

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

Bu nimani anglatadi?

**$b_0 = 42.2$**

Agar talaba 0 soat o‘qisa va 0 ta test yechsa, model boshlang‘ich qiymat
sifatida taxminan 42.2 ball beradi.

Bu har doim real ma’noda to‘g‘ri bo‘lishi shart emas. Lekin matematik modelda
chiziq yoki tekislikning boshlang‘ich nuqtasi sifatida kerak.

**$b_1 = 5.4$**

Yechilgan testlar soni o‘zgarmasa, o‘qish soati 1 soatga oshganda test bali
o‘rtacha 5.4 ballga oshadi.

Muhim joyi: $x_2$ doimiy deb olinadi. Ya’ni $b_1$ ni talqin qilayotganda
$x_2$ ta’siri ajratib turiladi.

**$b_2 = 4.8$**

O‘qish soati o‘zgarmasa, yechilgan testlar soni 1 taga oshganda test bali
o‘rtacha 4.8 ballga oshadi.

Multiple Linear Regressiondagi eng muhim tushuncha:

> Har bir koeffitsiyent boshqa belgilar o‘zgarmagan holatda shu belgining
> $y$ ga ta’sirini bildiradi.

---

## 7. Bashorat qilish

Masalan, yangi talaba:

- $x_1=5$ — 5 soat o‘qigan
- $x_2=4$ — 4 ta test yechgan

Model:

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

Qiymatlarni qo‘yamiz:

$$
\hat{y}=42.2+5.4\cdot5+4.8\cdot4
$$

$$
\hat{y}=42.2+27+19.2
$$

$$
\hat{y}=88.4
$$

Demak, model bashorati:

$$
\hat{y}=88.4
$$

Ya’ni talaba taxminan **88.4 ball** olishi mumkin.

---

## 8. Modelning datasetdagi bashoratlari

Endi har bir talaba uchun model bashoratini ko‘ramiz.

Model:

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

| Talaba | $x_1$ | $x_2$ | Haqiqiy $y$ | Bashorat $\hat{y}$ | Xato $(y-\hat{y})$ |
| -----: | ----: | ----: | ----------: | -----------------: | -----------------: |
|      1 |     1 |     1 |          52 |               52.4 |               -0.4 |
|      2 |     2 |     1 |          58 |               57.8 |                0.2 |
|      3 |     2 |     2 |          63 |               62.6 |                0.4 |
|      4 |     3 |     2 |          68 |               68.0 |                0.0 |
|      5 |     4 |     3 |          78 |               78.2 |               -0.2 |

Ko‘rib turibmiz, bashoratlar haqiqiy qiymatlarga juda yaqin.

---

## 9. $R^2$ orqali baholash

Regression model sifatini baholash uchun $R^2$ ishlatiladi.

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
SSE = 0.4
$$

$$
SST = 392.8
$$

$$
R^2 = 1 - \frac{0.4}{392.8}
$$

$$
R^2 \approx 0.999
$$

Bu juda yuqori natija. Ya’ni model datasetdagi o‘zgarishlarning deyarli
hammasini tushuntiryapti.

Lekin bu yerda ehtiyot bo‘lish kerak: dataset juda kichik. Real loyihalarda
$R^2$ bunchalik yuqori chiqsa, modelni albatta test datasetda ham tekshirish
kerak.

---

## 10. Simple va Multiple Linear Regression farqi

| Jihat | Simple Linear Regression | Multiple Linear Regression |
| ----- | ------------------------ | -------------------------- |
| Kiruvchi belgilar soni | 1 ta | 2 yoki undan ko‘p |
| Formula | $\hat{y}=b_0+b_1x$ | $\hat{y}=b_0+b_1x_1+b_2x_2+\cdots+b_nx_n$ |
| Misol | O‘qish soati → test bali | O‘qish soati + testlar soni → test bali |
| Geometrik ko‘rinish | Chiziq | Tekislik yoki ko‘p o‘lchamli tekislik |
| Talqin qilish | Osonroq | Har bir belgi alohida tahlil qilinadi |

---

## 11. Geometrik ma’nosi

Simple Linear Regressionda model to‘g‘ri chiziq topadi.

Multiple Linear Regressionda esa:

- agar 2 ta feature bo‘lsa — tekislik topadi
- agar 3 yoki undan ko‘p feature bo‘lsa — ko‘p o‘lchamli tekislik, ya’ni
  hyperplane topadi

Bizning misolda:

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

Bu 3D fazoda tekislik bo‘ladi:

- $x_1$ — o‘qish soati
- $x_2$ — testlar soni
- $y$ — test bali

Model shu nuqtalarga eng yaqin joylashgan tekislikni topadi.

---

## 12. Multiple Linear Regression qachon ishlatiladi?

Quyidagi holatlarda ishlatiladi:

| Masala | Featurelar | Natija |
| ------ | ---------- | ------ |
| Uy narxini bashorat qilish | maydon, xona soni, joylashuv | uy narxi |
| Ish haqini bashorat qilish | tajriba, bilim darajasi, sertifikatlar | oylik |
| Test balini bashorat qilish | o‘qish soati, testlar soni, uyqu vaqti | test bali |
| Sotuvni bashorat qilish | reklama, narx, chegirma | sotuv hajmi |
| Tarmoq trafigini baholash | paket soni, kechikish, bandwidth | ishlash ko‘rsatkichi |

---

## 13. Muhim muammo: multicollinearity

Multiple Linear Regressionda bitta muhim muammo bor: featurelar bir-biriga juda
o‘xshash bo‘lib qolishi.

Masalan:

- $x_1$ — o‘qish soati
- $x_2$ — tayyorgarlik vaqti

Bu ikkalasi deyarli bir xil ma’no berishi mumkin.

Agar featurelar bir-biriga juda kuchli bog‘langan bo‘lsa, model
koeffitsiyentlari noto‘g‘ri yoki beqaror chiqishi mumkin. Bunga
**multicollinearity** deyiladi.

Oddiy aytganda:

> Model qaysi feature haqiqatan ta’sir qilayotganini ajrata olmay qoladi.

---

## 14. Python orqali qisqa ko‘rinishi

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Dataset
X = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [3, 2],
    [4, 3]
])

y = np.array([52, 58, 63, 68, 78])

# Model
model = LinearRegression()
model.fit(X, y)

# Koeffitsiyentlar
print("b0:", model.intercept_)
print("b1, b2:", model.coef_)

# Bashorat
y_pred = model.predict(X)
print("Predictions:", y_pred)

# Baholash
print("R2:", r2_score(y, y_pred))
print("MAE:", mean_absolute_error(y, y_pred))

# Yangi talaba uchun bashorat
new_student = np.array([[5, 4]])
print("New prediction:", model.predict(new_student))
```

Natija taxminan:

```text
b0: 42.2
b1, b2: [5.4 4.8]
R2: 0.999
New prediction: 88.4
```

---

## 15. Yakuniy xulosa

Multiple Linear Regressionning asosiy g‘oyasi:

> Bitta natijaga bir nechta omillar ta’sir qilsa, model ularning har birining
> ta’sirini alohida koeffitsiyentlar orqali baholaydi.

Bizning misolda model:

$$
\hat{y}=42.2+5.4x_1+4.8x_2
$$

Bu shuni bildiradi:

- o‘qish soati oshsa, test bali oshadi
- yechilgan testlar soni oshsa, test bali oshadi
- har bir omilning alohida ta’siri sonli koeffitsiyent orqali ifodalanadi

Eng muhim joyi: Multiple Linear Regression faqat bashorat qilmaydi, balki qaysi
feature natijaga qanday ta’sir qilayotganini ham tushuntirib beradi.
