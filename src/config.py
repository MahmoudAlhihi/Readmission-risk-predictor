import os 
from dotenv import load_dotenv
from pathlib import Path

#Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Project settings
PROJECT_NAME = os.getenv("PROJECT_NAME", "readmission-risk")

# Paths
DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
RAW_DATA_DIR = BASE_DIR / os.getenv("RAW_DATA_DIR", "data/raw")
PROCESSED_DATA_DIR = BASE_DIR / os.getenv("PROCESSED_DATA_DIR", "data/processed")
MODEL_DIR = BASE_DIR / os.getenv("MODEL_DIR", "models")

#Modeling parameters
RANDOM_SEED = int(os.getenv("RANDOM_SEED", 42))
TEST_SIZE = float(os.getenv("TEST_SIZE", 0.2))
