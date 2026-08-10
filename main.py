import os

# made by kurlwin on github (https://github.com/Kurlwin)

FILE_CATEGORIES = ["Photo", "Video", "Audio", "Other"]
file_extensions = {
    "Photo": ["png", "jpg", "jpeg", "avif", "webp", "jfif", "gif", "tiff", "bmp"],
    "Video": ["mp4", "mov", "m4v", "mkv", "wmv", "avi"],
    "Audio": ["mp3", "wav", "ogg", "m4a", "aiff", "au"]
} # these are just common file extensions, you can probably add more

def categorize_file(extension):
    for k, v in file_extensions.items():
        if extension in v:
            return k
    return FILE_CATEGORIES[-1]
    

for cat in FILE_CATEGORIES:
    if not os.path.exists(f"sorted/{cat}"):
        os.makedirs(f"sorted/{cat}")

unsorted_files = os.listdir("unsorted")

if len(unsorted_files) == 0:
    print("There are no files in the \"unsorted\" folder")
else:
    for file in unsorted_files:
        print(f"Processing '{file}'")
        if not "." in file and not os.path.exists(f"sorted/Other/{file}"):
            os.rename(f"unsorted/{file}", f"sorted/Other/{file}")
        elif os.path.exists(f"sorted/Other/{file}"):
            print(f"'{file}' is already in the 'Other' folder")
        else:
            cuts = file.split(".")
            extension = cuts[-1]
            cat = categorize_file(extension)
            if not os.path.exists(f"sorted/{cat}/{file}"):
                os.rename(f"unsorted/{file}", f"sorted/{cat}/{file}")
            else:
                print(f"'{file}' is already in the '{cat}' folder")