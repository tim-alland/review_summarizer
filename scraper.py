from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# Example:
# scrape("https://www.amazon.com/product-reviews/B0C2YYBLC1/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar")
def scrape (url):
    '''Scrape the review texts from the URL, which is expected to be a link to an amazon 1/5 start review page.'''
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    reviews = soup.find_all('span', class_='a-size-base review-text review-text-content')
    return [review.get_text() for review in reviews]
