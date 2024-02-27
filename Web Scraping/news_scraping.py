from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import pandas as pd

def initialize_driver():
    options = Options()
    options.headless = True
    return webdriver.Chrome(options=options)

def scrape_hurriyet_economy_news(start_page, end_page):
    driver = initialize_driver()
    content = []
    header = []
    date = []

    for j in tqdm(range(start_page, end_page + 1)):
        url = f'https://www.hurriyet.com.tr/arama/#/?page={j}&where=hurriyet&how=Article&startDate=01/01/2018&finishDate=16/11/2022&year=2022&yearInterval=1&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true%22'
        driver.get(url)

        for link in driver.find_elements(By.XPATH, '//div[@id="pageArticles"]//a[not(@class="muted video")]'):
            href = link.get_attribute('href')
            if href:
                driver.get(href)
                content.append(driver.find_element(By.CSS_SELECTOR, 'div.article-content').text)
                header.append(driver.find_element(By.TAG_NAME, 'h1').text)
                date.append(driver.find_element(By.XPATH, '//span[contains(text(), "Oluşturulma Tarihi:")]').text.replace("Oluşturulma Tarihi: ", ""))

    driver.quit()
    return pd.DataFrame({'News Date': date, 'Header': header, 'Content': content})

# Kullanım örneği
all_data = scrape_hurriyet_economy_news(1, 2)