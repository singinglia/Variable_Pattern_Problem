import random
from collections import Counter
random.seed(666, 2)
import bisect

def is_found(pi,sstarts):
 
    if len(pi)<len(sstarts):
        return False

    insert_points = [bisect.bisect_left(pi,x) for x in sstarts]
    print(insert_points)
    if len(set(insert_points))<len(insert_points):
        return False
    
    if max(insert_points)>=len(pi):
        return False
    
    return True

def hamming_distance(s1,s2):
    assert len(s1)==len(s2), 'strings must be same length'
    return sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])

def validate(I,E,match,lmin,answer):
    ret = True
    
    #match criteria
    for i in range(len(answer)):
        cur = answer[i]
        temp = [I[i][start:stop] for i,(start,stop) in enumerate(cur)]
        med = median_string(I,cur)
        cur_match = 1-max([hamming_distance(x,med)/len(med) for x in temp])>=match
        if cur_match<match:
            print("error, pattern {i} does not meet match criteria".format(i=i))
            ret = False

    #no overlap
    prev = answer[i]
    cur = answer[i+1]
    for j in range(len(prev)):
        gap = cur[j][0]-prev[j][1]
        if gap<1:
            print("error, patterns {i} and {k} do not meet gap criteria in string I[{j}]".format(i=i,j=j,k=i+1))
            ret = False

    #excluded criteria
    excluded_dic = get_excluded_dic(E,lmin)
    for i,cur in answer:
        med = median_string(I,cur)
        if is_excluded(cur,lmin,E,excluded_dic):
            print("error, pattern {i} does not meet exclusion criteria")
            ret = False
    return ret


def minmax(l):
    '''
    inputs:
        l: iterable, but basically I envision this being a list
    outputs:
        tuple of (min_value,max_value)
    '''
    lo = min(l)
    hi = max(l)
    return (lo,hi)

def get_excluded_dic(E, lmin):
    '''
    inputs:
        E: exclusion
        lmin: shortes acceptable pattern
    returns:
        dic; keys are lmin-length strings and values are lists of tuples (string_index, start_index)
            string_index indicates which E string; start_index indicates where in E[string_index] the key occurs
    '''
    
    excluded_lmin_mers = {}
    for i,e in enumerate(E):
        for j in range(len(e)-lmin+1):
            cur = E[i][j:j+lmin]
            try:
                excluded_lmin_mers[cur].append((i,j))
            except:
                excluded_lmin_mers[cur] = [(i,j)]
                
    return excluded_lmin_mers


def median_string(I, index_list):
    '''
    inputs:
        I: inclusion
        index_list: a list of start/stop coordinates corresponding to strings in I
    return:
        a string containing the most frequently occuring character at each position across I substrings
        
    errors:
    
    '''
    assert all([min(x)>=0 for x in index_list]), 'error provided index_list must not contain negative values'
    mm = minmax([x[1]-x[0] for x in index_list])
    assert mm[0]==mm[1], 'error provided index_list must define equal length substrings of I'
    

    patterns = [I[i][start:stop] for i,(start,stop) in enumerate(index_list)]

    return ''.join([Counter([x[i] for x in patterns]).most_common()[0][0] for i in range(len(patterns[0]))])


def is_excluded(p, lmin, E,ex_dic=None):
    '''
    inputs:
        p: a string
        lmin: minimum acceptable pattern length
        E: an exclusion set
        ex_dic: result of get_excluded_dic(E, lmin); if default (None) will call get_excluded_dic with given E and lmin
    outputs:
        True/False whether string p can be found exactly in any string of E
        
    '''
    if ex_dic is None:
        ex_dic = get_excluded_dic(E,lmin)
    
    try:
        assert len(p)>= lmin
        pref = p[:lmin]
        locs = ex_dic[pref]
        
        for i,start in locs:
            if p == E[i][start:start+len(p)]:
                return True
            
        return False
    except:
        return False
    
def chop(I, index_list, lmin, factor = 2, exp = 4):
    '''
    inputs:
        I: inclusion multiset of strings
        index_list: regions within inclusion strings considered valid
        lmin: minimum acceptable pattern length
        factor: chop will return index_list covering lmin*factor length substrings
        exp: higher positive values increase liklihood of randomly selected subregions appearing to the left
        
    return:
        res: list of indexes covering equal length regions of length lmin*factor
        
    errors:
        raises assertion error if index_list contains negative numbers
        raises assertion error if a substring of I defined by index_list is shorter than int(lmin*factor)
        
    '''
    assert all([min(x)>=0 for x in index_list]), 'error provided index_list must not contain negative values'
    assert all([(x[1]-x[0])>=int(lmin*factor) for x in index_list]), 'error: regions of length {x} not possible in all strings based on given index_list'.format(x=int(lmin*factor))

    
    lo = [x[1]-x[0] for x in index_list]
    
    res = []

    for i,x in enumerate(I):
        siz_range = range(index_list[i][0], index_list[i][1] - int(lmin*factor)+1)
        a = random.choices(siz_range, map(lambda y: (len(x)-y)**exp, siz_range))[0]
        res.append((a,a+int(factor*lmin)))
    return res
