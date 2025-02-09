import os
import shutil

def create_folders (base_file, categories):
    for folder in categories.values():
        folder_path = os.path.join(base_file,folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def move_files(base_file, categories):
    for file in os.listdir(base_file):
        file_path = os.path.join(base_file,file)

        if os.path.isfile(file_path):
            file_ext = file.split('.')[-1].lower()


            for ext, folder in categories.items():
                if file_ext in ext:
                    dest_folder = os.path.join(base_file,folder)
                    shutil.move(file_path , dest_folder)
                    print(f"Moved: {file} -> {folder}/")
                    break

def main():
    base_file = "C:\\Users\\ASUS\\Desktop\\test4"
    if not os.path.exists(base_file):
        print("The folder does not exist")
        return 

    categories = {
        ("jpg", "jpeg", "png", "gif", "bmp"): "Images",
        ("mp4", "mkv", "avi", "mov"): "Videos",
        ("mp3", "wav", "flac"): "Audio",
        ("pdf", "docx", "txt", "xlsx", "pptx"): "Documents",
        ("zip", "rar", "7z"): "Compressed",
        ("exe", "msi"): "Programs",
        ("py", "java", "cpp", "js", "html", "css"): "Code Files"
    }

    create_folders(base_file, categories)
    move_files(base_file, categories)
    print("Organizing files is done")

if __name__ == "__main__":
    main()