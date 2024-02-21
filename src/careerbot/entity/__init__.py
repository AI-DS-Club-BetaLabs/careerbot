from dataclasses import dataclass
from pathlib import Path 


@dataclass(frozen=True)
class ScraperConfig:
    xpath: str 
    career_url: str 
    base_url: str 
    data_path: Path 
