from careerbot.constants import *
from utils.common import read_yaml, create_directories
from careerbot.entity import (
    ScraperConfig, 
    LLMConfig
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

    def get_llm_config(self) -> LLMConfig:
        '''
        returns llm configuration 
        
        ## Returns: 
        
        llm_config: LLMConfig
            the configuration class for LLM
        '''
        config = self.config
        params = self.params
        llm_config = LLMConfig(
            data_path=config.data,
            hf_token=config.HF_TOKEN, 
            llm=params.llm.huggingface,
            bit_4=params.llm.bit_4,
            context_window=params.llm.context_window,
            max_new_tokens=params.llm.max_new_tokens,
            device=params.llm.device,
            embedding=params.embedding.huggingface,
            chunk_size=params.chunk_size
        )
        
        return llm_config
