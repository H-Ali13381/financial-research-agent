from langchain_community.utilities import SearxSearchWrapper
import os
from dotenv import load_dotenv

load_dotenv()

def web_search(search_input: str) -> str:
    """
    Search the internet for information with the search_input
    
    :param search_input: Input for the search
    """
    s = SearxSearchWrapper(
        # SearCNG URL
        searx_host="http://localhost:8888",
        # Default params
        params={
            "language":"en",
            "format":"json",
            "categories": "general",
        },
        # Secret key
        headers={"Authorization": f"Bearer {os.getenv("SEARX_SECRET_KEY")}"}  # If using auth
    )
    return s.run(search_input)