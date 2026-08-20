# Logistic Regression

**Logistic Regression** — nomida “regression” so‘zi bo‘lsa ham, asosan
klassifikatsiya masalalarida ishlatiladigan algoritm. Model obyektning ma’lum
sinfga tegishli bo‘lish ehtimolini hisoblaydi.

Masalan:

- elektron xat spam yoki spam emas;
- mijoz kreditni qaytaradi yoki qaytarmaydi;
- bemorda kasallik bor yoki yo‘q;
- talaba imtihondan o‘tadi yoki o‘tmaydi.

Binary klassifikatsiyada natija ikki sinfdan iborat:

$$
y\in\{0,1\}
$$

Odatda `0` — manfiy sinf, `1` esa musbat sinf sifatida belgilanadi.

---

## 1. Linear Regression bilan asosiy farqi

Simple Linear Regression quyidagi qiymatni hisoblaydi:

$$
\hat{y}=b_0+b_1x
$$

Natija istalgan haqiqiy son, masalan $-3$, $0.7$ yoki $15$ bo‘lishi mumkin.
Klassifikatsiyada esa $0$ va $1$ oralig‘idagi ehtimollik kerak:

$$
0\leq P(y=1\mid x)\leq1
$$

Logistic Regression chiziqli ifodani avval hisoblaydi:

$$
z=b_0+b_1x
$$

Keyin $z$ qiymatini sigmoid funksiyasi orqali ehtimollikka aylantiradi.

---

## 2. Sigmoid funksiyasi

Sigmoid funksiyasi:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Logistic Regression modeli:

$$
p=P(y=1\mid x)=\sigma(b_0+b_1x)
$$

Sigmoid har qanday haqiqiy sonni $(0,1)$ oralig‘iga o‘tkazadi:

| $z$ | $\sigma(z)$ | Talqin |
| --: | ----------: | ------ |
| $-5$ | $0.0067$ | `1`-sinf ehtimoli juda past |
| $-1$ | $0.2689$ | `1`-sinf ehtimoli past |
| $0$ | $0.5000$ | Ikki sinf chegarasi |
| $1$ | $0.7311$ | `1`-sinf ehtimoli yuqori |
| $5$ | $0.9933$ | `1`-sinf ehtimoli juda yuqori |

$z$ oshganda ehtimollik `1` ga, $z$ kamayganda esa `0` ga yaqinlashadi.

---

## 3. Kichik dataset

Quyidagi misolda:

- $x$ — o‘qish soati;
- $y=0$ — imtihondan o‘tmagan;
- $y=1$ — imtihondan o‘tgan.

| Obyekt | O‘qish soati $x$ | Natija $y$ |
| -----: | ----------------: | ---------: |
|      1 |                 1 |          0 |
|      2 |                 2 |          0 |
|      3 |                 3 |          0 |
|      4 |                 4 |          1 |
|      5 |                 5 |          1 |
|      6 |                 6 |          1 |

Maqsad — o‘qish soati asosida imtihondan o‘tish ehtimolini hisoblash.

---

## 4. Ehtimollikni qo‘lda hisoblash

Tushuntiruvchi misol sifatida quyidagi koeffitsiyentlar berilgan bo‘lsin:

$$
b_0=-5,\qquad b_1=1.5
$$

Model:

$$
z=-5+1.5x
$$

$$
P(y=1\mid x)=\frac{1}{1+e^{-(-5+1.5x)}}
$$

$x=4$ uchun avval chiziqli qiymat hisoblanadi:

$$
z=-5+1.5\cdot4=1
$$

Keyin sigmoid qo‘llanadi:

$$
p=\frac{1}{1+e^{-1}}\approx0.731
$$

Demak, model $x=4$ bo‘lgan obyekt uchun `1`-sinf ehtimolini taxminan
$73.1\%$ deb baholaydi.

Bu bo‘limdagi $b_0=-5$ va $b_1=1.5$ qiymatlari hisoblash jarayonini
ko‘rsatish uchun berilgan. Koeffitsiyentlar amalda ma’lumotdan optimizatsiya
orqali o‘rganiladi.

