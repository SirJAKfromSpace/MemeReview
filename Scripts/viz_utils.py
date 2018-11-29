import json
import os
import shutil
from glob import glob

with open("plot_data.json") as f:
    centroids = json.load(f)["centroids"]


def create_folders():
    """ Creates cluster folders. """
    ignore = open('.gitignore', 'a')

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
    """ Moves centroid images to cluster folders. """
    for key in centroids:
        try:
            shutil.move(f'preprocess/data/memes/{key["img"]}', f'{key["label"]}/{key["img"]}')
        except FileNotFoundError:
            print(f'{key["img"]} does not exist in /preprocess/data/memes')
        except FileExistsError:
            print(f'{key["img"]} already exists in {key["label"]}')


# create_folders()
# move_images()


def selective_move():
    """  Moves all similar clustered images to folder specified. """
    json_paths = glob("nearest_neighbors/*json")
    print(len(json_paths))
    num = 1
    for jp in json_paths:
        print(" ")
        print("~ ",num)
        num += 1
        jsonfilename = jp.split('\\')[1]
        indexfile = jsonfilename.split('.')[0]
        print("Opening: ", jsonfilename)
        if os.path.isfile('memes/'+indexfile+'.jpg') :
            with open(jp) as f:
                image_meta = json.load(f)
            print(image_meta)
            print("===================")
            print("Similar images:")
            for v in image_meta:
                print(v["filename"])

            print("Specify destination folder:")
            dest = input()

            for v in image_meta:
                try:
                    jsonrefimage = 'memes/'+v["filename"]+'.jpg'
                    if os.path.isfile(jsonrefimage) :
                        shutil.move(f'memes/{v["filename"]}.jpg', f'{dest}')
                        print("moving", jsonrefimage)
                    else: print(jsonrefimage+" already moved")
                except FileNotFoundError:
                    print(f'{v["filename"]} does not exist in source folder')

        else: print('Skipping')


# print("1) Create cluster folders\n2) Move centroid images to cluster folders\n3) Cluster images to specified folder")
#
# options = {'1': create_folders(),
#            '2': move_images(),
#            '3': selective_move()}

selective_move()
