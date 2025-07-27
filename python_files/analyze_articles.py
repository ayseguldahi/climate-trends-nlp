import pandas as pd
from textblob import TextBlob
import random
file_path = "csv_files/reddit_climate_articles_gpt.csv"
df = pd.read_csv(file_path)

# Function to assign an improved importance score
def assign_importance(title):
    keyword_weights = {
        "climate crisis": 5, "kill":5, "death":5, "canada":5, "global warming": 5, "climate": 4, "carbon emissions": 4,
        "environment": 3, "renewable energy": 4, "fossil fuels": 3, "solar": 3, "wind": 3,
        "policy": 4, "green": 2, "emissions": 3
    }

    # Calculate score based on keyword presence
    score = sum(title.lower().count(word) * weight for word, weight in keyword_weights.items())

    # Normalize the score to fit between 1-10
    score = min(score + random.randint(1, 3), 10)
    
    return score

# Function to analyze sentiment 
def analyze_sentiment(title):
    sentiment = TextBlob(title).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative"

# Apply Importance Scoring & Sentiment Analysis
df["importance_score"] = df["title"].apply(assign_importance)
df["sentiment"] = df["title"].apply(analyze_sentiment)
df.to_csv("csv_files/reddit_climate_articles_analyzed.csv", index=False)

print("Analysis Completed!")

