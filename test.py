# Import necessary libraries
import openai
from paperqa import Docs, Settings
from dotenv import load_dotenv
import os

load_dotenv()
# Ensure you have set your OpenAI API key in the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Docs object for managing the documents
docs = Docs()

# Add your documents (pdf, txt, etc.)
# Replace 'my_paper.pdf' with your actual file path.
docs.add("my_papers/Skin_needling_as_a_treatment_for_acne_scarring_An_.pdf")

# Define the query you want to ask
query = "How many studies discussed the combination of skin needling with other treatment methods?"

# Configure settings for OpenAI, without using any other external APIs
settings = Settings()
settings.answer.answer_max_sources = 5  # Limit the number of sources in the answer
settings.verbosity = 3
# Query the documents with the specified settings
answer = docs.query(query, settings=settings)

# Output the formatted answer
print(answer.formatted_answer)
