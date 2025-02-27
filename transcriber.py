import os
import whisper
from session_manager import mark_as_processed, is_processed

# Load Whisper model
model = whisper.load_model("base")

def transcribe_file(file_path):
    """Transcribes an audio/video file using Whisper and saves the output as a text file."""
    
    # Skip transcription if the file has already been processed
    if is_processed(file_path):
        print(f"Skipping already processed file: {file_path}")
        return
    
    print(f"Starting transcription for: {file_path}")
    
    try:
        # Transcribe the audio/video file
        result = model.transcribe(file_path)
        
        # Save the transcription result to a text file
        with open(file_path + ".txt", "w") as text_file:
            text_file.write(result["text"])
        
        print(f"Transcription saved successfully: {file_path}.txt")
        
        # Mark the file as processed to avoid re-processing
        mark_as_processed(file_path)
    
    except Exception as e:
        # Print error message if transcription fails
        print(f"Error processing {file_path}: {e}")
