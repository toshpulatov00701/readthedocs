# Baholash metrikalari

**Baholash metrikalari (*evaluation metrics*)** - bu mashinali o‘rganishda (ko‘pincha klassifikatsiyada) modelning ishlash sifatini o‘lchash uchun qo‘llanadigan ko‘rsatkichlardir.

Confusion Matrix (chalg‘ituvchi matritsa):

|                      | Haqiqatda ijobiy (Positive) | Haqiqatda salbiy (Negative) |
|----------------------|-----------------------------|-----------------------------|
| Model ijobiy dedi    | True Positive (TP)          | False Positive (FP)         |
| Model salbiy dedi    | False Negative (FN)         | True Negative (TN)          |

---

<h3>Accuracy (aniqlik darajasi)</h3>
To‘g‘ri klassifikatsiya qilingan obyektlar sonining jami obyektlar soniga nisbati.

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Model “kasal” deganlarning 87% haqiqatda kasal bo‘lgan.

---

<h3>Precision (aniqlik, ishonchlilik)</h3>
model musbat (masalan, anomal) deb aytganlarning nechta qismi aslida ham musbat?

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

Savolga javob beradi: “Model anomal dedi, haqiqatda ham anomal bo‘lish ehtimoli nechcha %?”

---

<h3>Recall (Qamrov)</h3>
Haqiqiy musbatlardan nechtasini model topa oldi?

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

Haqiqiy kasallarning 55% ini model topgan.

---

<h3>F1-score</h3>
Precision va Recall orasidagi balansni o‘lchaydi (ularning harmonik o‘rtachasi).

$$
\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

Nega alohida ko‘rsatkich yetarli emas?

- Agar faqat Accuracy yuqori bo‘lsa, recall past bo‘lishi mumkin (ko‘p haqiqiy pozitivlar o‘tkazib yuboriladi).
- Agar faqat recall yuqori bo‘lsa, precision past bo‘lishi mumkin (ko‘p noto‘g‘ri pozitivlar chiqadi).
- F1-score ikkalasini harmonik o‘rtacha qilib baholaydi, shuning uchun bir tomonga og‘ib ketishni oldini oladi.

---

<h3>Misol</h3>
Aytaylik, sizda 100 ta test namunasi bor:

- TP = 40  
- FP = 10  
- FN = 20  
- TN = 30  

Hisoblash:

- Accuracy = (40+30) / 100 = `0.70 (70%)`  
- Precision = 40 / (40+10) = `0.80 (80%)`  
- Recall = 40 / (40+20) = `0.67 (67%)`  
- F1-score ≈ `0.73 (73%)`
