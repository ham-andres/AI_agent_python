import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types




def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description = "Your personal AI")
    parser.add_argument("user_prompt",type = str, help = "Enter your prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages,
    )
    
    if response.usage_metadata is None:
        raise RuntimeError("No token usage info")
    
    if args.verbose:
        print("User prompt:", args.user_prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response:")
        print(response.text)
    else:
        print("Response:")
        print(response.text)



if __name__ == "__main__":
    main()
