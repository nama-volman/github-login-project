from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_URL = "https://github.com/"
DETAILS = {
    "github_username" : os.getenv("TEST_USERNAME"),
    "github_password" : os.getenv("TEST_PASSWORD")
 }