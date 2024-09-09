from dotenv import load_dotenv
import requests
from typing import Iterable
import time
from requests.exceptions import ChunkedEncodingError, RequestException

def read_recipes():
    encodings = ['utf-8', 'latin-1', 'ascii', 'utf-16']
    for encoding in encodings:
        try:
            with open('recipes.txt', 'r', encoding=encoding) as recipes_file:
                return recipes_file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError("Unable to read the file with any of the attempted encodings")

def main():
    load_dotenv()

    # Set the URL for the local API
    BASE_URL = "http://127.0.0.1:5000/v1"

    # Which model we want the AI Chef to use
    MODEL = "local-model"  # Adjust this to match your local model's name

    # Read all the recipes that we saved in the file
    try:
        recipes = read_recipes()
    except ValueError as e:
        print(f"Error reading recipes: {e}")
        return

    messages = [
        {
            "role": "system",
            "content": f"""
                You are a Montenegrin AI Chef. You should only respond about the recipes you know. If you don't know the recipe, say so, don't make it up.
                These are the types of requests you allow:
                1. If the user gives lists you some ingredient, give them a list of names of the recipes that contain those ingredient. Just the name, don't give any details.
                2. If the user tells you a dish name, provide a detailed recipe.
                3. If the users suggests a recipe or asks for improvements for one, even if you don't know it, offer a constructive critique with suggested improvements.
                If the user asks anything else, explain that it's outside your scope, and what you are able to do.

                These are the recipes you know:
                {recipes}
            """,
        }
    ]

    while True:
        user_input = input("(Type \"exit\" to stop) Ask the AI Chef: ")

        if user_input == "exit":
            break

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f"{BASE_URL}/chat/completions",
                    json={
                        "model": MODEL,
                        "messages": messages,
                        "stream": True,
                    },
                    stream=True,
                    timeout=30  # Set a timeout of 30 seconds
                )

                response.raise_for_status()  # Raise an exception for bad status codes

                collected_messages = []
                for line in response.iter_lines():
                    if line:
                        chunk = line.decode('utf-8').strip()
                        if chunk.startswith("data: "):
                            chunk = chunk[6:]  # Remove "data: " prefix
                            if chunk != "[DONE]":
                                chunk_content = chunk.strip()
                                print(chunk_content, end="", flush=True)
                                collected_messages.append(chunk_content)

                print('\n')
                messages.append(
                    {
                        "role": "assistant",
                        "content": "".join(collected_messages)
                    }
                )
                break  # If successful, break out of the retry loop

            except (ChunkedEncodingError, RequestException) as e:
                print(f"Error occurred: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in 5 seconds... (Attempt {attempt + 2}/{max_retries})")
                    time.sleep(5)
                else:
                    print("Max retries reached. Please check your local API server.")
                    break

    print("Thanks for using our AI Chef!")

# Check if we're running as the main file
if __name__ == "__main__":
    main()
