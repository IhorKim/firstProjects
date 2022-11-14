"""
Simple program to sort pictures by collections in directory
"""
import os
import shutil

os.chdir("fall2022 photo")
counter = 0

for dir in os.listdir():
    print(counter, dir)
    try:
        os.chdir(dir)
        for file in os.listdir():  # take each photo in every dir
            if file.endswith("_z.jpg"):  # sort photos
                collection = file[2:5]  # in the name of a photo
                collection_dir = "../NEW PHOTO" + "/" + collection

                if not os.path.exists(collection_dir):
                    os.mkdir(collection_dir)

                shutil.copy2(file, collection_dir)

        os.chdir("..")
        counter += 1
    except NotADirectoryError:
        pass
