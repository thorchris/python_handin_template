import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass

class TextComparer():
    def __init__(self, url_list):
        self.url_list = url_list
        self._filenames = []
        self.num = 0
            
    def download(self, url, filename):
        print("downloading: ",url)
        r = requests.get(url)
        if r.status_code == 404:
            raise NotFoundException("404 - Not found")
    
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)
    
        
    def multidownload(self):
        print("download started")
        folder = 'modules/Week6/books/'
    
        for index, val in enumerate(self.url_list):
            s = folder + "bog" + str(index) + ".txt"
            self._filenames.append(s) 
           
        with ThreadPoolExecutor(5) as ex:
            ex.map(self.download, self.url_list, self._filenames)
            
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.num <= len(self._filenames)):
            num = self.num
            self.num += 1
            return self._filenames[num]
        else:
            self.num = 0
            raise StopIteration


    def urllist_generator(self):
        for url in self.url_list:
            yield url
    
    def avg_vowels(self, text):
        vowels = set("AEIOUaeiou")
        countV = 0
        file = open(text, 'r')
        text_file = file.read()
        for c in text_file:
            if c in vowels:
                countV += 1
        return countV
    
    
    def hardest_read(self, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, self._filenames)
        results = dict(zip(self._filenames, list(res)))
        return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
