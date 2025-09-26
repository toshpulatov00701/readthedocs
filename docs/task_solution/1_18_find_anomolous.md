# 1.18. LOF (Local Outlier Factor)

## LOF (Local Outlier Factor) asosida anomal ob’ektlarni aniqlash

Berilgan $A=\{a_{ij}\}_{mn}$ jadvalda $E_{0} = (S_{1}, \ldots, S_{m})$ ob’ektlarning $n$ miqdoriy alomatlar bo‘yicha tavsifi keltirilgan. Ikkita $S_{u}, S_{v} \in E_{0}$ ob’ektlar o‘rtasidagi masofa $\rho(x,y)$ e’vklid metrikasi bilan hisoblanadi. Tanlanmaning $S$ ob’ektining $k$ ta eng yaqin qo‘shnilarini $N_{k}(S)$ bilan, $k\text{–}dis(S)$ orqali $S$ ob’ektidan $k$–yaqin qo‘shnigacha bo‘lgan masofani belgilaylik.
$S_{v}$ ob’ektidan $S_{u}$ ob’ektgacha erishiluvchi masofa quyidagicha aniqlanadi:  

$$
RD_{k}(S_{u}, S_{v}) = \max\{\,k\text{–}dis(S_{v}), \; \rho(S_{u}, S_{v})\}
$$

(1.a-rasmga qarang).

$S_{u}$ ob’ektga erishuvchanlikning lokal zichligi formula bilan aniqlanadi va $S_{u}$ ob’ektga uning qo‘shnilaridan erishish masofalarining o‘rta arifmetikiga nisbatan teskari hisoblanadi.  

Erishishning lokal zichligi qo‘shnilarning erishish lokal zichligi bilan quyidagicha taqqoslanadi:  

$$
LOF_{k}(S_{u}) = \frac{\sum_{S_{v} \in N_{k}(S_{u})} \dfrac{lrd_{k}(S_{v})}{lrd_{k}(S_{u})}}{|N_{k}(S_{u})|}
$$

ya’ni qo‘shnilarga erishishning o‘rtacha lokal zichligini ob’ektning o‘zining erishish lokal zichligiga bo‘lish orqali.  

Agar $LOF_{k}(S_{u}) \approx 1$ yaqin qiymat teng bo‘lsa, $S_{u}$ ob’ektni qo‘shnilar bilan qiyoslash mumkin bo‘ladi  
(u holda bu ob’ekt **anomal emas (sachratqi)**).  

- **$< 1$** qiymatlar zich sohani anglatadi (u ichki soha bo‘lishi mumkin).  
- **$> 1$** va yetarlicha katta qiymatlar ob’ektning anomalligidan guvoh beradi.  

---

Berilgan $E_{0}$ tanlanmaning $k = 3, 5, 7$ holatlar uchun barcha anomal ob’ektlari aniqlansin.  

---

### 1-rasm. Anomal ob’ektlarni aniqlash  
*(1-рис. Обнаружение аномальных объектов)*  

- 1.a–rasmda **V** va **S** ob’ektlari bir xil erishish masofasiga ega
