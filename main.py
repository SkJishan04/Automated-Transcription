import os
from transcriber import transcribe_file
from monitor import start_monitoring
from config import WATCH_DIRECTORY, SUPPORTED_FORMATS
from session_manager import is_processed

def transcribe_unprocessed_files(directory):
    """Scan the directory for existing files and transcribe the ones that haven't been processed yet."""
    print("Scanning existing files for transcription...")

    # Walk through all files in the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Check if the file has a supported format
            if file_name.endswith(SUPPORTED_FORMATS):
                file_path = os.path.join(root, file_name)
                
                # If the file hasn't been processed yet, transcribe it
                if not is_processed(file_path):
                    transcribe_file(file_path)

if __name__ == "__main__":
    print("Starting the Automated Transcription System...")

    # Scan and transcribe any existing files before monitoring live files
    transcribe_unprocessed_files(WATCH_DIRECTORY)

    # Start monitoring the directory for new files to transcribe
    start_monitoring()
