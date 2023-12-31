# -*- coding: utf-8 -*-
"""taskRecommender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jc2ZCiPZXGjzOnpKC2gOW2yMfPA94-0r
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Data
dataset = pd.DataFrame({'activity': ['go for a walk', 'watch a movie', 'read a book', 'cook a meal', 'listen to music',
                                     'go for a hike', 'paint a picture', 'play a sport', 'visit a museum', 'have a picnic',
                                     'go shopping', 'visit a friend', 'do yoga', 'try a new recipe', 'attend a concert'],
                        'mood': ['relaxed', 'happy', 'relaxed', 'energetic', 'sad',
                                 'energetic', 'creative', 'energetic', 'curious', 'relaxed',
                                 'excited', 'social', 'relaxed', 'creative', 'excited']})


# Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset['activity'])
y = dataset['mood']

# Training the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

def recommend_activity(mood):
    # Preprocessing user input
    X_user = vectorizer.transform([mood])
    # Predicting mood based on user input
    predicted_mood = model.predict(X_user)[0]
    # Filtering activities based on predicted mood
    recommended_activities = dataset[dataset['mood'] == predicted_mood]['activity']

    return recommended_activities

user_mood = input("Enter your current mood: ")
recommended_activities = recommend_activity(user_mood)

if recommended_activities.empty:
    print("Sorry, no activities found for your current mood.")
else:
    print("Recommended activities:")
    for activity in recommended_activities:
        print("- " + activity)