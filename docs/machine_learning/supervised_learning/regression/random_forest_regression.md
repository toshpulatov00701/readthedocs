# Random Forest Regression

**Random Forest Regression** — ko‘plab Decision Tree Regression modellarini
birlashtirib, uzluksiz sonli qiymatni bashorat qiluvchi ansambl algoritmi.

Masalan:

- uy narxini bashorat qilish;
- hosildorlik miqdorini aniqlash;
- suv yoki elektr sarfini baholash;
- havo haroratini bashorat qilish;
- mahsulotga talabni prognozlash.

Nomdagi uchta so‘z algoritmning asosiy g‘oyasini ifodalaydi:

- **Tree** — bitta qaror daraxti;
- **Forest** — ko‘plab qaror daraxtlari;
- **Random** — obyektlar va alomatlar tasodifiy tanlanadi.

Bitta daraxt o‘rniga turlicha daraxtlar quriladi va ularning bashoratlari
o‘rtachalanadi. Bu yondashuv **bagging** deb ataladi.

---

## 1. Kichik dataset

Quyidagi datasetda tayyorlanish vaqti orqali imtihon natijasi bashorat qilinadi:

| Obyekt | Tayyorlanish vaqti $x$ | Natija $y$ |
| -----: | ----------------------: | ---------: |
|      1 |                       1 |         10 |
|      2 |                       2 |         14 |
|      3 |                       3 |         15 |
|      4 |                       4 |         25 |
|      5 |                       5 |         28 |
|      6 |                       6 |         30 |

Maqsad — $x_{\text{new}}=3.5$ uchun $y$ qiymatini bashorat qilish.

Linear Regression bitta umumiy tenglama quradi:

$$
\hat{y}=b_0+b_1x
$$

Random Forest Regression esa turli daraxtlardagi `if–else` qoidalarini
birlashtiradi. Shu sababli bitta yopiq regressiya tenglamasi mavjud emas.

---

## 2. Random Forest qanday ishlaydi?

Algoritmning asosiy bosqichlari:

1. Har bir daraxt uchun trening datasetidan bootstrap namuna olinadi.
2. Har bir bootstrap namuna asosida regression daraxti quriladi.
3. Har bir tugunda alomatlarning tasodifiy qismigina tekshiriladi.
4. Har bir daraxt yangi obyekt uchun alohida bashorat beradi.
5. Barcha daraxtlarning bashoratlari o‘rtachalanadi.

$B$ ta daraxt uchun yakuniy bashorat:

$$
\boxed{\hat{y}(x)=\frac{1}{B}\sum_{b=1}^{B}T_b(x)}
$$

Bu yerda $T_b(x)$ — $b$-daraxtning bashorati.

---

## 3. Bootstrap Sampling

Bootstrap — asl datasetdan obyektlarni **takrorlanish bilan** tasodifiy tanlash
usuli.

Asl indekslar:

$$
D=[1,2,3,4,5,6]
$$

Uchta daraxt uchun namunalar quyidagicha bo‘lishi mumkin:

$$
D_1=[1,2,2,4,5,6]
$$

$$
D_2=[1,3,3,4,5,6]
$$

$$
D_3=[2,3,4,4,5,6]
$$

Natijada:

- ayrim obyektlar bir necha marta qatnashadi;
- ayrim obyektlar ma’lum bir daraxtga umuman tushmaydi;
- har bir daraxt biroz boshqacha ma’lumotda o‘rganadi.

Barcha daraxtlar aynan bir xil ma’lumotda qurilsa, ularning tuzilishi va
xatolari ham o‘xshash bo‘lib qolishi mumkin. Bootstrap daraxtlar orasidagi
farqni oshiradi.

---

## 4. Bitta daraxt qanday quriladi?

Birinchi bootstrap namuna:

$$
D_1=[1,2,2,4,5,6]
$$

Unga mos ma’lumotlar:

| $x$ | $y$ |
| --: | --: |
|   1 |  10 |
|   2 |  14 |
|   2 |  14 |
|   4 |  25 |
|   5 |  28 |
|   6 |  30 |

Takrorlangan $x=2$ qiymatlari bitta noyob qiymat sifatida qaraladi. Nomzod
chegaralar qo‘shni noyob qiymatlarning o‘rtasidan olinadi:

