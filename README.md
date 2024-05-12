# Summary

reviews_app.py is a script that, when run with a Replicate API Token, will take summarize the 1, 2, 3, 4, or 5 star reviews of an Amazon product. When reviews_app.py is run, it asks for the user to input the URL of an Amazon product's reviews. It then scrapes the review information using Selenium and BeautifulSoup. These are then passed to Meta's Llama 3 70B Instruct LLM via Replicate's API. The summarization is done by first distilling each review to a single core complaint or praise and then summarizes these distilled versions, grouping similar reviews together.
