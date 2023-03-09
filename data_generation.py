import pandas as pd
import numpy as np
import random
from random import *

dict_nuc = {1:"A", 2:"T", 3:"C", 4:"G"}


def make_pat(num_patterns, len_pattern):
    set_pats = set()
    dict_nuc = {1: "A", 2: "T", 3: "C", 4: "G"}

    while len(set_pats) != num_patterns:
        s_temp = ''.join(pd.Series(np.random.randint(low=1, high=4, size=len_pattern)).map(dict_nuc).values)
        set_pats.add(s_temp)
    return set_pats

def add_pats_to_str(pat, string, gap = 1):
    locs = np.random.choice(np.arange(0,len(string) - len(pat[0]), len(pat[0])+gap ), size=len(pat), replace=False)
    locs = sorted(locs)
    # print(locs)
    for i in range(len(locs)):
        string = string[:locs[i]] + pat[i] + string[locs[i]+len(pat[i]):]
    return string, locs

def make_str_without_pats(pat, len_string):
    string = ""
    dict_nuc = {1:"A", 2:"T", 3:"C", 4:"G"}
    s_temp = ''.join(pd.Series(np.random.randint(low=1, high=4, size=len_string)).map(dict_nuc).values)
    locs = [s_temp.find(x) for x in pat]
    locs = list(filter((-1).__ne__, locs)).copy()
    kkk = 2
    while len(locs) != 0:
        for idx in locs:
            list_nuc = ["A","T", "C", "G"]
            list_nuc.remove(s_temp[idx])
            s_temp = s_temp[:idx] + np.random.choice(list_nuc, size=1)[0] + s_temp[idx+1:]
        locs = [s_temp.find(x) for x in pat]
        locs = list(filter((-1).__ne__, locs)).copy()
        kkk -=1
    return s_temp
