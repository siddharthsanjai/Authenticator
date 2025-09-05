# Authenticator
A small Flask project that renders a login page at the route /login using templates, along with a command line flow that creates users, saves credentials to a JSON file, and performs simple authentication in the terminal. The script reads and writes a JSON dictionary from a file named Credentials.txt using Python’s json module.

## Features
- Web route /login that returns a login.html file with Flask’s render_template helper.
- Command line functions to create a user, save credentials as JSON, and authenticate with a username and code.
- File based persistence using json.load and json.dump for reading and writing a dictionary to disk.

## How it works
- Flask looks for HTML templates inside a folder named templates, and render_template will automatically load login.html from there.
- The CLI flow creates a username and numeric code, stores them in a JSON file, then checks future logins against the in memory dictionary and file contents.
- The code currently appends JSON to the credentials file, which can lead to invalid JSON, so writing a full JSON object in write mode is often safer for a single object file.

## Requirements
- Python 3.x with the standard library json module available by default.
- Flask installed in the environment to run the web route and render templates.
- A templates folder containing login.html so the /login route can render the page.

## Installation
- Create a project folder and place the script file inside it, for example as app.py.
- Create a templates folder next to app.py and add a file named login.html inside it for the route to render.
- Install Flask into the environment with pip install Flask to make the app and render_template available.

## Project structure
- app.py or main script containing the Flask app, the /login route, and the CLI user functions.
- templates/login.html which is the page returned by the /login route using render_template.
- Credentials.txt which stores a JSON dictionary of usernames mapped to numeric codes for the CLI flow.

## Running the web route
- Use the Flask CLI by pointing FLASK_APP to the script that defines app, then run flask run from the project folder.
- The development server will start and serve the app on http://127.0.0.1:5000, so visit /login to load the template.
- Flask’s CLI looks for the app object on import, and the templates folder must be present so render_template can find login.html.

## Running the CLI flow
- Run the script directly with Python to follow the prompts for creating a username and entering a numeric code in the terminal.
- The flow uses json.load and json.dump to keep a dictionary of users and codes in Credentials.txt between runs.
- After authentication, the flow can update the code and write the updated dictionary back to the file for persistence.

## Notes and limitations
- The script mixes a Flask web route with a blocking terminal input loop, and calling CLI functions at import can interfere with flask run since Flask imports the module to discover app.
- It is common practice to place CLI logic under if __name__ == "__main__": so the web server can import the app without triggering input prompts.
- Templates must be stored in a folder named templates for render_template to work, otherwise Flask will raise a template not found error.

## Credentials file details
- json.dump writes a Python object to a file as JSON and json.load reads it back into a Python object, which is suitable for simple credential dictionaries in a local file.
- Appending JSON to the same file can make the file invalid, so writing a single JSON object with json.dump in write mode is usually the simplest approach for this layout.
- If a JSONDecodeError occurs when reading credentials, the file likely has invalid JSON and should be rewritten as a single valid object.

## Security tips
- Plain text credential storage is not secure, and frameworks typically recommend hashing secrets rather than storing them directly.
- The Flask tutorial shows how to add user accounts with proper password hashing using common helpers, which is safer than storing raw codes.
- Consider moving to a simple user table with hashed secrets if this project grows beyond a demo or learning exercise.

## Troubleshooting
- Template not found errors usually mean the login.html file is not inside the templates folder at the correct path.
- If flask run does nothing or waits for input, remove or guard any input calls that execute during import, then run again with FLASK_APP set.
- If json.load fails with a JSONDecodeError, rewrite Credentials.txt as valid JSON or switch to using json.dump in write mode for a single object per file.