---

## 5. Ehtimollikdan sinfga o‘tish

Logistic Regression dastlab `0` yoki `1` emas, ehtimollik qaytaradi. Sinf
olish uchun **threshold**, ya’ni chegara qiymati tanlanadi. Masalan,
$t=0.5$ bo‘lsa:

$$
\hat{y}=
\begin{cases}
1, & p\geq0.5,\\
0, & p<0.5.
\end{cases}
$$

Yuqoridagi misolda $p=0.731$ bo‘lgani sababli bashorat `1` bo‘ladi.

Threshold har doim `0.5` bo‘lishi shart emas:

- kasallikni o‘tkazib yuborish xavfli bo‘lsa, threshold pasaytirilishi mumkin;
- noto‘g‘ri musbat bashorat qimmatga tushsa, threshold oshirilishi mumkin.

Threshold o‘zgarishi precision va recall orasidagi muvozanatni o‘zgartiradi.

---

## 6. Qaror chegarasi

$0.5$ threshold uchun sinflar chegarasi $p=0.5$ nuqtada joylashadi. Sigmoid
funksiyasida $\sigma(0)=0.5$, shuning uchun:

$$
b_0+b_1x=0
$$

Bitta alomatli modelning qaror chegarasi:

$$
x=-\frac{b_0}{b_1}
$$

$b_0=-5$ va $b_1=1.5$ uchun:

$$
x=-\frac{-5}{1.5}\approx3.33
$$

$x$ qiymati taxminan `3.33` dan katta bo‘lsa, model `1`-sinfga moyil bo‘ladi.

---

## 7. Koeffitsiyentlar qanday topiladi?

$b_0$ va $b_1$ qiymatlari variantlarni ko‘r-ko‘rona sinash orqali
tanlanmaydi. Optimal qiymatlar **Maximum Likelihood Estimation** orqali
topiladi. Bu jarayon Binary Cross-Entropy yoki **Log Loss** funksiyasini
minimallashtirishga teng.

Bitta obyekt uchun loss:

$$
L_i=-\left[y_i\ln(p_i)+(1-y_i)\ln(1-p_i)\right]
$$

Dataset bo‘yicha o‘rtacha loss:

$$
J(b_0,b_1)=
-\frac{1}{m}\sum_{i=1}^{m}
\left[y_i\ln(p_i)+(1-y_i)\ln(1-p_i)\right]
$$

Maqsad:

$$
J(b_0,b_1)\rightarrow\min
$$

Log Loss quyidagi xususiyatga ega:

- to‘g‘ri sinfga yuqori ehtimollik berilsa, loss kichik bo‘ladi;
- noto‘g‘ri sinfga katta ishonch bildirilsa, loss juda katta bo‘ladi.

Masalan, haqiqiy sinf $y=1$ bo‘lsa:

$$
L=-\ln(p)
$$

| Bashorat $p$ | Loss $-\ln(p)$ |
| -----------: | -------------: |
|         0.90 |          0.105 |
|         0.60 |          0.511 |
|         0.10 |          2.303 |
|         0.01 |          4.605 |

---

## 8. Gradient qanday hisoblanadi?

Log Lossning koeffitsiyentlar bo‘yicha hosilalari gradientni beradi:

$$
\frac{\partial J}{\partial b_0}
=\frac{1}{m}\sum_{i=1}^{m}(p_i-y_i)
$$

$$
\frac{\partial J}{\partial b_1}
=\frac{1}{m}\sum_{i=1}^{m}(p_i-y_i)x_i
$$

Gradient loss eng tez oshadigan yo‘nalishni ko‘rsatadi. Lossni kamaytirish
uchun koeffitsiyentlar gradientga qarama-qarshi yo‘nalishda yangilanadi:

$$
b_j:=b_j-\alpha\frac{\partial J}{\partial b_j}
$$

Bu yerda $\alpha$ — **learning rate**, ya’ni qadam kattaligi.

