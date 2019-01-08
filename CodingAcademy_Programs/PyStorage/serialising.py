import pickle

from PyStorage.writing_to_files import feeds

...

with open("lxf-test.txt", "a") as file:
    pickle.dump(feeds, file)

...

with open("lxf-test.txt", "r") as file:
    feeds = pickle.load(file)

# Shelves in Python

tracker = {"bbc.co.uk": {"last-read": "foo", "num-unread": 10, },
           "linuxformat.com":
               {"last-read": "bar", "num-read": 5, }}
