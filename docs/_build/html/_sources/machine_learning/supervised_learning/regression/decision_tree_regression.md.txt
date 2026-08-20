# Decision Tree Regression

**Decision Tree Regression** — sonli qiymatni qarorlar daraxti yordamida
bashorat qiluvchi regressiya algoritmi.

Masalan:

- uy narxini bashorat qilish;
- havo haroratini aniqlash;
- suv yoki elektr sarfini baholash;
- oylik daromadni bashorat qilish;
- imtihon balini aniqlash.

Model ma’lumotlarni ketma-ket shartlar orqali kichik guruhlarga ajratadi. Har
bir yakuniy guruh, ya’ni barg uchun shu guruhdagi $y$ qiymatlarining o‘rtachasi
bashorat sifatida olinadi.

---

## 1. Asosiy g‘oya

Quyidagi kichik dataset berilgan bo‘lsin:

| Obyekt | O‘qish soati $x$ | Imtihon bali $y$ |
| -----: | ----------------: | ----------------: |
|      1 |                 1 |                10 |
|      2 |                 2 |                12 |
|      3 |                 3 |                13 |
|      4 |                 4 |                30 |
|      5 |                 5 |                32 |
|      6 |                 6 |                35 |

$x=1,2,3$ bo‘lganda ballar kichik, $x=4,5,6$ bo‘lganda esa katta. Daraxt
birinchi bosqichda quyidagi shartni topishi mumkin:

```text
O‘qish soati x ≤ 3.5 mi?
          /              \
        Ha                Yo‘q
   kichik ballar       katta ballar
```

Algoritm `3.5` chegarasini taxminan tanlamaydi. Barcha mumkin bo‘lgan
chegaralardagi xatoliklar hisoblanadi va eng kichik xatolik bergan chegara
tanlanadi.

---

## 2. Daraxtdagi asosiy tushunchalar

```text
                 x ≤ 3.5?
                /        \
              Ha          Yo‘q
          x ≤ 1.5?       x ≤ 5.5?
          /     \         /     \
        10     12.5      31      35
```

- **Root node** — eng yuqoridagi boshlang‘ich tugun;
- **internal node** — shart joylashgan ichki tugun;
- **branch** — shart natijasida tanlanadigan yo‘nalish;
- **split** — tugundagi ma’lumotlarni ikkiga ajratish;
- **leaf node** — yakuniy tugun va bashorat qiymati.

Regression daraxtida barg qiymati odatda shu bargga tushgan obyektlarning
o‘rtacha target qiymatidir.

---

## 3. Daraxt bo‘linmasa nima bo‘ladi?

Barcha target qiymatlari bitta ildiz tugunda joylashadi:

$$
y=[10,12,13,30,32,35]
$$

Tugundagi bashorat target qiymatlarining o‘rtachasiga teng:

$$
\bar{y}=\frac{10+12+13+30+32+35}{6}=22
$$

Daraxt bo‘linmasa, barcha obyektlar uchun:

$$
\hat{y}=22
$$

bashorat qilinadi. Bitta qiymat barcha obyektlarni yaxshi ifodalamagani uchun
daraxt foydali bo‘linishni izlaydi.

---

## 4. Tugundagi xatolik

Decision Tree Regression ko‘pincha **Squared Error** mezonidan foydalanadi.
Tugundagi kvadratik xatoliklar yig‘indisi:

$$
SSE=\sum_{i=1}^{n}(y_i-\bar{y})^2
$$

Ushbu dataset uchun:

$$
\begin{aligned}
SSE={}&(10-22)^2+(12-22)^2+(13-22)^2\\
&+(30-22)^2+(32-22)^2+(35-22)^2\\
={}&144+100+81+64+100+169\\
={}&658
\end{aligned}
$$

Daraxt bo‘linishdan keyingi umumiy xatolikni imkon qadar kamaytirishga
harakat qiladi.

---

## 5. Nomzod chegaralar qanday topiladi?

Tugundagi $x$ qiymatlari kichikdan kattaga saralanadi:

$$
1,\ 2,\ 3,\ 4,\ 5,\ 6
$$

Qo‘shni noyob qiymatlar orasidagi o‘rta nuqtalar nomzod chegara sifatida
olinadi:

$$
1.5,\ 2.5,\ 3.5,\ 4.5,\ 5.5
$$

Har bir $t$ chegara uchun ma’lumot ikki guruhga ajratiladi:

$$
R_L=\{(x_i,y_i):x_i\leq t\}
$$

