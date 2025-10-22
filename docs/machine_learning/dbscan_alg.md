# DBSCAN

<img src="../_static/dbscan.gif" alt="Rasm tavsifi" width="50%"/>

**DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*)** — bu **zichlikka asoslangan klasterlash algoritmi**. U 1996-yilda Ester va hamkorlari tomonidan taklif qilingan va ayniqsa **shakli murakkab bo‘lgan klasterlarni aniqlashda** hamda **shovqin (noise) nuqtalarni ajratishda** samarali hisoblanadi.  

## Parametrlari

1. **ε (eps)** – radius. Bir nuqtaning atrofidagi hududni belgilaydi.  
2. **minPts** – minimal qo‘shnilar soni. Klaster hosil qilish uchun kerakli nuqtalar soni.

*! Agar biron obyekt berilgan ridiusga teng masofada bo'lsa, shu obyekt minPtsga qo'shiladi.*

## Obyektlar turlari

- **Yadroviy (Core point)** – agar ε-radius ichida kamida `minPts` (shu obyektning o‘zini ham qo‘shib hisoblaganda) qo‘shnisi bo‘lsa.  
- **Chegaraviy (Border point)** – ε ichida yadro obyektga bog‘langan, lekin qo‘shnilari yetarli bo‘lmagan.
- **Anomal/Shovqin (Noise/Outlier)** – hech qaysi klasterga kirmagan nuqta.

*! 2 ta klaster va ular o'rtasida bitta obyekt bor. O'rtaga turgan obyekt ikki klaster uchun ham chegaraviy. Oxirida o'rtada turgan obyekt qaysi klasterga tegishli bo'ladi? - DBSCAN algoritmi bunday holatlarni hal qilishda deterministik emas (noaniq) hisoblanadi, chunki bu amalga oshirishga bog'liq. Agar obyekt ikkala klasterning yadro nuqtasining radiusida bo'lsa, u qaysi klaster birinchi bo'lib tekshirilishiga/kengaytirilishiga bog'liq holda klasterga biriktiriladi. scikit-learn ning implementatsiyasida, birinchi bo'lib uni o'z ichiga olgan klasterga biriktirilib, boshqa klasterga qarash to'xtatiladi.*

*! Agar eps radius ichida minPts dan kam obyekt bo'lsa, bu obyekt anomal yoki chegaraviyga nomzod hisoblanadi. Chunki uni oldindan anomal yoki chegaraviy deb aytib bo'lmaydi.*

*!!! Klasterlar o'rtasida ham, klaster va chegaraviy obyekt o'rtasida ham bo'g'lovchi sifatida chegaraviy obyekt bo'lishi kerak emas. Klaster kengayishi faqat yadroviy bo'yicha bo'lishi shart.*

## Ishlash jarayoni

1. Bitta tasodifiy nuqta tanlanadi.  
2. Uning ε-radiusidagi qo‘shnilari hisoblanadi.  
3. Agar qo‘shnilar soni ≥ minPts → yangi klaster boshlanadi.  
4. Yadro nuqta orqali klaster qo‘shnilarga kengaytiriladi.  
5. Shunday qilib barcha nuqtalar ko‘rib chiqiladi.  

## Afzalliklari

- Oldindan klaster sonini (K) belgilash shart emas.  
- Murakkab shaklli klasterlarni topa oladi (masalan, egri yoki yoy shaklidagi).  
- Shovqinlarni alohida ajratib beradi.  

## Kamchiliklari

- ε va minPts tanlash qiyin.  
- Zichlik juda o‘zgaruvchan datasetlarda yaxshi ishlamasligi mumkin.  
- Juda katta datasetlarda hisoblash og‘ir.  

Python kod: [github.com](https://github.com/toshpulatov00701/ai_tasks/blob/main/DBSCAN/myDBSCAN.py)
