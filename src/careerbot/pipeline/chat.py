from careerbot.components.scraper import Scraper
from careerbot.components.llm import LLM
from careerbot.config.configuration import ConfigurationManager
from logger import logger

from time import time 


class Chat:
    def __init__(self):
        '''
        creates an instance of the Chat Pipeline for Counselling
        '''
        self.config = ConfigurationManager()
        
    def initiate(self, scrape: bool = False):
        '''
        initiate the pipeline before starting the chatting
        
        ## Parameters:
        
        scrape: bool - True
            whether to scrape the articles or not
        '''
        if scrape:
            scraper_config = self.config.get_scraper_config()
            scraper = Scraper(scraper_config)
            
            logger.info("Scraping Started")
            career_records = scraper.scrape_careers()
            scraper.scrape_articles(career_records)
            logger.info("Scraping Finished!!!")
        else:
            logger.info("Skipping Scraping")
        
        llm_config = self.config.get_llm_config()
        self.llm = LLM(llm_config)
        self.llm.prepare_llm()
        logger.info("LLM successfully Loaded and Prepared!!!")

    def respond(self, query: str):
        start = time()
        response = self.llm.generate_response(query)
        end = time()
        
        logger.info("Respond took ", start-end, " time")
        
        return response 
                