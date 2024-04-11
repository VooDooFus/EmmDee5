EmmDee5
EmmDee5 is a Python script designed to rename all files in a directory with their MD5 hash and generate a corresponding CSV file containing the old and new filenames. This tool facilitates the secure renaming of files while preserving a record that can be used to undo the changes with its sister script, UnnDee5.

Features
MD5 Hashing: EmmDee5 calculates the MD5 hash of each file in the specified directory to generate a unique identifier for the file contents.
File Renaming: The script renames each file with its MD5 hash to ensure uniqueness and maintain integrity.
CSV Generation: EmmDee5 creates a CSV file (EmmDee5.csv) that maps the old filenames to their corresponding MD5-based names, providing a reference for future use.
Undo Capability: The generated CSV file can be used with UnnDee5, the sister script of EmmDee5, to revert the changes and restore the original filenames.

Usage
Ensure you have Python installed on your system.
Copy the EmmDee5 script to the directory containing the files you want to rename.
Open a terminal or command prompt and navigate to the directory containing EmmDee5.

Run EmmDee5 using the following command:
python EmmDee5.py

EmmDee5 will calculate the MD5 hash of each file, rename them accordingly, and generate EmmDee5.csv in the same directory.
The CSV file will contain two columns: "Old Filename" and "New Filename," mapping the original filenames to their MD5-based names.

You can use the CSV file with UnnDee5 to revert the changes and restore the original filenames if needed.

Disclaimer
Please use this tool responsibly and ensure that you have proper backups of your files before executing the script.

Note: Renaming files with MD5 hashes may lead to collisions (multiple files with the same hash). While this is unlikely, exercise caution and verify the integrity of renamed files as needed.

/VooDooFus/
