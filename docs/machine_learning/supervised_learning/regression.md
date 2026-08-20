# Regression

Regression - bu Supervised Learning, ya'ni nazorat ostidagi o'rganishning
asosiy yo'nalishlaridan biri. Unda model kiruvchi ma'lumotlar asosida sonli
qiymat bashorat qiladi.

Masalan:

- uy narxini bashorat qilish;
- bemorning kasallik xavfi foizini baholash;
- ertangi haroratni taxmin qilish;
- avtomobil yoqilg'i sarfini oldindan aytish;
- kanal bo'yicha suv oqimi tezligi yoki sathini bashorat qilish;
- aksiyalar narxi yoki talab hajmini prognoz qilish.

Regressionda natija odatda uzluksiz son bo'ladi:

$$
y = f(x)
$$

Bu yerda:

- $x$ - kiruvchi belgilar, ya'ni features;
- $y$ - bashorat qilinadigan sonli qiymat;
- $f(x)$ - model o'rganadigan bog'lanish.

Masalan, uy narxini bashorat qilishda:

$$
\text{Narx} = f(\text{maydon}, \text{xonalar soni}, \text{joylashuv}, \text{qurilgan yili})
$$

**Regression nima uchun kerak?**

Regressionning asosiy vazifasi - kiruvchi belgilar va sonli natija orasidagi
bog'liqlikni o'rganish.

________________________________________

**Regression turlari:**

- Simple Linear Regression — oddiy chiziqli regressiya
- Multiple Linear Regression — ko‘p omilli chiziqli regressiya
- Polynomial Regression — polinomial regressiya
- Ridge Regression — L2 regularizatsiyali regressiya
- Lasso Regression — L1 regularizatsiyali regressiya
- Elastic Net Regression — Ridge + Lasso kombinatsiyasi
- Logistic Regression — logistik regressiya
- Poisson Regression — sanash/count ma’lumotlari uchun regressiya
- Quantile Regression — kvantil regressiya
- Robust Regression — outlierlarga chidamli regressiya
- Stepwise Regression — belgilarni tanlab regressiya qurish
- Bayesian Regression — Bayes regressiyasi
- Support Vector Regression, SVR — SVM asosidagi regressiya
- Decision Tree Regression — daraxt asosidagi regressiya
- Random Forest Regression — ansambl regressiya
- Gradient Boosting Regression — boosting asosidagi regressiya
- XGBoost / LightGBM / CatBoost Regression — kuchaytirilgan daraxt regressiyalari
- Neural Network Regression — neyron tarmoq asosidagi regressiya
- KNN Regression — k yaqin qo‘shni asosidagi regressiya
- Gaussian Process Regression — ehtimollik asosidagi regressiya

**Regression metrikalari(asosiylari):**

**MAE - Mean Absolute Error**

O‘rtacha absolyut xatoni ko‘rsatadi.

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}\left|y_i-\widehat{y_i}\right|
$$

**MSE - Mean Squared Error**

Katta xatolarni kuchliroq jazolaydi.

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}\left(y_i-\widehat{y_i}\right)^2
$$

**RMSE - Root Mean Squared Error**

Xatoni target bilan bir xil birlikda ko‘rsatadi.

$$
RMSE=\sqrt{MSE}
$$

**R² Score — Coefficient of Determination**

Model target o‘zgarishini qanchalik tushuntirishini ko‘rsatadi.

$$
R^2=1-\frac{SS_{res}}{SS_{tot}}
$$

**Adjusted R²**

Ko‘p featureli modelda R² ning yaxshilangan shakli.
Feature soni ko‘payganda modelni adolatliroq baholaydi.

**MAPE - Mean Absolute Percentage Error**

Xatoni foizlarda ko‘rsatadi.

$$
MAPE=\frac{100}{n}\sum_{i=1}^{n}\left|\frac{y_i-\widehat{y_i}}{y_i}\right|
$$

________________________________________

```{toctree}
:maxdepth: 1
:hidden:

regression/simple_linear_regression
regression/multiple_linear_regression
regression/polynomial_regression
regression/logistic_regression
regression/decision_tree_regression
regression/random_forest_regression
```
