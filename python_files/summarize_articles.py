import os
import openai
import time

openai.api_key = os.getenv("OPENAI_API_KEY")
import pandas as pd

file_path = "csv_files/reddit_climate_articles.csv" 
df = pd.read_csv(file_path)
print(df.head())

openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to summarize text using GPT with request throttling
def gpt_summarize(title):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Summarize the following title briefly."},
                      {"role": "user", "content": title}],
            temperature=0.7
        )
        time.sleep(20)  # Wait 20 seconds to stay within rate limit
        return response["choices"][0]["message"]["content"]

    except openai.error.RateLimitError:
        print("Rate limit reached. Waiting for 30 seconds before retrying...")
        time.sleep(30)  
        return gpt_summarize(title) 

# Apply GPT summarization with progress tracking
summaries = []
for i, title in enumerate(df["title"]):
    print(f"Processing article {i+1}/{len(df)}: {title[:50]}...") 
    summary = gpt_summarize(title)
    summaries.append(summary)

df["summary"] = summaries
print("Summarization Completed! Here are some results:")
print(df[["title", "summary"]].head())
df.to_csv("csv_files/reddit_climate_articles_gpt.csv", index=False)




