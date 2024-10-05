# Import necessary libraries
import openai
from paperqa import Docs, Settings
from dotenv import load_dotenv
import os
import glob
from langsmith import traceable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@traceable(name="Process data batch")
def process_data_batch(path):
    docs = Docs()
    for file_path in glob.glob(f"{path}/*.*"):
        docs.add(file_path)
    return docs
docs = process_data_batch("my_papers")


query = "How many studies discussed the combination of skin needling with other treatment methods?"

# Configure settings for OpenAI, without using any other external APIs
settings = Settings()
settings.answer.answer_max_sources = 5  # Limit the number of sources in the answer
settings.verbosity = 3
# Query the documents with the specified settings
answer = docs.query(query, settings=settings)

# Output the formatted answer
print(answer.formatted_answer)
