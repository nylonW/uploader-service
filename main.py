import os
import subprocess
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VideoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".mp4"):
            # Check if there's a corresponding metadata JSON file
            json_file = event.src_path.replace(".mp4", ".json")
            if os.path.exists(json_file):
                self.upload_to_youtube(event.src_path, json_path=json_file, channel_folder=os.path.dirname(event.src_path))

    def upload_to_youtube(self, video_path, json_path, channel_folder):
        cmd = [
            "./youtubeuploader",
            "-filename", video_path,
            "-metaJSON", json_path,
            "-secrets", os.path.join(channel_folder, "client_secrets.json")
        ]
        result = subprocess.run(cmd)
        
        # If the upload was successful, move the files
        if result.returncode == 0:
            uploaded_folder = os.path.join("/uploaded", os.path.basename(channel_folder))
            if not os.path.exists(uploaded_folder):
                os.makedirs(uploaded_folder)
            shutil.move(video_path, os.path.join(uploaded_folder, os.path.basename(video_path)))
            shutil.move(json_path, os.path.join(uploaded_folder, os.path.basename(json_path)))
            print("Uploaded video to YouTube!")

def watch_folder(base_folder):
    observer = Observer()
    for root, dirs, _ in os.walk(base_folder):
        for dir in dirs:
            observer.schedule(VideoHandler(), os.path.join(root, dir), recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    base_folder = "channels"
    watch_folder(base_folder)
