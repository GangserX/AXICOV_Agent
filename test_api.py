import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API key
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key (first 10 chars): {api_key[:10]}...")

genai.configure(api_key=api_key)

# List available models
print("\n🔍 Available Gemini Models:")
print("="*60)
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name}")
print("="*60)

# Test with a simple prompt
print("\n🧪 Testing model with simple prompt...")
try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello in JSON format with a 'message' field")
    print(f"\n✅ Success! Response: {response.text}")
except Exception as e:
    print(f"\n❌ Error: {e}")
    # Try with different model
    try:
        print("\nTrying gemini-1.5-flash-latest...")
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content("Say hello in JSON format with a 'message' field")
        print(f"✅ Success! Response: {response.text}")
    except Exception as e2:
        print(f"❌ Error: {e2}")
