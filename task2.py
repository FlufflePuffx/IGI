import json
import os
import re

FUNCTIONS = '''
* add
* remove
* find
* list
* grep
* save
* switch
* exit
'''


class Container:
    _username: str
    _storage: set[str] = set()
    _filename: str

    def __init__(self, username):
        self._username = username
        self._filename = f'./data/{username}.json'
        self.load()

    def add(self, key):
        self._storage.add(key)

    def remove(self, key):
        if key in self._storage:
            self._storage.remove(key)

    def find(self, key) -> bool:
        return key in self._storage

    def list(self):
        print(self._storage, sep=' ')

    def grep(self, regex) -> list:
        return filter(lambda key: re.match(regex, key), self._storage)

    def save(self):
        os.makedirs(os.path.dirname(self._filename), exist_ok=True)
        with open(self._filename, "w") as outfile:
            json.dump(list(self._storage), outfile)

    def load(self):
        if os.path.exists(self._filename):
            with open(self._filename, 'r') as infile:
                self._storage = set(json.load(infile))

    def switch(self, username):
        self._username = username
        self._filename = f'./data/{username}.json'
        self._storage.clear()
        self.load()
