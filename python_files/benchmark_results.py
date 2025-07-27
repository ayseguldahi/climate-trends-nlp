import time
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import scrapy
from scrapy.crawler import CrawlerProcess
import psutil
import pandas as pd

TEST_URL = "https://www.reddit.com/r/climatechange/"

# Function to measure execution time and memory usage
def measure_performance(func):
    process = psutil.Process()
    start_memory = process.memory_info().rss / (1024 * 1024)  
    start_time = time.time()
    func()  
    end_time = time.time()
    end_memory = process.memory_info().rss / (1024 * 1024)  
    return round(end_time - start_time, 2), round(abs(end_memory - start_memory), 2)

# Benchmark BeautifulSoup (static scraping)
def benchmark_bs4():
    response = requests.get(TEST_URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [tag.text for tag in soup.find_all("h3")]

# Benchmark Playwright (dynamic scraping)
def benchmark_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(TEST_URL, timeout=30000)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2) 
        titles = page.query_selector_all("h3")
        browser.close()

# Benchmark Scrapy (framework-based)
class ScrapySpider(scrapy.Spider):
    name = "scrapy_benchmark"
    start_urls = [TEST_URL]

    def parse(self, response):
        titles = response.css("h3::text").getall()

def benchmark_scrapy():
    process = CrawlerProcess(settings={"LOG_ENABLED": False})
    process.crawl(ScrapySpider)
    process.start()

bs4_time, bs4_memory = measure_performance(benchmark_bs4)
playwright_time, playwright_memory = measure_performance(benchmark_playwright)
scrapy_time, scrapy_memory = measure_performance(benchmark_scrapy)

# Create benchmark table
benchmark_results = pd.DataFrame({
    "Library": ["BeautifulSoup", "Playwright", "Scrapy"],
    "Execution Time (s)": [bs4_time, playwright_time, scrapy_time],
    "Memory Usage (MB)": [bs4_memory, playwright_memory, scrapy_memory],
    "Ease of Use (1-10)": [9, 6, 4]  
})

print("Web Scraping Libraries Benchmark Results:")
print(benchmark_results)
benchmark_results.to_csv("csv_files/web_scraping_benchmark.csv", index=False)
print("Benchmark results saved to 'web_scraping_benchmark.csv'.")

