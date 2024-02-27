from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import pandas as pd

# Sabitler
COMPANY_LIST = ['turkcell', 'vodafone', 'turktelekom', 'gtechtr', 'akbank', 'netastr', 'teknosa', 'havelsan', 'bilkom', 'pentateknoloji', 'ziraatbankasi', 'garanti-bbva', 'isbankasi', 'papara', 'turksat', 'kocsistem', 'innova', 'logo-yazilim', 'mobiltel', 'turktelekom']
LINKEDIN_URL = "https://www.linkedin.com/company/{}/"
WEBDRIVER_PATH = r'C:\Program Files\geckodriver'
FIREFOX_PATH = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Fonksiyonlar
def get_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.binary_location = FIREFOX_PATH
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    browser = webdriver.Firefox(executable_path=WEBDRIVER_PATH, options=options)
    return browser

def get_company_info(browser, company):
    browser.get(LINKEDIN_URL.format(company))
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    info = soup.find('div', {'class': 'org-top-card-summary-info-list t-14 t-black--light'})
    content = info.find_all('div', {'class': 'org-top-card-summary-info-list__info-item'})
    company_data = {}
    for i, item in enumerate(content):
        company_data[i] = item.text.strip()
    return company_data

# Ana iş mantığı
def main():
    browser = get_browser()
    companies_data = []
    for company in tqdm(COMPANY_LIST, desc="Scraping Companies"):
        company_data = get_company_info(browser, company)
        company_data['Company'] = company
        companies_data.append(company_data)
    browser.quit()

    # Veriyi DataFrame'e dönüştürme
    df = pd.DataFrame(companies_data).rename(columns={0: 'Working Area', 1: 'Location', 2: 'Followers'})
    df.to_csv('linkedin_companies.csv', index=False)

if __name__ == "__main__":
    main()