from dataclasses import dataclass
from pathlib import Path 


# TODO: Convert dataclass into pydantic
@dataclass(frozen=True)
class ScraperConfig:
    xpath: str 
    career_url: str 
    base_url: str 
    data_path: Path 

@dataclass(frozen=True)
class LLMConfig:
    data_path: Path 
    hf_token: str 
    llm: str 
    bit_4: bool 
    temperature: float 
    context_window: int
    max_new_tokens: int
    device: str 
    embedding: str 
    chunk_size: int 