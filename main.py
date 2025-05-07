import os
import shutil

# Define folder categories
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Others': []
}

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"❌ Path '{folder_path}' is not a valid directory.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    move_file(file_path, folder_path, category)
                    moved = True
                    break

            if not moved:
                move_file(file_path, folder_path, 'Others')

def move_file(file_path, base_path, category):
    category_path = os.path.join(base_path, category)
    os.makedirs(category_path, exist_ok=True)
    shutil.move(file_path, os.path.join(category_path, os.path.basename(file_path)))
    print(f"✅ Moved '{file_path}' to '{category}/'")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_folder(folder)