$$
1.5,\quad3,\quad4.5,\quad5.5
$$

Har bir $s$ chegara uchun chap va o‘ng guruhlar:

$$
R_L(s)=\{(x_i,y_i):x_i\leq s\}
$$

$$
R_R(s)=\{(x_i,y_i):x_i>s\}
$$

Bo‘linish xatoligi:

$$
Q(s)=
\sum_{i\in R_L}(y_i-\bar{y}_L)^2+
\sum_{i\in R_R}(y_i-\bar{y}_R)^2
$$

Daraxt quyidagi chegarani tanlaydi:

$$
s^*=\arg\min_s Q(s)
$$

---

## 5. $s=3$ chegarasini hisoblash

$x\leq3$ sharti uchun chap targetlar:

$$
y_L=[10,14,14]
$$

$$
\bar{y}_L=\frac{10+14+14}{3}\approx12.67
$$

$$
Q_L\approx10.67
$$

O‘ng targetlar:

$$
y_R=[25,28,30]
$$

$$
\bar{y}_R=\frac{25+28+30}{3}\approx27.67
$$

$$
Q_R\approx12.67
$$

Umumiy xatolik:

$$
\boxed{Q(3)=Q_L+Q_R\approx23.34}
$$

Barcha chegaralar taqqoslanadi:

| Chegara $s$ | Umumiy xatolik $Q(s)$ |
| ----------: | ---------------------: |
|         1.5 |                 236.80 |
|         3.0 |                  23.34 |
|         4.5 |                 126.75 |
|         5.5 |                 244.80 |

Eng kichik xatolik $s=3$ da hosil bo‘lgani uchun ildiz tugun quyidagicha
bo‘ladi:

```text
                 x ≤ 3?
                /      \
              Ha        Yo‘q
        [10, 14, 14]  [25, 28, 30]
```

---

## 6. Daraxtning keyingi bo‘linishlari

Chap guruhdagi eng yaxshi chegara $x\leq1.5$, o‘ng guruhdagi eng yaxshi
chegara esa $x\leq4.5$ bo‘lsin. Daraxt:

```text
                       x ≤ 3?
                     /        \
                   Ha          Yo‘q
               x ≤ 1.5?      x ≤ 4.5?
               /      \      /       \
             10       14    25        29
```

Oxirgi bargdagi `29` qiymati shu bargga tushgan targetlarning o‘rtachasidir:

$$
\frac{28+30}{2}=29
$$

Regression daraxtining umumiy barg bashorati:

$$
\boxed{\hat{y}_{\text{leaf}}
=\frac{1}{n_{\text{leaf}}}\sum_{i=1}^{n_{\text{leaf}}}y_i}
$$

---

## 7. Daraxtlar bashoratini o‘rtachalash

$x_{\text{new}}=3.5$ uchun uchta tushuntiruvchi daraxt quyidagi bashoratlarni
bergan bo‘lsin:

| Daraxt | Bashorat |
| -----: | -------: |
| $T_1$ | 25 |
| $T_2$ | 15 |
| $T_3$ | 15 |

Random Forest natijasi:

$$
\hat{y}=\frac{25+15+15}{3}\approx18.33
$$

Ushbu uchta daraxt va `18.33` natijasi algoritmni tushuntirish uchun berilgan
kichik misoldir. Haqiqiy modeldagi bootstrap namunalar va bashoratlar
`random_state`, daraxt parametrlari hamda realizatsiyaga bog‘liq.

---

## 8. Alomatlar qanday tasodifiy tanlanadi?

Random Forestda tasodifiylik ikki joyda ishlatiladi:

1. Har bir daraxt uchun obyektlar bootstrap orqali tanlanadi.
2. Har bir tugunda alomatlarning tasodifiy qismi tanlanadi.

Masalan, uy narxini bashorat qilish uchun oltita alomat mavjud bo‘lsin:

1. maydon;
2. xonalar soni;
3. qavat;
4. markazgacha masofa;
5. uy yoshi;
6. tuman.

