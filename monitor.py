import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCH_DIRECTORY, SUPPORTED_FORMATS
from transcriber import transcribe_file

class NewFileHandler(FileSystemEventHandler):
    """Handles file system events, specifically new file creation, and triggers transcription."""
    
    def on_created(self, event):
        """Triggered when a new file is added to the monitored directory."""
        
        # Check if the event is a file (not a directory) and if it has a supported format
        if not event.is_directory and event.src_path.endswith(SUPPORTED_FORMATS):
            time.sleep(1)  # Small delay to ensure the file is fully written before processing
            transcribe_file(event.src_path)  # Trigger transcription for the new file

def start_monitoring():
    """Starts monitoring the specified directory for new files in real time."""
    
    # Initialize the observer and event handler
    observer = Observer()
    event_handler = NewFileHandler()
    
    # Set up the observer to watch the directory for changes (recursive search)
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=True)
    observer.start()
    
    print(f"Monitoring directory: {WATCH_DIRECTORY}")

    try:
        # Keep the monitoring running indefinitely until interrupted
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        observer.stop()  # Stop the observer on keyboard interrupt
    observer.join()  # Ensure the observer thread completes before the program exits
