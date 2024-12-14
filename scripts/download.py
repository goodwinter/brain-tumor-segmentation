import os
import zipfile

def extract_zip(file_path, extract_to):
    """
    解壓 .zip 文件
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"解壓完成：{file_path} 到 {extract_to}")

def extract_all_data():
    """
    解壓所有壓縮文件
    """
    # 壓縮文件的列表
    files_to_extract = [
        ("data/train1.zip", "data/train"),
        ("data/train2.zip", "data/train"),
        ("data/train3.zip", "data/train"),
        ("data/test.zip", "data/test"),
        ("data/valid.zip", "data/valid"),
    ]

    for file_path, extract_to in files_to_extract:
        if os.path.exists(file_path):
            os.makedirs(extract_to, exist_ok=True)
            extract_zip(file_path, extract_to)
        else:
            print(f"文件未找到：{file_path}")

if __name__ == "__main__":
    extract_all_data()

