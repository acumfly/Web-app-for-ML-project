import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
import joblib


# data loading
df = pd.read_csv('./train_churn.csv')

# Числовые признаки
num_cols = [
    'ClientPeriod',
    'MonthlySpending',
    'TotalSpent'
]

# Категориальные признаки
cat_cols = [
    'Gender',
    'IsSeniorCitizen',
    'HasPartner',
    'HasChild',
    'HasPhoneService',
    'HasMultiplePhoneNumbers',
    'HasInternetService',
    'HasOnlineSecurityService',
    'HasOnlineBackup',
    'HasDeviceProtection',
    'HasTechSupportAccess',
    'HasOnlineTV',
    'HasMovieSubscription',
    'HasContractPhone',
    'IsBillingPaperless',
    'PaymentMethod'
]

feature_cols = num_cols + cat_cols
target_col = 'Churn'

# initializing train/test data
X, y = df.drop(columns=['Churn']), df.Churn
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

# training catboost
boosting_model = CatBoostClassifier(cat_features=cat_cols, iterations=50, learning_rate=0.1, random_seed=42)
boosting_model.fit(X_train, y_train, silent=True)

#saving the model
filename = 'CB_trained.sav'
joblib.dump(boosting_model, open(filename, 'wb'))




