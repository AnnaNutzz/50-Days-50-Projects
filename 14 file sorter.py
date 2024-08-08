import os
import logging
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, src_path, name):
    if os.path.exists(os.path.join(dest, name)):
        unique_name = make_unique(dest, name)
        old_path = os.path.join(dest, name)
        new_path = os.path.join(dest, unique_name)
        os.rename(old_path, new_path)
    os.rename(src_path, os.path.join(dest, name))

class MovingHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        name = os.path.basename(event.src_path)
        self.check_image_files(event.src_path, name)
        self.check_document_files(event.src_path, name)

    def check_image_files(self, src_path, name):
        dest_dirs = {
            "mod 1": "/Module 1",
            "mod 2": "/Module 2",
            "mod 3": "/Module 3",
            "mod 4": "/Module 4",
            "mod 5": "/Module 5",
            "assignment": "/assignments",
            "misc": "/misc"
        }
        
        for key, dest_dir in dest_dirs.items():
            if key in name.lower():
                move_file(src_path, dest_dir, name)
                logging.info(f"Moved image/document file: {name} to {dest_dir}")
                return
        
        move_file(src_path, "/misc", name)
        logging.info(f"Moved image/document file: {name} to /misc")

if __name__ == "__main__":
    src_dir = input("Enter the Folder to sort (as a path): ")
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = src_dir
    event_handler = MovingHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
