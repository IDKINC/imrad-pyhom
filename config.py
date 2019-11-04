from congress import Congress
from dotenv import load_dotenv
import os

load_dotenv()
congress = Congress(os.getenv("PROPUBLICA"))
