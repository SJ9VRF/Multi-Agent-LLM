# Miscellaneous utility functions.
import os

def setup_environment():
    os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY

def log_to_console(message):
    print(message)
