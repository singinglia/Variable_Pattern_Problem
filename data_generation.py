import pandas as pd
import numpy as np
import random
from random import *

dict_nuc = {1:"A", 2:"T", 3:"C", 4:"G"}

def random_mutate_pat(base_string, num_muts = 0):
    mut_pos = [randint(0,len(base_string)-1) for _ in range(num_muts)]
    new_string = list(base_string)
    for x in mut_pos:
        new_string[x] = choice(list(set(["A","C","G","T"])-set(new_string[x])))
    return ''.join(new_string)

def make_pat(num_patterns, len_pattern):
    set_pats = set()
    dict_nuc = {1: "A", 2: "T", 3: "C", 4: "G"}

    while len(set_pats) != num_patterns:
        s_temp = ''.join(pd.Series(np.random.randint(low=1, high=5, size=len_pattern)).map(dict_nuc).values)
        set_pats.add(s_temp)
    return set_pats

def add_pats_to_str(pat, string, gap = 1, num_muts = 0):
    locs = np.random.choice(np.arange(0,len(string) - len(pat[0]), len(pat[0])+gap ), size=len(pat), replace=False)
    locs = sorted(locs)
#     print(locs)
    for i in range(len(locs)):
#         random_mutate(, param)
        string = string[:locs[i]] + random_mutate_pat(pat[i], num_muts) + string[locs[i]+len(pat[i]):]
    return string, locs

def make_str_without_pats(pat, len_string, num_muts = 0):
    string = ""
    dict_nuc = {1:"A", 2:"T", 3:"C", 4:"G"}
    s_temp = ''.join(pd.Series(np.random.randint(low=1, high=5, size=len_string)).map(dict_nuc).values)
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
