import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
    TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
    MONGODB_URI = os.getenv('MONGODB_URI')
    
    @staticmethod
    def validate_config():
        required_vars = ['TWITTER_USERNAME', 'TWITTER_PASSWORD', 'MONGODB_URI']
        missing_vars = [var for var in required_vars if not getattr(Config, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
