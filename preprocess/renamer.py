import glob
import json
import os


def find_meme_name(j, meme_id):
    """" Finds a meme ID from a json file and rename the file with the ID"""

    found = False
    name = ''
    meme = []

    for i in j:
        meme = j[str(i)]
        # print('meme[id]', meme['id'])
        # print('meme_id', meme_id)
        if meme['id'] == meme_id:
            print("\nFound", meme_id)
            print("Renaming to", str(i))
            name = str(i)
            found = True
            meme = meme['id']
            break

    if found:
        return str(name)
    else:
        return str(meme)


with open('data/original.json') as f:
    data = json.load(f)

files = glob.glob("data/memes/*.png")
files.extend("data/memes/*.jpg")

for source_name in files:
    path, fullname = os.path.split(source_name)
    print(path, fullname)
    basename, ext = os.path.splitext(fullname)
    print(basename)
    target_name = os.path.join(path, '{}{}'.format(find_meme_name(data, basename), ext))
    print(target_name)
    os.rename(source_name, target_name)





