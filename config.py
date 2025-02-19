from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

LANG_BACKEND = os.getenv("LANG_BACKEND")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")