Oddiy Decision Tree har bir tugunda barcha alomatlarni tekshirishi mumkin.
Random Forest esa $m_{\text{try}}=2$ bo‘lsa, ildiz tugunda tasodifan faqat
`maydon` va `masofa` alomatlarini ko‘rishi mumkin.

```text
Ildiz tugun:  Maydon, Masofa
Chap tugun:   Xonalar soni, Qavat
O‘ng tugun:   Uy yoshi, Tuman
```

Tasodifiy alomatlar to‘plami **har bir tugunda yangidan** tanlanadi. Bir
tugunda tanlanmagan alomat o‘chirilmaydi; u shu daraxtning boshqa tugunida
yoki boshqa daraxtda qatnashishi mumkin.

---

## 9. Nega tasodifiy alomatlar kerak?

Agar juda kuchli bitta alomat har bir tugunda doim mavjud bo‘lsa, ko‘p
daraxtlar aynan shu alomat bilan bir xil yoki juda o‘xshash tarzda bo‘linishi
mumkin. Kuchli korrelyatsiyalangan daraxtlarni o‘rtachalashning foydasi
cheklangan bo‘ladi.

Alomatlar qismi tasodifiy tanlanganda ayrim daraxtlar boshqa foydali
alomatlardan foydalanishga majbur bo‘ladi. Natijada:

- daraxtlar bir-biridan ko‘proq farq qiladi;
- daraxtlar orasidagi korrelyatsiya kamayadi;
- o‘rtacha bashorat barqarorroq bo‘ladi;
- bitta daraxtga xos overfitting ta’siri kamayadi.

Bootstrap va tasodifiy alomat tanlash birgalikda o‘rmondagi xilma-xillikni
hosil qiladi.

---

## 10. To‘liq matematik ko‘rinish

Dataset:

$$
D=\{(x_i,y_i)\}_{i=1}^{n}
$$

Har bir $b$-daraxt uchun bootstrap namuna olinadi:

$$
D_b^*=\operatorname{Bootstrap}(D)
$$

Har bir tugunda tasodifiy alomatlar to‘plami $M_b$ ichidan alomat $j$ va
chegara $s$ tanlanadi:

$$
(j^*,s^*)=\arg\min_{j\in M_b,s}
\left[
\sum_{x_i\in R_L}(y_i-\bar{y}_L)^2+
\sum_{x_i\in R_R}(y_i-\bar{y}_R)^2
\right]
$$

Har bir daraxt $T_b(x)$ bashoratini beradi. O‘rmon bashorati:

$$
\boxed{\hat{y}(x)=\frac{1}{B}\sum_{b=1}^{B}T_b(x)}
$$

---

## 11. Nega bitta daraxtdan barqarorroq?

Bitta chuqur Decision Tree trening ma’lumotidagi kichik o‘zgarishlarga juda
sezgir. Dataset ozgina o‘zgarsa, daraxt tuzilishi va bashorati sezilarli
o‘zgarishi mumkin. Bu yuqori variance muammosidir.

Random Forest turli bootstrap namunalar va alomatlar bilan ko‘plab daraxtlar
quradi. Daraxtlarning xatolari to‘liq bir xil bo‘lmasa, o‘rtachalashtirish
tasodifiy xatolarni qisman muvozanatlashtiradi. Natijada variance odatda
kamayadi.

Daraxtlar sonining oshishi o‘rmonni avtomatik ravishda overfittingga olib
kelmaydi, lekin hisoblash va xotira sarfini oshiradi. Daraxt chuqurligi,
barg hajmi va alomatlar tanlovi baribir nazorat qilinadi.

---

## 12. Out-of-Bag ma’lumotlar

Bootstrap tanlashda ayrim trening obyektlari ma’lum bir daraxt namunasiga
tushmaydi. Bunday obyektlar **Out-of-Bag**, qisqacha **OOB** obyektlar deyiladi.

Bitta obyektning $n$ marta tanlash davomida umuman tanlanmaslik ehtimoli:

$$
\left(1-\frac{1}{n}\right)^n
$$

$n$ kattalashganda:

$$
\left(1-\frac{1}{n}\right)^n\approx e^{-1}\approx0.368
$$

