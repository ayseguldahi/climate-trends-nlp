import asyncio
from playwright.async_api import async_playwright
import pandas as pd
URL = "https://www.reddit.com/r/climatechange/"

async def scrape_reddit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context()
        page = await context.new_page()

        article_list = []

        try:
            await page.goto(URL, timeout=30000, wait_until="domcontentloaded")

            # Scroll down multiple times to load more posts
            for _ in range(10):  
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(3)  
                posts = await page.query_selector_all('a[slot="full-post-link"]')

                for post in posts:
                    title_element = await post.query_selector("faceplate-screen-reader-content")
                    title = await title_element.inner_text() if title_element else "No Title"
                    link = await post.get_attribute("href")
                    if link and not link.startswith("http"):
                        link = "https://www.reddit.com" + link

                    if title and link:
                        article_list.append({"title": title.strip(), "url": link})
                    if len(article_list) >= 100:
                        break
                if len(article_list) >= 120:
                    break

        except Exception as e:
            print(f"⚠️ Error occurred: {e}")

        finally:
            await browser.close()

        return article_list

# Run the scraper
async def main():
    articles_data = await scrape_reddit()

    if articles_data:
        print("Scraped Data:")
        for article in articles_data[:5]: 
            print(article)

        df = pd.DataFrame(articles_data)
        df.to_csv("csv_files/reddit_climate_articles.csv", index=False, encoding="utf-8")
        print("Data saved to 'reddit_climate_articles.csv'")
    else:
        print("No posts found!")

asyncio.run(main())