$$
R_R=\{(x_i,y_i):x_i>t\}
$$

Bo‘linish xatoligi:

$$
SSE_{\text{split}}=SSE_L+SSE_R
$$

---

## 6. Birinchi nomzod: $x\leq1.5$

Chap guruhda faqat bitta target qiymati qoladi:

$$
y_L=[10],\qquad \bar{y}_L=10,\qquad SSE_L=0
$$

O‘ng guruh:

$$
y_R=[12,13,30,32,35]
$$

$$
\bar{y}_R=\frac{12+13+30+32+35}{5}=24.4
$$

$$
SSE_R=485.2
$$

Umumiy xatolik:

$$
SSE_{\text{split}}=0+485.2=485.2
$$

---

## 7. Ikkinchi nomzod: $x\leq2.5$

Chap guruh:

$$
y_L=[10,12],\qquad \bar{y}_L=11,\qquad SSE_L=2
$$

O‘ng guruh:

$$
y_R=[13,30,32,35],\qquad \bar{y}_R=27.5,\qquad SSE_R=293
$$

Umumiy xatolik:

$$
SSE_{\text{split}}=2+293=295
$$

---

## 8. Uchinchi nomzod: $x\leq3.5$

Chap guruh:

$$
y_L=[10,12,13],\qquad \bar{y}_L=\frac{35}{3}\approx11.67
$$

$$
SSE_L\approx4.67
$$

O‘ng guruh:

$$
y_R=[30,32,35],\qquad \bar{y}_R=\frac{97}{3}\approx32.33
$$

$$
SSE_R\approx12.67
$$

Umumiy xatolik:

$$
\boxed{SSE_{\text{split}}\approx17.34}
$$

Bu bo‘linish dastlabki xatolikni keskin kamaytiradi:

$$
658\longrightarrow17.34
$$

---

## 9. Eng yaxshi birinchi bo‘linish

Barcha nomzodlarning natijasi:

| Bo‘linish | Chap targetlar | O‘ng targetlar | Umumiy SSE |
| --------- | -------------- | -------------- | ----------: |
| $x\leq1.5$ | `[10]` | `[12,13,30,32,35]` | 485.20 |
| $x\leq2.5$ | `[10,12]` | `[13,30,32,35]` | 295.00 |
| $x\leq3.5$ | `[10,12,13]` | `[30,32,35]` | **17.34** |
| $x\leq4.5$ | `[10,12,13,30]` | `[32,35]` | 261.25 |
| $x\leq5.5$ | `[10,12,13,30,32]` | `[35]` | 455.20 |

Eng kichik xatolik $x\leq3.5$ shartida hosil bo‘ladi. Shuning uchun ildiz
tugunda shu shart tanlanadi:

```text
                    x ≤ 3.5?
                   /        \
                 Ha          Yo‘q
          [10, 12, 13]    [30, 32, 35]
```

Xatolik kamayishi **impurity reduction** deb ham qaraladi:

$$
\Delta SSE=SSE_{\text{parent}}-SSE_{\text{split}}
$$

Eng kichik $SSE_{\text{split}}$ eng katta xatolik kamayishiga teng.

---

## 10. Keyingi tugunlarni bo‘lish

Chap tugundagi qiymatlar:

$$
y=[10,12,13]
$$

Ikki nomzoddan $x\leq1.5$ uchun SSE `0.5`, $x\leq2.5$ uchun esa `2`
chiqadi. Shuning uchun chap tugunda $x\leq1.5$ tanlanadi.

O‘ng tugundagi qiymatlar:

$$
y=[30,32,35]
$$

$x\leq4.5$ uchun SSE `4.5`, $x\leq5.5$ uchun esa `2` chiqadi. Shuning
uchun o‘ng tugunda $x\leq5.5$ tanlanadi.

Maksimal chuqurlik `2` bo‘lsa, hosil bo‘lgan daraxt:

```text
                         x ≤ 3.5?
                       /          \
                     Ha            Yo‘q
                x ≤ 1.5?          x ≤ 5.5?
                /      \          /       \
              10       12.5      31        35
```

Qoidalar bo‘lakli funksiya ko‘rinishida yoziladi:

$$
\hat{y}=
\begin{cases}
10, & x\leq1.5,\\
12.5, & 1.5<x\leq3.5,\\
31, & 3.5<x\leq5.5,\\
35, & x>5.5.
\end{cases}
$$

