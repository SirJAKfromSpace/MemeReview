import json
import os
import shutil


with open("plot_data.json") as f:
    centroids = json.load(f)["centroids"]


ignore = open('.gitignore', 'a')


def create_folders():
    for r in centroids:
        print(r["label"])
        ignore.write(f'{r["label"]}\n')
        try:
            os.makedirs(r["label"])
            ignore.write(r["label"])
        except FileExistsError:
            print("Folder already exists: Skipping")

    ignore.close()


def move_images():
    for key in centroids:
        try:
            shutil.move(f'preprocess/data/memes/{key["img"]}', f'{key["label"]}/{key["img"]}')
        except FileNotFoundError:
            print(f'{key["img"]} does not exist in /preprocess/data/memes')
        except FileExistsError:
            print(f'{key["img"]} already exists in {key["label"]}')


create_folders()
move_images()
