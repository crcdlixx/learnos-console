import zipfile
import os

def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    zip_file = input("请输入要解压的.zip文件路径：")
    extract_to = '/root/'  # 设置解压目标路径为/root/

    # 检查目标路径是否存在，如果不存在则创建
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    unzip_file(zip_file, extract_to)
    print(f"{zip_file} 已成功解压到 {extract_to} 目录中。")

if __name__ == "__main__":
    main()
