# Montenegrin AI Chef

Our AI Chef is an interactive command-line application that uses a local AI model to provide knowledge of Montenegrin recipes and culinary advice.

## Features

The AI Chef supports three main functionalities:

1. Ingredient-based recipe suggestions: Give a list of recipe names that can be made with provided ingredients.
2. Detailed recipe instructions: List out the steps for making a specific recipe known to the AI.
3. Recipe critique and improvement: Provide constructive feedback on recipes suggested by users.

If asked to do anything else, the AI will list all the "commands" it can perform.

All known recipes can be found in the [recipes.txt](./recipes.txt) file.

For more details, see [The report](./report.md).

## Prerequisites

- Python 3.x
- Local text generation API (text-generation-webui)

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Perpernet/Montenegrin-AI-Chef-Local-API-.git
   cd Montenegrin-AI-Chef-Local-API-
   ```

2. Set up and activate the virtual environment:
   ```sh
   python3 -m venv .venv
   ```

   - On Windows with CMD:
     ```batch
     .venv\Scripts\activate.bat
     ```
   - On Windows with PowerShell:
     ```ps
     .venv\Scripts\Activate.ps1
     ```
   - On Linux/MacOS:
     ```bash
     source .venv/bin/activate
     ```

3. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your local text generation API (text-generation-webui) is running and properly configured.

2. Run the main script:
   ```sh
   python main.py
   ```

3. Follow the prompts to interact with the AI Chef.

## API Integration

This project uses a separate local text generation API. For more information, see [text-generation-webui-api](https://github.com/Perpernet/text-generation-webui-api).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]