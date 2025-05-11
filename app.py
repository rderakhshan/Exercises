import os
import sys
import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import chromadb.utils.embedding_functions as embedding_functions

# Loading enviromental variables
load_dotenv()

# Setting up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
# if openai_api_key is None:
#     print("Please set the OPENAI_API_KEY environment variable.")
#     sys.exit(1)
    

# Setting up OpenAI embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key = openai_api_key,
                model_name="text-embedding-3-small"
            )