Demak, har bir daraxt uchun trening obyektlarining taxminan `36.8%` qismi OOB
bo‘lib qoladi. Obyekt uchun faqat shu obyektni treningda ko‘rmagan daraxtlar
bashorati birlashtirilib, OOB score hisoblanadi.

```python
RandomForestRegressor(
    bootstrap=True,
    oob_score=True,
)
```

OOB score validation natijasining qulay ichki bahosini beradi, lekin yakuniy
test datasetini to‘liq almashtirmaydi.

---

## 13. Asosiy parametrlar

| Parametr | Vazifasi |
| -------- | -------- |
| `n_estimators` | O‘rmondagi daraxtlar sonini belgilaydi |
| `max_depth` | Har bir daraxtning maksimal chuqurligini cheklaydi |
| `min_samples_split` | Tugunni bo‘lish uchun zarur minimal obyektlar sonini belgilaydi |
| `min_samples_leaf` | Har bir bargdagi minimal obyektlar sonini belgilaydi |
| `max_features` | Har bir tugunda tasodifiy tekshiriladigan alomatlar ulushini yoki sonini belgilaydi |
| `bootstrap` | Bootstrap namuna ishlatilishini boshqaradi |
| `max_samples` | Har bir bootstrap namunadagi obyektlar sonini cheklaydi |
| `oob_score` | OOB baholashni yoqadi |
| `random_state` | Tasodifiy jarayonni takrorlanuvchan qiladi |
| `n_jobs` | Parallel ishlatiladigan protsessorlar sonini boshqaradi |

`n_estimators` oshganda bashorat odatda barqarorlashadi, lekin ma’lum nuqtadan
keyin sifatdagi o‘sish kichrayadi. `max_depth` juda kichik bo‘lsa underfitting,
juda katta va barglar juda kichik bo‘lsa overfitting xavfi paydo bo‘ladi.

---

## 14. Alomat muhimligi qanday aniqlanadi?

Impurity-based feature importance asosiy fikri:

> Qaysi alomat daraxt tugunlaridagi xatolikni ko‘proq kamaytirsa, shu alomat
> model uchun muhimroq hisoblanadi.

Boshlang‘ich targetlar:

$$
y=[100,120,200,220]
$$

O‘rtacha va boshlang‘ich MSE:

$$
\bar{y}=160
$$

$$
MSE_{\text{parent}}=
\frac{(100-160)^2+(120-160)^2+(200-160)^2+(220-160)^2}{4}
=2600
$$

`Maydon` alomati targetlarni `[100,120]` va `[200,220]` guruhlariga ajratsa,
ikkala guruh MSE qiymati `100` bo‘ladi. O‘lcham bilan vaznlangan keyingi
xatolik:

$$
MSE_{\text{after}}=\frac{2}{4}\cdot100+\frac{2}{4}\cdot100=100
$$

Xatolik kamayishi:

$$
\Delta MSE_{\text{maydon}}=2600-100=2500
$$

`Xonalar soni` alomati targetlarni `[100,200]` va `[120,220]` guruhlariga
ajratsa, keyingi MSE `2500` bo‘ladi:

$$
\Delta MSE_{\text{xonalar}}=2600-2500=100
$$

Faqat shu ikki hissa normallashtirilsa:

$$
Importance_{\text{maydon}}=\frac{2500}{2500+100}\approx0.9615
$$

$$
Importance_{\text{xonalar}}=\frac{100}{2500+100}\approx0.0385
$$

Random Forestda har bir alomat ishlatilgan barcha tugunlardagi vaznlangan
xatolik kamayishlari barcha daraxtlar bo‘yicha yig‘iladi va yig‘indi `1` ga
teng bo‘ladigan qilib normallashtiriladi.

---

## 15. Alomat muhimligini to‘g‘ri talqin qilish

Masalan, `feature_importances_` natijasi:

```text
Maydon         : 0.65
Xonalar soni   : 0.20
Uy yoshi       : 0.15
```

`Maydon = 0.65` qiymati targetning aynan `65%` qismi maydon sababli yuzaga
kelganini bildirmaydi. Bu daraxtlardagi normallashtirilgan xatolik kamayishining
katta qismi maydon ishlatilgan bo‘linishlarga to‘g‘ri kelganini bildiradi.

Muhim cheklovlar:

