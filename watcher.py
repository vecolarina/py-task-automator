import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_csv, save_processed_file
from notifier import send_notification
from config import WATCH_FOLDER, OUTPUT_FOLDER, CHECK_INTERVAL

class CSVHandler(FileSystemEventHandler):
    """
    Watches a folder for new CSV files.
    When detected — processes, saves, and sends email notification.
    """
    def on_created(self, event):
        # Only handle CSV files
        if event.is_directory:
            return
        if not event.src_path.endswith('.csv'):
            return

        print(f"\n🔔 New CSV detected: {event.src_path}")

        # Wait briefly to ensure file is fully written
        time.sleep(2)

        # Process the file
        df, summary = process_csv(event.src_path)

        if df is not None and summary is not None:
            # Save cleaned version
            save_processed_file(df, event.src_path, OUTPUT_FOLDER)

            # Send email notification
            send_notification(summary)

            print(f"✅ All done for: {event.src_path}\n")
        else:
            print(f"⚠️ Skipped: {event.src_path} could not be processed.\n")


def main():
    # Create watch folder if it doesn't exist
    os.makedirs(WATCH_FOLDER, exist_ok=True)

    print("🚀 Py Task Automator Starting...")
    print(f"👁️  Watching folder: {WATCH_FOLDER}")
    print(f"📁  Output folder: {OUTPUT_FOLDER}")
    print("⏳ Waiting for new CSV files... (Press Ctrl+C to stop)\n")

    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Stopping watcher...")
        observer.stop()

    observer.join()
    print("✅ Py Task Automator stopped.")


if __name__ == "__main__":
    main()