Decision Tree Regression grafigi silliq chiziq emas, zinapoyasimon funksiya
hosil qiladi.

---

## 11. Bashorat qilish

Yangi obyekt ildizdan boshlab shartlar bo‘ylab barggacha yo‘naltiriladi.

| Yangi $x$ | Bosib o‘tiladigan yo‘l | Bashorat |
| --------: | ---------------------- | -------: |
|       2.7 | $x\leq3.5$, keyin $x>1.5$ | 12.5 |
|       4.2 | $x>3.5$, keyin $x\leq5.5$ | 31 |
|       6.5 | $x>3.5$, keyin $x>5.5$ | 35 |

Trening datasetidagi bashoratlar:

| $x$ | Haqiqiy $y$ | Bashorat $\hat{y}$ |
| --: | ----------: | ------------------: |
|   1 |          10 |                  10 |
|   2 |          12 |                12.5 |
|   3 |          13 |                12.5 |
|   4 |          30 |                  31 |
|   5 |          32 |                  31 |
|   6 |          35 |                  35 |

$$
SSE=2.5
$$

$$
MSE=\frac{2.5}{6}\approx0.417
$$

Bu natija faqat trening ma’lumotidagi moslikni ko‘rsatadi. Model sifati
alohida test ma’lumotida yoki cross-validation orqali baholanadi.

---

## 12. Nega bargda o‘rtacha qiymat olinadi?

Bitta bargga $y=[12,13]$ qiymatlari tushgan bo‘lsin. Kvadratik xatolik uchun
eng yaxshi doimiy bashorat o‘rtacha qiymatdir:

$$
\bar{y}=\frac{12+13}{2}=12.5
$$

$$
SSE(12.5)=(12-12.5)^2+(13-12.5)^2=0.5
$$

$12$ yoki $13$ bashorat qilinsa, SSE `1` ga teng bo‘ladi. Umuman olganda,
kvadratik xatolikni minimallashtiruvchi doimiy qiymat arifmetik o‘rtachadir:

$$
\boxed{\hat{y}_{\text{leaf}}
=\frac{1}{n_{\text{leaf}}}\sum_{i=1}^{n_{\text{leaf}}}y_i}
$$

---

## 13. Bir nechta alomat bilan ishlash

Bir nechta alomat bo‘lsa, daraxt har bir tugunda barcha alomatlardagi barcha
mumkin bo‘lgan chegaralarni tekshiradi.

Uy narxi misoli:

| Obyekt | Maydon $x_1$ | Yosh $x_2$ | Narx $y$ |
| -----: | ------------: | ----------: | --------: |
|      1 |            50 |          20 |       200 |
|      2 |            60 |           5 |       260 |
|      3 |           100 |          25 |       400 |
|      4 |           110 |           4 |       460 |

Daraxt bo‘linmasa, o‘rtacha narx va xatolik:

$$
\bar{y}=330,\qquad SSE_{\text{root}}=43600
$$

Maydon bo‘yicha nomzod chegaralar:

$$
55,\quad80,\quad105
$$

Yosh qiymatlari tegishli obyektlar bilan birga saralanganda nomzod chegaralar:

$$
4.5,\quad12.5,\quad22.5
$$

Barcha natijalar:

| Alomat | Bo‘linish | Umumiy SSE |
| ------ | --------- | ----------: |
| Maydon $x_1$ | $x_1\leq55$ | 21066.67 |
| Maydon $x_1$ | $x_1\leq80$ | **3600.00** |
| Maydon $x_1$ | $x_1\leq105$ | 21066.67 |
| Yosh $x_2$ | $x_2\leq4.5$ | 21066.67 |
| Yosh $x_2$ | $x_2\leq12.5$ | 40000.00 |
| Yosh $x_2$ | $x_2\leq22.5$ | 37066.67 |

Eng kichik xatolik maydonning `80` chegarasida hosil bo‘ladi:

$$
\boxed{x_1\leq80}
$$

```text
                     Maydon ≤ 80?
                    /            \
                  Ha              Yo‘q
            [200, 260]        [400, 460]
```

Yosh alomati ushbu tugunda tanlanmagan bo‘lsa ham, boshqa tugunda yoki boshqa
datasetda tanlanishi mumkin. Har bir tugun uchun tanlash jarayoni qaytadan
bajariladi.

---

## 14. Eng yaxshi alomat va chegaraning umumiy formulasi

Datasetda $m$ ta alomat mavjud bo‘lsin:

