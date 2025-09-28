import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/chatbot')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'chatbot')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'qa_pairs')
