import json
from glob import glob


def add_meme_type():
    """  Adds the type of meme attribute to the target json """

    target_file = 'meme_metadata.json'
    with open(target_file) as f:
        target = json.load(f)

    dir_paths = glob("memes/[!*ini, !*jpg]*")

    dir_ls = [fp for fp in dir_paths]
    print(dir_ls)

    for folder in dir_ls:
        print("\nOpening: ", folder)

        file_paths = glob(f'{folder}\*jpg')
        # print(file_paths)

        for file_path in file_paths:
            file_path = file_path.split(f'{folder}\\')[1].split('.jpg')[0]
            print(file_path)

            for i in target:
                if i['id'] == file_path:
                    i["type"] = folder.split('memes\\')[1]

    print(target)

    print("Press any key to write changes?")
    n = input()
    if n is not None:
        f = open(target_file, "w")
        json.dump(target, f)


add_meme_type()  # run
