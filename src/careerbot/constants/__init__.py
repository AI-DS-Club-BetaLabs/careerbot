from pathlib import Path 

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("config/params.yaml")

SYSTEM_PROMPT = """
You are a Q&A assistant. Your goal is to answer questions as
accurately as possible based on the instructions and context provided.
"""

QUERY_PROMPT = "<|USER|>{query_str}<|ASSISTANT|>"