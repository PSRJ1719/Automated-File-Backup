# Automated File Backup

This Python script automates the process of backing up a specified folder to a destination directory on a daily basis.

## Prerequisites

-os
-shutil
-datetime
-schedule
-time


# Automated Backup Script Setup

This repository contains the necessary files to set up an automated backup script on macOS using `launchd`.

## Files

- `script.py`: The Python script that performs the backup task.
- `com.user.backup.plist`: The `launchd` configuration file to schedule the script.

## Setup Instructions

1. **Modify Paths**:
   - Open `script.py` and modify the `SOURCE_DIR` and `DESTINATION_DIR` variables to the appropriate paths on your system.
   - Open `com.user.backup.plist` and modify the `ProgramArguments` array to point to your Python interpreter and the `script.py` file. Ensure the paths are correct.

2. **Move the Plist File**:
   - Copy the `com.user.backup.plist` file to the `~/Library/LaunchAgents/` directory:
     
     cp com.user.backup.plist ~/Library/LaunchAgents/
     
3. **Load the LaunchAgent**:
   - Load the LaunchAgent using `launchctl`:
     
     launchctl load ~/Library/LaunchAgents/com.user.backup.plist
