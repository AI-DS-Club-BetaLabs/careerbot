from bs4 import BeautifulSoup
from requests.exceptions import SSLError
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm 
import requests

from logger import logger
from utils.common import create_directories
from careerbot.entity import ScraperConfig


class Scraper:
    def __init__(self, config: ScraperConfig):
        '''
        creates an instance of data Scraper class for scraping configured source
        
        ## Parameters:
        
        config: ScraperConfig 
            configuration for scraper
        '''
        self.config = config 
        create_directories([self.config.data_path])
        
    # TODO: Configure the scrape_careers using the selenium 
    def scrape_careers(self) -> dict :
        '''
        scrapes the career list from the browse page of the MyPlan website
        
        ## Returns:
        
        records: dict 
            dict containing all the records with title as key and hyperlink as value
        '''
        try:
            scraped = False 
            while not scraped:
                try:
                    response = requests.get(self.config.career_url)
                    scraped = True 
                except SSLError as e:
                    continue 
            
            soup = BeautifulSoup(response.content, "html5lib")
            careers = (soup
                       .find("td", attrs={"class": "box_table"})
                       .findAll('a', attrs={"class": "list-link"}))
            
            records = {
                career.text: self.config.base_url+career['href'].split("?")[0] for career in careers
            }
            
            return records 
        except Exception as e:
            logger.exception(e)
    
    def scrape_articles(self, records: dict):
        '''
        scrapes articles from the scraped records and saves the records in txt files at defined path
        
        ## Parameters:
        
        records: dict 
            includes all the records to be scraped with key as title and value as hyperlink
        '''
        scraped_data = {}
        
        driver = self.__initiate_chrome_driver()
        for entry, hyperlink in tqdm(records.items(), total=len(records)):
            entry = entry.replace("/", " or ")
            result = ""
            
            # Scrapes description page 
            driver.get(hyperlink.replace("summary", "description"))
            element = driver.find_element(By.XPATH, self.config.xpath)
            result += element.text + "\n\n"
            
            # Scrapes requirements page
            driver.get(hyperlink.replace("summary", "requirements"))
            element = driver.find_element(By.XPATH, self.config.xpath)
            result += element.text 
            
            scraped_data[entry] = result 
        
        self.__save_articles(scraped_data)
        
    def __save_articles(self, data: dict):
        for title, content in data.items():
            with open(self.config.data_path+f"{title}.txt", "w") as file:
                file.write(content)
        
    def __initiate_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=options)
        
        return driver
    