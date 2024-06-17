import os
import shutil
import datetime
import schedule
import time

# 定义源目录和目标目录的路径
SOURCE_DIR = "/Users/xcc/Pictures/Screenshots"
DESTINATION_DIR = "/Users/xcc/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    """将源目录复制到目标目录，以当前日期命名目标目录"""
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
    """调度每天定时备份任务"""
    schedule.every().day.at(time_str).do(lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR))

def main():
    backup_time = "19:00"  # 设定备份时间
    schedule_backup(backup_time)
    
    print(f"Backup scheduled daily at {backup_time}")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次任务

if __name__ == "__main__":
    main()
