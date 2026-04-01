import pandas as pd
import pickle
from preprocess import clean_text

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Create model folder if not exists
os.makedirs("../model", exist_ok=True)

df = pd.read_csv("../data/train.csv")

if 'text' not in df.columns:
    df.columns = ['text', 'emotion']

df = df.dropna()
df['text'] = df['text'].apply(clean_text)

vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
X = vectorizer.fit_transform(df['text'])
y = df['emotion']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

model = LogisticRegression(max_iter=300, class_weight='balanced')
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

pickle.dump(model, open("../model/model.pkl", "wb"))
pickle.dump(vectorizer, open("../model/vectorizer.pkl", "wb"))

print("Model saved!")