---

## 9. Gradient Descentning birinchi qadami

Yuqoridagi dataset va boshlang‘ich qiymatlar:

$$
b_0=0,\qquad b_1=0
$$

Barcha obyektlar uchun:

$$
z_i=0,\qquad p_i=\sigma(0)=0.5
$$

Haqiqiy qiymatlar va xatoliklar:

$$
y=[0,0,0,1,1,1]
$$

$$
p-y=[0.5,0.5,0.5,-0.5,-0.5,-0.5]
$$

Intercept gradienti:

$$
\frac{\partial J}{\partial b_0}
=\frac{0.5+0.5+0.5-0.5-0.5-0.5}{6}=0
$$

$b_1$ gradienti:

$$
\begin{aligned}
\frac{\partial J}{\partial b_1}
&=\frac{1}{6}\sum_{i=1}^{6}(p_i-y_i)x_i\\
&=\frac{0.5\cdot1+0.5\cdot2+0.5\cdot3
-0.5\cdot4-0.5\cdot5-0.5\cdot6}{6}\\
&=-0.75
\end{aligned}
$$

$\alpha=0.1$ bo‘lsa, birinchi yangilanish:

$$
b_0:=0-0.1\cdot0=0
$$

$$
b_1:=0-0.1\cdot(-0.75)=0.075
$$

Yangi model:

$$
z=0.075x
$$

Keyingi iteratsiyada ehtimolliklar, gradientlar va koeffitsiyentlar qayta
hisoblanadi. Loss yetarlicha kamayguncha yoki to‘xtash sharti bajarilguncha
jarayon davom etadi.

Birinchi qadamda dataset simmetriyasi sababli $b_0$ gradienti nol chiqdi.
Keyingi qadamlarda ehtimolliklar o‘zgargani uchun $b_0$ ham yangilanadi.

---

## 10. Nega bu perebor emas?

Perebor barcha mumkin bo‘lgan koeffitsiyent juftliklarini navbat bilan sinab
ko‘rishni talab qiladi. Gradient Descent esa hosila yordamida loss qaysi
yo‘nalishda kamayishini aniqlaydi.

Jarayonning qisqa ko‘rinishi:

1. Koeffitsiyentlarga boshlang‘ich qiymat beriladi.
2. $z=X\beta$ hisoblanadi.
3. $p=\sigma(z)$ orqali ehtimolliklar olinadi.
4. Log Loss va gradient hisoblanadi.
5. Koeffitsiyentlar $\beta:=\beta-\alpha\nabla J$ orqali yangilanadi.
6. To‘xtash sharti bajarilguncha qadamlar takrorlanadi.

Logistic Regression uchun oddiy Linear Regressiondagi kabi yopiq ko‘rinishdagi
normal tenglama mavjud emas. Koeffitsiyentlar iterativ optimizatsiya orqali
topiladi. Amaliy kutubxonalar `lbfgs`, `liblinear`, `newton-cg`, `sag` yoki
`saga` kabi optimizatorlardan foydalanishi mumkin.

---

## 11. Matritsa ko‘rinishi

Bir nechta alomatli dataset uchun:

$$
z=X\beta
$$

$$
p=\sigma(X\beta)
$$

$$
J(\beta)=-\frac{1}{m}
\left[y^T\ln(p)+(1-y)^T\ln(1-p)\right]
$$

Gradient:

$$
\nabla J=\frac{1}{m}X^T(p-y)
$$

Yangilanish:

$$
\beta:=\beta-\alpha\nabla J
$$

Intercept $X$ matritsadagi `1` lar ustuni yoki alohida parametr orqali
ifodalanadi.

---

## 12. Bir nechta alomatli model

$n$ ta kiruvchi alomat uchun chiziqli qism:

$$
z=b_0+b_1x_1+b_2x_2+\cdots+b_nx_n
$$

Ehtimollik:

$$
P(y=1\mid x_1,\ldots,x_n)
=\frac{1}{1+e^{-z}}
$$

