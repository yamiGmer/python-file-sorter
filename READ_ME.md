File Sorter

A Python desktop application for analyzing and organizing files in a selected folder.

Basic Setup
1. Create a Virtual Environment
python -m venv .venv

2. Activate the Virtual Environment

On Windows:

.venv\Scripts\activate

3. Install Dependencies

Install the required Python packages:

pip install customtkinter CTkMessagebox

Installed Packages
customtkinter — Used to create the graphical user interface.
python-dotenv — Used for loading environment variables from a .env file.
CTkMessagebox — Used for displaying custom message boxes.
Project Structure

The application uses a class-based structure centered around the FileSorterApp class.

The application is separated into modules responsible for:

UI/window setup
UI widgets
File sorting
Sorting categories/rules
File path validation and utilities
Running the Application

Make sure the virtual environment is activated, then run the main Python file:

python main.py