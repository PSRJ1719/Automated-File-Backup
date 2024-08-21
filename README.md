# Automated File Backup

This Python script automates the process of backing up a specified folder to a destination directory. The backup process is scheduled to run daily at a specified time, creating a new folder in the destination directory named with the current date.

## Features

- **Automated Backups:** The script automatically copies the contents of a specified source folder to a destination folder every day at a scheduled time.
- **Date-Named Backups:** Each backup is stored in a new folder named with the current date, ensuring that backups are organized and easily accessible.
- **Error Handling:** The script checks if the backup folder for the current date already exists to avoid duplicate backups and provides error messages for any issues that arise during the copy process.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x
- Required Python packages: `schedule`

You can install the required package using pip:

pip install schedule

## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   git clone https://github.com/PSRJ1719/Automated-File-Backup.git

2. **Navigate to the Script Directory:**

   Navigate to the directory where the script is located:

   cd Automated-File-Backup

3. **Set Source and Destination Directories:**

   Edit the script to define your source and destination directories. Replace the `SOURCE_DIR` and `DESTINATION_DIR` variables with the paths to the folders you want to back up and the location where you want the backups to be stored:

   SOURCE_DIR = "path/to/source_directory"
   DESTINATION_DIR = "path/to/destination_directory"

4. **Set the Backup Time:**

   In the `main` function, adjust the `backup_time` variable to the time you want the backup to occur daily (in 24-hour format):

   backup_time = "19:00"  # Set the backup time (e.g., 19:00 for 7:00 PM)

5. **Run the Script:**

   Run the script using the following command:

   python automated_backup.py

   The script will schedule the backup to run at the specified time every day. It will create a new folder in the destination directory named with the current date and copy the contents of the source directory into it.

6. **Example Output:**

   - If the backup is successful, you will see a message like:
     
     Folder copied to: path/to/destination_directory/YYYY-MM-DD
     
   - If a backup folder for the current date already exists, you will see:
   
     Folder already exists in: path/to/destination_directory/YYYY-MM-DD
     
   - If an error occurs during the copy process, an error message will be printed:
     
     Error copying folder: [Error details]
     

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
