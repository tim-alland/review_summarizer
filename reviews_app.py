import scraper
import summaryllm
import os


print("Enter an Amazon URL you want a reviews summary from")

url = input()
key = os.environ["REPLICATE_API_TOKEN"]
model = "meta/meta-llama-3-70b-instruct"

reviews = scraper.scrape(url)
summary = summaryllm.get_summary(reviews, model, key)

print(summary)