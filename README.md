# Web-app-for-ML-project

## Обзор

Проект посвящен разработке локального веб-приложения для анализа данных и прогнозирования оттока клиентов. Данные взяты с соревнования на платформе Kaggle: https://www.kaggle.com/c/advanced-dls-spring-2021/

Приложение состоит из двух страниц. Главная страница содержит интерактивные графики с анализом исходных данных: пользователь может самостоятельно выбирать признаки, распределение которых он хочет изучить, диаграммы переключаются в зависимости от выбранных признаков.
![image](https://github.com/acumfly/Web-app-for-ML-project/assets/75485157/52e3b956-8235-48eb-b517-04b3d380ad02)
![image](https://github.com/acumfly/Web-app-for-ML-project/assets/75485157/342bdbd1-a24e-49e8-a3c3-fc021a6fee1c)


При нажатии на “Get prediction” пользователь переходит на вторую страницу, где он может ввести данные о своем клиенте и, нажав на кнопку “Вероятность ухода”, оценить вероятность того, что услугами перестанут пользоваться.
![image](https://github.com/acumfly/Web-app-for-ML-project/assets/75485157/f120764c-3dca-4032-aac4-0e3400bd697a)


## Составляющие приложения

* Исследовательская часть (папка analysis)
Анализ данных был проведен в отдельном jupyter-ноутбуке. После тестирования моделей для предсказания в качестве лучшей был выбран CatBoost Classifier.
* Обучение модели (папка catboost_training)
Обучение модели также было вынесено отдельно от веб-приложения.
* Веб-приложение (папка web_app)
Создано с помощью фреймворка Dash.

## Библиотеки
* Plotly
* Dash Bootstrap Components
* CatBoost
* Scikit-learn
* Pandas
* Numpy
* Joblib
