import os
import hashlib
import csv
from tqdm import tqdm

def get_md5(filename):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def hash_and_rename_files():
    """Hash all files in the directory except the script itself and rename them to their MD5 hashes."""
    script_name = os.path.basename(__file__)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    files_to_process = [f for f in os.listdir(current_dir) if f != script_name and os.path.isfile(os.path.join(current_dir, f))]
    
    hash_map = {}  # To store original filenames and their corresponding hashes
    new_filenames = {}  # To store old and new filenames for CSV generation
    with tqdm(total=len(files_to_process), desc="Total Progress") as pbar_total:
        for filename in files_to_process:
            file_path = os.path.join(current_dir, filename)
            file_hash = get_md5(file_path)
            hash_map[filename] = file_hash
            new_filename = file_hash + os.path.splitext(filename)[1]
            os.rename(file_path, os.path.join(current_dir, new_filename))
            new_filenames[filename] = new_filename
            pbar_total.update(1)
            tqdm.write(f"Hashed and Renamed {filename} to {new_filename}")
    tqdm.write("All files have been hashed and renamed successfully.")
    return hash_map, new_filenames

def write_csv(data, filename):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Old Filename", "New Filename"])
        for key, value in data.items():
            writer.writerow([key, value])
    tqdm.write(f"CSV file '{filename}' has been generated successfully.")

if __name__ == "__main__":
    hash_map, new_filenames = hash_and_rename_files()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    csv_path = os.path.join(script_dir, "EmmDee5.csv")
    write_csv(new_filenames, csv_path)