Masalan, imtihondan o‘tish ehtimoli quyidagi alomatlar orqali baholanishi
mumkin:

- $x_1$ — o‘qish soati;
- $x_2$ — yechilgan testlar soni;
- $x_3$ — uyqu soati.

Model:

$$
z=b_0+b_1x_1+b_2x_2+b_3x_3
$$

Har bir koeffitsiyent boshqa alomatlar o‘zgarmagan holatda tegishli alomatning
log-odds qiymatiga ta’sirini bildiradi.

---

## 13. Log-odds va koeffitsiyent talqini

Ehtimollikdan **odds** quyidagicha olinadi:

$$
\text{odds}=\frac{p}{1-p}
$$

Logistic Regression log-odds qiymatini chiziqli modellashtiradi:

$$
\ln\left(\frac{p}{1-p}\right)
=b_0+b_1x_1+\cdots+b_nx_n
$$

$x_j$ bir birlikka oshganda log-odds $b_j$ ga o‘zgaradi, odds esa $e^{b_j}$
marta o‘zgaradi. Masalan:

- $b_j>0$ bo‘lsa, `1`-sinf ehtimoli oshishga moyil;
- $b_j<0$ bo‘lsa, `1`-sinf ehtimoli kamayishga moyil;
- $b_j=0$ bo‘lsa, alomat chiziqli qaror qiymatiga ta’sir qilmaydi.

Koeffitsiyent kattaligini alomatlar turli birliklarda bo‘lganda to‘g‘ridan
to‘g‘ri solishtirish noto‘g‘ri bo‘lishi mumkin. Standartlashtirish talqinni va
optimizatsiyani yengillashtiradi.

---

## 14. Regularizatsiya

Amaliy Logistic Regression ko‘pincha koeffitsiyentlarning haddan tashqari
kattalashishini cheklovchi regularizatsiyadan foydalanadi.

L2 regularizatsiyali loss:

$$
J_{L2}(\beta)=J(\beta)+\lambda\sum_{j=1}^{n}b_j^2
$$

Regularizatsiya:

- overfitting xavfini kamaytiradi;
- kuchli bog‘langan alomatlarda modelni barqarorlashtiradi;
- mukammal ajraladigan sinflarda koeffitsiyentlarning cheksiz o‘sishini
  cheklaydi.

Yuqoridagi kichik datasetda `0` va `1` sinflari mukammal ajraladi. Shu sababli
regularizatsiyasiz Maximum Likelihood koeffitsiyentlari chekli optimumga ega
bo‘lmasligi mumkin. Amaliy kutubxonalardagi regularizatsiya chekli va barqaror
yechim olishga yordam beradi.

---

## 15. Modelni baholash

Faqat accuracy qiymatiga tayanish, ayniqsa sinflar nomutanosib bo‘lsa, noto‘g‘ri
xulosa berishi mumkin. Asosiy baholash vositalari:

| Metrika | Ko‘rsatadigan jihat |
| ------- | ------------------- |
| Accuracy | Barcha bashoratlarning to‘g‘ri ulushi |
| Precision | `1` deb topilgan obyektlarning qanchasi haqiqatan `1` ekani |
| Recall | Haqiqiy `1` obyektlarning qanchasi topilgani |
| F1-score | Precision va recallning muvozanatli o‘rtachasi |
| ROC-AUC | Turli thresholdlarda sinflarni ajratish qobiliyati |
| Log Loss | Bashorat ehtimolliklarining sifati |

Confusion matrix `true positive`, `true negative`, `false positive` va
`false negative` holatlarini alohida ko‘rsatadi.

---

## 16. Python orqali misol

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, log_loss

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

X_new = np.array([[3.5], [4.5]])
probabilities = model.predict_proba(X_new)
classes = model.predict(X_new)

print("b0:", model.intercept_)
print("b1:", model.coef_)
print("Probabilities:", probabilities)
print("Classes:", classes)

y_probability = model.predict_proba(X)[:, 1]
y_pred = model.predict(X)

