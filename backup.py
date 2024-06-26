import os
import shutil
import datetime
import schedule
import time

# Define the source and destination directory paths
SOURCE_DIR = "～Pictures/Screenshots"
DESTINATION_DIR = "～Desktop/Backups"

def copy_folder_to_directory(source, dest):
    """Copy the source directory to the destination directory, naming the destination directory with the current date"""
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        if not os.path.exists(dest_dir):
            shutil.copytree(source, dest_dir)
            print(f"Folder copied to: {dest_dir}")
        else:
            print(f"Folder already exists in: {dest_dir}")
    except Exception as e:
        print(f"Error copying folder: {e}")

def schedule_backup(time_str):
    """Schedule the daily backup task"""
    schedule.every().day.at(time_str).do(lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR))

def main():
    backup_time = "19:00"  # Set the backup time
    schedule_backup(backup_time)
    
    print(f"Backup scheduled daily at {backup_time}")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check for tasks every minute

if __name__ == "__main__":
    main()

