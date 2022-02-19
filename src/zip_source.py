import os
import zipfile

SOURCE_ZIP_NAME = 'source_code.zip'


def zip_dir(directory: str, zip_file: str):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file))


def zip_source():
    if os.path.exists(SOURCE_ZIP_NAME):
        os.remove(SOURCE_ZIP_NAME)
    zip_dir('src', SOURCE_ZIP_NAME)
    print(f'Zip file created: {SOURCE_ZIP_NAME}')


'''
Remember to change the Working Directory in run configuration to Google_Hashcode_2022!
'''
if __name__ == '__main__':
    zip_source()
