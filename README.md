# 🌍 climate-trends-nlp

**climate-trends-nlp** is a Python-based project that scrapes, summarizes, and analyzes Reddit posts related to climate change using NLP techniques. The pipeline integrates web scraping with Playwright, GPT-powered summarization and sentiment analysis, and outputs datasets and insights useful for climate communication research.

---

## 🧠 Project Goals

- Understand how climate change is discussed on social media.
- Summarize long Reddit posts into digestible insights using GPT models.
- Analyze the sentiment and engagement metrics of climate discourse.
- Benchmark different scraping approaches for speed and reliability.
- Provide researchers, journalists, and educators with a foundation for analyzing public climate narratives.

---

## 📁 Project Structure

```
📁 csv_files/
│   ├─ reddit_climate_articles.csv              # Raw scraped Reddit posts
│   ├─ reddit_climate_articles_analyzed.csv     # Sentiment & keyword analysis
│   ├─ reddit_climate_articles_gpt.csv          # GPT-based summaries
│   └─ web_scraping_benchmark.csv               # Scraper performance metrics

📁 python_files/
│   ├─ analyze_articles.py            # NLP logic: keyword extraction, sentiment
│   ├─ benchmark_results.py           # Script for scraping benchmark results
│   ├─ scrape_reddit_playwright.py    # Scrapes Reddit posts with Playwright
│   └─ summarize_articles.py          # GPT summarization for Reddit posts

📄 requirements.txt                   # Python dependencies
📄 README.md                          # Project documentation
```

---

## 🛠️ Setup Instructions

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Get an OpenAI API key**

   - Visit [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
   - Log in and create a new API key.
   - Copy the key securely.

3. **Set your API key**

   You can either:

   - Set it as an environment variable:

     **Windows (CMD):**
     ```cmd
     set OPENAI_API_KEY=your_api_key_here
     ```

     **macOS/Linux (Bash):**
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```

   - Or store it in a `.env` file and load it with `dotenv`:

     ```bash
     echo "OPENAI_API_KEY=your_api_key_here" > .env
     ```

     And in Python:

     ```python
     from dotenv import load_dotenv
     import os

     load_dotenv()
     api_key = os.getenv("OPENAI_API_KEY")
     ```

---

## 📊 Output

- Structured CSVs containing original posts, summaries, and sentiment.
- Benchmark logs comparing scraping runtimes.
- Optional visualizations for topic trends and sentiment distribution (not included in this repo).

---

## 📌 Use Cases

- Academic research in environmental communication
- Journalistic coverage of climate discourse
- Educational tools for analyzing online narratives
- Social media trend tracking for climate NGOs

---

## 📬 License & Contributions

This project is open-source. Contributions, improvements, and issue reporting are all welcome!
