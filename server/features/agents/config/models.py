from pydantic_ai.models.google import GoogleModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

google_model = GoogleModel("gemini-2.5-flash-lite")