- alomat muhimligi sababiy bog‘lanishni isbotlamaydi;
- bir-biriga kuchli bog‘langan alomatlar muhimlikni bo‘lib olishi mumkin;
- ko‘p noyob qiymatga ega alomatlar impurity-based usulda ustun ko‘rinishi
  mumkin;
- ishonchliroq tekshiruv uchun test datasetidagi permutation importance ham
  hisoblanishi mumkin.

Tasodifiy tanlovga qaramay, foydali alomat ko‘plab daraxt va tugunlarda
xatolikni kamaytirsa, yuqori umumiy muhimlik oladi.

---

## 16. Bir nechta alomat bilan ishlash

Uy narxi datasetida uchta alomat bo‘lsin:

| Maydon | Xonalar | Uy yoshi | Narx |
| -----: | -------: | --------: | ----: |
|     50 |        2 |        15 |   300 |
|     60 |        2 |        10 |   350 |
|     75 |        3 |         8 |   430 |
|     90 |        4 |         5 |   550 |
|    110 |        4 |         2 |   700 |

$$
X=
\begin{bmatrix}
50 & 2 & 15\\
60 & 2 & 10\\
75 & 3 & 8\\
90 & 4 & 5\\
110 & 4 & 2
\end{bmatrix},
\qquad
y=
\begin{bmatrix}
300\\350\\430\\550\\700
\end{bmatrix}
$$

Har bir daraxt tugunida `maydon`, `xonalar` va `uy yoshi` alomatlarining
tasodifiy qismi tekshiriladi. Tanlangan qism ichidagi eng yaxshi
`alomat + chegara` juftligi ishlatiladi.

---

## 17. Python orqali model qurish

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

X = np.array([
    [50, 2, 15],
    [60, 2, 10],
    [75, 3, 8],
    [90, 4, 5],
    [110, 4, 2],
])

y = np.array([300, 350, 430, 550, 700])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
)

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=5,
    min_samples_leaf=1,
    max_features=1.0,
    bootstrap=True,
    oob_score=True,
    random_state=42,
    n_jobs=-1,
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
print("R2:", r2_score(y_test, y_pred))
print("OOB R2:", model.oob_score_)

new_house = np.array([[80, 3, 6]])
print("Yangi bashorat:", model.predict(new_house)[0])

feature_names = ["Maydon", "Xonalar", "Uy yoshi"]
for name, importance in zip(feature_names, model.feature_importances_):
    print(name, importance)
```

Ushbu besh qatorli dataset faqat kod tuzilishini ko‘rsatadi. Ishonchli train,
test va OOB baholash uchun ancha katta dataset talab qilinadi. Juda kichik
test to‘plamida $R^2$ beqaror yoki aniqlanmagan bo‘lishi mumkin.

---

## 18. Har bir daraxt bashoratini ko‘rish

```python
tree_predictions = [
    tree.predict(new_house)[0]
    for tree in model.estimators_
]

