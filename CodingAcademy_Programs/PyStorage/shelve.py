import shelve

from PyStorage.serialising import tracker
from PyStorage.writing_to_files import feeds

shelf = shelve.open("lxf-test")
shelf["feeds"] = feeds
shelf["tracker"] = tracker
shelf.close()