$$
X=(x_1,x_2,\ldots,x_m)
$$

Har bir $j$ alomat va $t$ chegara uchun:

$$
SSE(j,t)=
\sum_{i\in R_L(j,t)}(y_i-\bar{y}_L)^2
+\sum_{i\in R_R(j,t)}(y_i-\bar{y}_R)^2
$$

Algoritm quyidagi juftlikni tanlaydi:

$$
\boxed{(j^*,t^*)=\arg\min_{j,t}SSE(j,t)}
$$

Bu formula barcha alomat va chegaralar orasidan bo‘linish xatoligi eng kichik
bo‘lgan juftlik tanlanishini bildiradi.

Multiple Linear Regression alomatlarni bitta formulada birlashtiradi:

$$
\hat{y}=b_0+b_1x_1+b_2x_2+\cdots+b_mx_m
$$

Decision Tree Regression esa alomatlarni ketma-ket `if–else` shartlarida
ishlatadi. Bir yo‘ldagi ayrim alomatlar umuman ishlatilmasligi ham mumkin.

---

## 15. Daraxt qachon bo‘linishni to‘xtatadi?

Cheklovsiz daraxt har bir trening obyektini alohida bargga joylashtirib,
trening xatoligini nolga tushirishi mumkin. Bunday daraxt yangi ma’lumotda
yomon ishlashi ehtimoli yuqori.

Asosiy boshqaruv parametrlari:

| Parametr | Vazifasi |
| -------- | -------- |
| `max_depth` | Daraxtning maksimal chuqurligini cheklaydi |
| `min_samples_split` | Tugunni bo‘lish uchun zarur minimal obyektlar sonini belgilaydi |
| `min_samples_leaf` | Har bir bargda qolishi kerak bo‘lgan minimal obyektlar sonini belgilaydi |
| `max_leaf_nodes` | Barglar sonini cheklaydi |
| `ccp_alpha` | Cost-complexity pruning kuchini belgilaydi |

Juda sayoz daraxt muhim bog‘liqliklarni o‘rgana olmay, **underfitting** qiladi.
Juda chuqur daraxt esa trening ma’lumotidagi shovqinni yodlab,
**overfitting** qiladi.

Parametrlar train natijasiga qarab emas, validation yoki cross-validation
natijasiga qarab tanlanadi.

---

## 16. Ekstrapolyatsiya cheklovi

Decision Tree Regression trening ma’lumotidan tashqaridagi o‘sish yoki pasayish
tendensiyasini davom ettirmaydi. Yuqoridagi daraxtda:

$$
x>5.5\Rightarrow\hat{y}=35
$$

Shuning uchun $x=6.5$, $x=10$ va $x=100$ qiymatlari bir xil oxirgi bargga
tushsa, har uchalasi uchun ham `35` bashorat qilinadi.

Linear Regression chiziqni yangi oraliqqa davom ettira oladi, Decision Tree
esa mavjud barg qiymatlaridan tashqariga tabiiy ravishda chiqmaydi.

---

## 17. Python orqali model qurish

```python
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor, export_text

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
])

y = np.array([10, 12, 13, 30, 32, 35])

model = DecisionTreeRegressor(
    max_depth=2,
    random_state=42,
)

model.fit(X, y)

y_pred = model.predict(X)
print("Bashoratlar:", y_pred)
print("MSE:", mean_squared_error(y, y_pred))

X_new = np.array([[2.7], [4.2], [6.5]])
print("Yangi bashoratlar:", model.predict(X_new))

rules = export_text(model, feature_names=["oqish_soati"])
print(rules)
```

Natija:

```text
Bashoratlar: [10.  12.5 12.5 31.  31.  35. ]
MSE: 0.4166666666666667
Yangi bashoratlar: [12.5 31.  35. ]
```

Daraxt qoidalari:

```text
|--- oqish_soati <= 3.50
|   |--- oqish_soati <= 1.50
|   |   |--- value: [10.00]
|   |--- oqish_soati > 1.50
|   |   |--- value: [12.50]
|--- oqish_soati > 3.50
|   |--- oqish_soati <= 5.50
|   |   |--- value: [31.00]
|   |--- oqish_soati > 5.50
|   |   |--- value: [35.00]
```

Bir nechta alomatli datasetda `X` matritsasiga qo‘shimcha ustunlar kiritiladi.
Algoritm har bir tugunda barcha ustunlarni avtomatik tekshiradi.

---

## 18. Modelni baholash

