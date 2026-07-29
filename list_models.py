"""
list_models.py

Run this once to see exactly which model names your API key supports.
Usage: python list_models.py
"""

from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

for m in genai.list_models():
    if "embedContent" in m.supported_generation_methods:
        print("EMBEDDING MODEL:", m.name)
    if "generateContent" in m.supported_generation_methods:
        print("CHAT MODEL:", m.name)