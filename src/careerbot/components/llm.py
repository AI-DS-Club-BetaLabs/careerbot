from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext
)
import torch
import os 

from careerbot.constants import SYSTEM_PROMPT, QUERY_PROMPT
from utils.common import load_key
from careerbot.entity import LLMConfig
from logger import logger


class LLM:
    def __init__(self, config: LLMConfig):
        '''
        creates an instance of LLM class for creating an LLM pipeline
        
        ## Parameters:
        
        config: LLMConfig 
            configuration for llm
        '''
        self.config = config 
        if not self.config.hf_token:
            self.config.hf_token = load_key("HF_TOKEN")
        self.query_engine = None 
        
    def prepare_llm(self):
        '''
        configures and loads the LLM with rag integration 
        '''
        documents = SimpleDirectoryReader(
                os.path.join(self.config.data_path, "scraped")
            ).load_data()

        query_wrapper_prompt = SimpleInputPrompt(QUERY_PROMPT)
        service_context = self.__load_service_context(query_wrapper_prompt)
        
        index = VectorStoreIndex.from_documents(documents, 
                                                service_context=service_context)
        query_engine = index.as_query_engine()
        
        if self.query_engine:
            logger.info("Reloading Query Engine!!!")
        self.query_engine = query_engine
        
    def generate_response(self, query: str) -> str:
        '''
        generates response from a query provide. If query engine not initiate, 
        will start the initiation process.
        
        ## Parameters:
        
        query: str 
            the user query for the llm 
        
        ## Returns:
        
        response: str 
            the response generated by the llm model
        '''
        if not self.query_engine:
            logger.info("Query Engine not found, initiating Query Engine!!!")
            self.prepare_llm()
        
        response = self.query_engine.query(query)
        return response 
        
        
    def __load_service_context(self, query_wrapper_prompt):
        llm = HuggingFaceLLM(
            context_window=self.config.context_window, 
            max_new_tokens=self.config.max_new_tokens, 
            generate_kwargs={"temperature": self.config.temperature,
                             "do_sample": False}, 
            system_prompt=SYSTEM_PROMPT, 
            query_wrapper_prompt=query_wrapper_prompt, 
            tokenizer_name=self.config.llm, 
            model_name=self.config.llm, 
            device_map=self.config.device, 
            model_kwargs={"torch_dtype": torch.float16, 
                          "load_in_4bit": self.config.bit_4, 
                          "token": self.config.hf_token}
        )
        
        embed_model = LangchainEmbedding(
            HuggingFaceEmbeddings(model_name=self.config.embedding)
        )
        
        service_context = ServiceContext.from_defaults(
            chunk_size=self.config.chunk_size, 
            llm=llm, 
            embed_model=embed_model
        )
        
        return service_context
        