print("Log Loss:", log_loss(y, y_probability))
print(classification_report(y, y_pred))
```

`predict_proba` har bir sinf ehtimolini qaytaradi. Binary klassifikatsiyada
ikkinchi ustun odatda `1`-sinf ehtimolidir. `predict` esa tanlangan threshold
asosida yakuniy sinfni qaytaradi.

Katta loyihalarda preprocessing va model bitta `Pipeline` ichiga joylanadi.
Model train ma’lumotida o‘rgatiladi, test ma’lumotida esa alohida baholanadi.

---

## 17. Ko‘p sinfli klassifikatsiya

Logistic Regression binary klassifikatsiyadan tashqari uch yoki undan ko‘p
sinf uchun ham qo‘llanishi mumkin.

Asosiy yondashuvlar:

- **One-vs-Rest** — har bir sinf qolgan barcha sinflarga qarshi o‘rgatiladi;
- **Multinomial Logistic Regression** — barcha sinflar ehtimoli softmax orqali
  birgalikda modellashtiriladi.

Ko‘p sinfli holatda barcha sinf ehtimollari yig‘indisi `1` ga teng bo‘ladi.

---

## 18. Qachon yaxshi ishlaydi?

Logistic Regression quyidagi holatlarda yaxshi boshlang‘ich model hisoblanadi:

- maqsad klassifikatsiya bo‘lsa;
- ehtimollik kerak bo‘lsa;
- sinflar taxminan chiziqli chegara bilan ajralsa;
- koeffitsiyentlarni tushuntirish muhim bo‘lsa;
- tez va sodda baseline model kerak bo‘lsa.

Model quyidagi holatlarda qiynalishi mumkin:

- sinflar orasidagi chegara juda murakkab bo‘lsa;
- kuchli nochiziqli bog‘liqliklar mavjud bo‘lsa;
- muhim interaction alomatlar modelga kiritilmagan bo‘lsa;
- kuchli outlierlar yoki noto‘g‘ri masshtablangan alomatlar optimizatsiyaga
  xalaqit bersa.

Polynomial va interaction alomatlar qo‘shish ayrim nochiziqli chegaralarni
ifodalashi mumkin, lekin model murakkabligi va overfitting xavfi ham oshadi.

---

## 19. Linear va Logistic Regression farqi

| Jihat | Linear Regression | Logistic Regression |
| ----- | ----------------- | ------------------- |
| Vazifa | Sonli qiymatni bashorat qilish | Sinfni yoki sinf ehtimolini bashorat qilish |
| Natija | Istalgan haqiqiy son | `0` va `1` oralig‘idagi ehtimollik |
| Asosiy funksiya | Chiziqli funksiya | Chiziqli funksiya va sigmoid |
| Loss | Odatda MSE | Log Loss |
| Koeffitsiyentlar | Yopiq formula yoki optimizatsiya | Iterativ optimizatsiya |
| Qaror | Sonli bashorat | Threshold orqali sinf |

“Regression” nomi log-odds qiymatining kiruvchi alomatlarga nisbatan chiziqli
modellashtirilishidan kelib chiqadi. Yakuniy vazifa esa klassifikatsiya bo‘ladi.

---

## 20. Muhim xulosa

Logistic Regressionning asosiy jarayoni:

$$
X\longrightarrow z=X\beta
\longrightarrow p=\sigma(z)
\longrightarrow \hat{y}
$$

Bu yerda:

1. Chiziqli qiymat hisoblanadi.
2. Sigmoid qiymatni ehtimollikka aylantiradi.
3. Threshold ehtimollikni sinfga aylantiradi.
4. Log Loss ehtimollik xatosini o‘lchaydi.
5. Gradient yoki boshqa optimizator koeffitsiyentlarni yangilaydi.

Koeffitsiyentlar perebor orqali emas, Log Lossni minimallashtiruvchi matematik
optimizatsiya orqali topiladi. Model natijasi avval ehtimollik, keyin esa
vazifaga mos threshold asosidagi sinfdir.