Regression daraxti MAE, MSE, RMSE va $R^2$ kabi odatiy regression
metrikalari bilan baholanadi.

Trening xatoligining kichikligi yetarli emas. To‘g‘ri baholash tartibi:

1. Dataset train va test qismlariga ajratiladi.
2. Daraxt faqat train qismida o‘rgatiladi.
3. `max_depth`, `min_samples_leaf` kabi parametrlar cross-validation orqali
   tanlanadi.
4. Yakuniy sifat test qismida o‘lchanadi.

Test xatoligi trening xatoligidan ancha katta bo‘lsa, overfitting ehtimoli
yuqori bo‘ladi.

---

## 19. Linear va Decision Tree Regression farqi

| Xususiyat | Linear Regression | Decision Tree Regression |
| --------- | ----------------- | ------------------------ |
| Model ko‘rinishi | To‘g‘ri chiziq yoki tekislik | Qarorlar daraxti |
| Ifoda | Koeffitsiyentli formula | `if–else` qoidalar |
| Chiziqlilik talabi | Mavjud | Mavjud emas |
| Masshtablash | Ba’zan kerak | Odatda kerak emas |
| Bashorat grafigi | Silliq | Zinapoyasimon |
| Interactionlar | Alohida kiritilishi mumkin | Avtomatik o‘rganilishi mumkin |
| Overfitting xavfi | Nisbatan pastroq | Yuqoriroq |
| Ekstrapolyatsiya | Mumkin | Yaxshi ishlamaydi |

Decision Tree Classification va Decision Tree Regression ham bir xil daraxt
tuzilmasidan foydalanadi. Farqi barg natijasida:

- Classification bargida sinf yoki sinf ehtimoli saqlanadi;
- Regression bargida sonli bashorat, odatda o‘rtacha qiymat saqlanadi.

---

## 20. Afzalliklari va kamchiliklari

Afzalliklari:

- qoidalarni tushuntirish oson;
- chiziqli bo‘lmagan bog‘liqliklarni o‘rganadi;
- bir nechta alomat bilan ishlaydi;
- alomatlarni standartlashtirish odatda talab qilinmaydi;
- alomatlar orasidagi murakkab o‘zaro ta’sirlarni aniqlaydi;
- sonli va tartibli qaror chegaralarini tabiiy ifodalaydi.

Kamchiliklari:

- chuqur daraxt tez overfitting qiladi;
- ma’lumotdagi kichik o‘zgarish daraxt tuzilishini o‘zgartirishi mumkin;
- bashorat funksiyasi zinapoyasimon bo‘ladi;
- ekstrapolyatsiya qobiliyati past;
- bitta daraxt ko‘pincha Random Forest yoki Gradient Boostingdan beqarorroq.

---

## 21. Algoritmning ishlash tartibi

1. Barcha obyektlar ildiz tugunga joylashtiriladi.
2. Har bir alomatdagi nomzod chegaralar topiladi.
3. Har bir `alomat + chegara` juftligi uchun chap va o‘ng guruhlar tuziladi.
4. Guruhlarning o‘rtacha target qiymatlari hisoblanadi.
5. Chap va o‘ng guruhdagi SSE qiymatlari qo‘shiladi.
6. Eng kichik umumiy xatolik bergan juftlik tanlanadi.
7. Hosil bo‘lgan yangi tugunlarda jarayon takrorlanadi.
8. To‘xtash sharti bajarilganda tugun bargga aylanadi.
9. Bargdagi target qiymatlarining o‘rtachasi bashorat sifatida saqlanadi.

---

## 22. Muhim xulosa

Decision Tree Regression har bir tugunda quyidagi ko‘rinishdagi shartlarni
tekshiradi:

$$
x_j\leq t
$$

Har bir bo‘linish uchun:

$$
SSE_{\text{split}}=SSE_{\text{left}}+SSE_{\text{right}}
$$

hisoblanadi va eng kichik xatolik bergan alomat hamda chegara tanlanadi.
Yakuniy barg bashorati:

$$
\boxed{\hat{y}_{\text{leaf}}
=\frac{1}{n_{\text{leaf}}}\sum_{i=1}^{n_{\text{leaf}}}y_i}
$$

Asosiy maqsad — o‘xshash target qiymatlarini bir bargda to‘plash. Daraxt
chuqurligi va barg hajmi nazorat qilinmasa, trening ma’lumotiga ortiqcha
moslashish xavfi paydo bo‘ladi.
