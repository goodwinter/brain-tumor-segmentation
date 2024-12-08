import os
import requests
from zipfile import ZipFile

def download_and_extract(url, output_dir):
    zip_path = "dataset.zip"
    print(f"Downloading dataset from {url}...")
    response = requests.get(url)
    with open(zip_path, "wb") as f:
        f.write(response.content)
    print("Download complete. Extracting...")
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Dataset extracted to {output_dir}")

    os.remove(zip_path)

if __name__ == "__main__":
    dataset_url = "https://your-dataset-link.com"  # 替換成實際的數據集下載鏈接
    output_directory = "data/"
    os.makedirs(output_directory, exist_ok=True)
    download_and_extract(dataset_url, output_directory)
