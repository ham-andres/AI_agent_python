import os
from dotenv import load_dotenv
from google import genai
import argparse




def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description = "Your personal AI")
    parser.add_argument("user_prompt",type = str, help = "Enter your prompt")
    args = parser.parse_args()

    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=args.user_prompt,
    )
    
    if response.usage_metadata == None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    else:
        print("User prompt:", args.user_prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response:")
        print(response.text)



if __name__ == "__main__":
    main()