print("Daraxtlar bashorati:", tree_predictions)
print("O‘rtacha:", np.mean(tree_predictions))
print("Model bashorati:", model.predict(new_house)[0])
```

Oddiy Random Forest Regressionda `model.predict` natijasi alohida daraxtlar
bashoratining arifmetik o‘rtachasiga teng.

---

## 19. Modelni baholash

Random Forest Regression boshqa regression modellari kabi baholanadi:

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

$$
RMSE=\sqrt{MSE}
$$

$$
R^2=1-
\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
{\sum_{i=1}^{n}(y_i-\bar{y})^2}
$$

Model sifati trening natijasida emas, test datasetida yoki cross-validation
orqali aniqlanadi. Giperparametrlar validation natijasiga qarab tanlanadi.
Test dataset yakuniy tekshiruvgacha model tanlash jarayonidan chetda saqlanadi.

---

## 20. Ma’lumotlarni tayyorlash

Random Forest chegaralar orqali bo‘linadi va masofa hisoblamaydi. Shu sababli
sonli alomatlarni standartlashtirish yoki normallashtirish odatda talab
qilinmaydi.

Shunga qaramay:

- yo‘qolgan qiymatlar tanlangan kutubxona va versiyaga mos qayta ishlanadi;
- matnli kategoriyalar sonli ko‘rinishga o‘tkaziladi;
- kategoriyaga tartib ma’nosini noto‘g‘ri beruvchi oddiy raqamlashdan ehtiyot
  bo‘linadi;
- train va test qismlariga ajratish preprocessingdan oldin bajariladi;
- target leakage keltirib chiqaradigan ustunlar olib tashlanadi.

---

## 21. Afzalliklari

- chiziqli bo‘lmagan bog‘lanishlarni o‘rganadi;
- alomatlar orasidagi murakkab interactionlarni avtomatik aniqlaydi;
- bitta Decision Treedan barqarorroq;
- alomatlarni masshtablash odatda kerak emas;
- sonli bashorat va alomat muhimligini bera oladi;
- katta miqdordagi alomatlar bilan ishlaydi;
- OOB orqali qo‘shimcha ichki baholash imkonini beradi;
- daraxtlar parallel qurilishi mumkin.

---

## 22. Kamchiliklari

- bitta daraxtga qaraganda tushuntirish qiyinroq;
- ko‘p daraxt xotira va hisoblash vaqtini oshiradi;
- bashoratlar trening targetlari diapazonidan tashqariga yaxshi
  ekstrapolyatsiya qilmaydi;
- juda kichik datasetda natija beqaror bo‘lishi mumkin;
- impurity-based feature importance noto‘g‘ri talqin qilinishi mumkin;
- kuchli trendni formulaga aylantirib tushuntirish Linear Regressionga
  qaraganda qiyinroq.

---

## 23. Linear, Decision Tree va Random Forest farqi

| Xususiyat | Linear Regression | Decision Tree Regression | Random Forest Regression |
| --------- | ----------------- | ------------------------ | ------------------------ |
| Model | Bitta formula | Bitta daraxt | Ko‘plab daraxtlar |
| Bog‘lanish | Asosan chiziqli | Chiziqli bo‘lishi shart emas | Chiziqli bo‘lishi shart emas |
| Bashorat | Formula natijasi | Bitta barg qiymati | Barg qiymatlarining o‘rtachasi |
| Masshtablash | Ba’zan kerak | Odatda kerak emas | Odatda kerak emas |
| Overfitting | Nisbatan pastroq | Yuqori bo‘lishi mumkin | Bitta daraxtdan pastroq |
| Barqarorlik | Datasetga bog‘liq | Pastroq | Yuqoriroq |
| Tushuntirish | Koeffitsiyentlar | Qoidalar | Umumiy muhimlik va yordamchi usullar |
| Ekstrapolyatsiya | Mumkin | Yaxshi emas | Yaxshi emas |

---

## 24. Algoritmning ishlash tartibi

1. $B$ ta daraxt soni belgilanadi.
2. Har bir daraxt uchun bootstrap namuna olinadi.
3. Daraxtning har bir tugunida alomatlarning tasodifiy qismi tanlanadi.
4. Tanlangan alomatlardagi barcha nomzod chegaralar tekshiriladi.
5. Xatolikni eng ko‘p kamaytirgan bo‘linish tanlanadi.
6. To‘xtash sharti bajarilguncha tugunlar rekursiv bo‘linadi.
7. Har bir bargda targetlarning o‘rtacha qiymati saqlanadi.
8. Yangi obyekt barcha daraxtlardan o‘tkaziladi.
9. Daraxtlar bashoratining o‘rtachasi yakuniy natija bo‘ladi.

---

## 25. Muhim xulosa

Random Forest Regressionning uchta tayanch g‘oyasi:

1. **Bootstrap** — har bir daraxt turli obyektlar namunasida o‘rganadi.
2. **Tasodifiy alomatlar** — har bir tugunda alomatlarning faqat bir qismi
   tekshiriladi.
3. **O‘rtachalashtirish** — barcha daraxtlar bashorati birlashtiriladi.

Yakuniy formula:

$$
\boxed{\hat{y}(x)=\frac{1}{B}\sum_{b=1}^{B}T_b(x)}
$$

Tasodifiylik daraxtlarni turlicha qiladi, o‘rtachalashtirish esa ularning
tasodifiy xatolarini kamaytirib, bitta daraxtga qaraganda barqarorroq model
hosil qiladi.
