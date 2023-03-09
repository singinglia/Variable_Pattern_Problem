from random import *
import pandas as pd
from collections import Counter


def ProfileProb(seq, k, prob_dic):
    minn = 0
    min_pat = []
    for i in range(len(seq) - k + 1):
        pat = seq[i:i+k]
        seq_sum = 0
        for j in range(k):
            seq_sum += prob_dic[pat[j]][j]
        if minn < seq_sum:
            minn = seq_sum
            min_pat = pat
    return min_pat

#def HammingDistance(s1,s2):
#    return sum([1 for i in range(len(s1)) if  s1[i]==s2[i]])

def Score(dna_list, motiff):
    st, end = motiff[0]
    k = end - st
    median_str =  median_string(dna_list, motiff)
    score = []
    for i, (mot_st, mot_end) in enumerate(motiff):
            score.append(hamming_distance(median_str, dna_list[i][mot_st:mot_end]))
    return 1 - (min(score)/k)

def Profile_creator(dna_list, motiff):
    st, end = motiff[0]
    k = end - st
    profile_matrix = {"A": [1]*k, "C": [1]*k, "G": [1]*k, "T": [1]*k}
    for indx, (st_nei,end_nei) in enumerate(motiff):
        idx = 0
        for nuc in str(dna_list[indx][st_nei:end_nei]):
            profile_matrix[nuc][idx] +=1
            idx+=1
    for j in range(k):
        col_sum =0
        for i in ["A", "C", "G", "T"]:
            col_sum += profile_matrix[i][j]
        for i in ["A", "C", "G", "T"]:
            profile_matrix[i][j] = profile_matrix[i][j]/col_sum
    return profile_matrix

def RandomMotif(seq, allowed_idx, k, prob_dic):
    allowed_idx_st, allowed_idx_end = allowed_idx
    rand_dic = {}    
    for i in range(allowed_idx_st, allowed_idx_end - k +1):
        pat = seq[i:i+k]
        seq_sum = 1
        for j in range(k):
            seq_sum *= prob_dic[pat[j]][j]
        rand_dic[(i,i+k)] = seq_sum
        
    keey = choices(list(rand_dic.keys()), weights=list(rand_dic.values()))  
    return keey[0]

def GibbsSampler(dna_list, part_index_list, k, t, N):
    motiff = []
    for i, (part_st, part_end) in enumerate(part_index_list):     
        rand = randint(part_st, part_end - k)
        motiff.append((rand, rand + k))      
        
    best_motif = motiff
    for j in range(N):
        i = randint(0,t-1)

        prof = Profile_creator(dna_list, best_motif[:i] + best_motif[i+1:])
        ith_motif_st, ith_motif_end = RandomMotif(dna_list[i], part_index_list[i], k, prof)

        motiff = best_motif[:i] + [(ith_motif_st,ith_motif_end)] + best_motif[i+1:]
        if Score(dna_list, motiff) < Score(dna_list,best_motif):
            best_motif = motiff.copy()
        return best_motif


def Search(I, part_index_list, Match, lmin):
    """
    Inclusion -> I
    part_index_list -> Partition index of each string in I
    Match -> Minimum match Threshold
    lmin -> Minimum length of the motif
    """
    assert all([min(x)>=0 for x in part_index_list]), 'error provided index_list must not contain negative values'
    st0, end0 = part_index_list[0]
    len_part = end0-st0
    best_motifs = []
    min_score = 1 - Match
    count = 0
    ctt = 0
    while count < 10000:
        lmin_rand = choices(list(range(len_pattern, len_part)), weights=1/np.arange(len_pattern, len_part)**3)[0]
        while ctt < 10000:
            motifs = GibbsSampler(I, part_index_list, lmin_rand, len(I), len_part)
            ss = Score(I, motifs)
            if ss <= min_score:
                best_motifs = motifs
                min_score = ss
                return best_motifs   
            ctt +=1
        count += 1
    return best_motifs
