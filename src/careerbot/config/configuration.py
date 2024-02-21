from careerbot.constants import *
from utils.common import read_yaml, create_directories
from careerbot.entity import (
    ScraperConfig
)
from pathlib import Path 


class ConfigurationManager:
    def __init__(self, 
                 config_filepath: Path = CONFIG_FILE_PATH, 
                 params_filepath: Path = PARAMS_FILE_PATH) -> None:
        '''
        creates a configuration manager class which manages configuration for various stages 
        of development 
        
        ## Parameters:
        
        config_filepath: Path - CONFIG_FILE_PATH
            configuration yaml file path
            
        params_filepath: Path - PARAMS_FILE PATH
            parameters yaml file path
        '''
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts])
    
    def get_scraper_config(self) -> ScraperConfig:
        '''
        returns data scraper configuration 
        
        ## Returns:
        
        data_scraper_config: ScraperConfig
            the configuration class for Scraper
        '''
        config = self.config.scraper
        data_scraper_config = ScraperConfig(
            xpath=config.xpath,
            career_url=config.career_url, 
            base_url=config.base_url,
            data_path=config.data 
        )
        
        return data_scraper_config
