# Montenegrin AI Chef

Our AI Chef has knowledge of some Montenegrin recipes, all of which you can find in the [recipes.txt](./recipes.txt) file.

It supports all three functionalities in a single file.

As specified in the document, it can:
1) Give user a list of recipe names that the user can make with the ingredients they provided
2) List out the steps for making the recipe, if the user asks about the specific recipe that's the AI knows.
3) Give back constructive feedback if the users asks about a recipe they thought of making.

If asked to do anything else, the AI will answer by instead listing all the "commands" it can do.

You can find the report here: [The report](./report.md)

# Setup

1) Clone the repository
```sh
git clone https://github.com/lodygens/bootcamp-ia.git
```

2) Go into the folder containing the repository, and into this homework folder
```sh
cd "bootcamp-ia/week1/Montenegrin-AI-Chef"
```

3) Set up the virtual environment
```sh
python3 -m venv .venv
```

4) Activate the virtual environment

4.1) On Windows with CMD:

4.1.1) With CMD
```batch
.venv\Scripts\activate.bat
```
4.1.2) With PowerShell:
```ps
.venv\Scripts\Activate.ps1
```

4.2) On Linux/MacOS
```bash
chmod +x .venv/bin/activate
source .venv/bin/activate
```

More info on activating virtual environments: [Venv docs](https://docs.python.org/3/library/venv.html#how-venvs-work)

4) Install all the required libraries
```sh
pip install -r requirements.txt
```

5) Create a .env file and replace "YOUR-OPENAI-KEY" with your OpenAI Key
```sh
cp .env.example .env
```

6) Use the AI Chef
```sh
python3 main.py
```
