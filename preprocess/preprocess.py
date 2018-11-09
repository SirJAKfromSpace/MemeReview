from datetime import datetime
import json
from pprint import pprint


def local_time(ts):
    """" Converts UTC to readable time."""
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')


def clean_data(file):
    """" Removes unnecessary data and formats data accordingly """
    data = []

    with open(file) as f:
        j = json.load(f)

    for i in j:
        data.append({"index": i,
                     "id": j[str(i)]['id'],
                     "upvotes": j[str(i)]['ups'],
                     "date": local_time(j[str(i)]['created_utc'])})

    pprint(data)

    with open('data/postprocessed.json', 'w') as outfile:
        json.dump(data, outfile)


def format_data(file):
    """" Formats the json data. """
    data = []

    with open(file) as f:
        j = json.load(f)

    for i in j:
        data.append({"index": i,
                     "id": j[str(i)]['id'],
                     "author": j[str(i)]['author'],
                     "thumbnail": j[str(i)]['thumbnail'],
                     "media": j[str(i)]['media'],
                     "upvotes": j[str(i)]['ups'],
                     "downvotes": j[str(i)]['downs'],
                     "date": local_time(j[str(i)]['created_utc'])})

    pprint(data)

    with open('data/postprocessed.json', 'w') as outfile:
        json.dump(data, outfile)
     

format_data('data/original.json')  # location to your json file
