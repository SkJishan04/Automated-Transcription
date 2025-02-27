import json
import os
from config import SESSION_FILE

def load_session():
    """Loads session data from a file to track processed files."""
    
    # Check if session file exists and load its content
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as session_file:
            return json.load(session_file)
    
    # Return an empty dictionary if the session file doesn't exist
    return {}

def save_session(processed_files):
    """Saves the current session data (processed files) to a file."""
    
    # Write the processed files to the session file
    with open(SESSION_FILE, "w") as session_file:
        json.dump(processed_files, session_file, indent=4)

def mark_as_processed(file_path):
    """Marks a file as processed by updating the session data."""
    
    # Load the current session data
    session_data = load_session()
    
    # Update the session with the processed file
    session_data[file_path] = "processed"
    
    # Save the updated session data
    save_session(session_data)

def is_processed(file_path):
    """Checks if a file has already been processed in the session."""
    
    # Load the session and check if the file is marked as processed
    session_data = load_session()
    return session_data.get(file_path) == "processed"
