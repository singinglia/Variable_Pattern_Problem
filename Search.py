from random import *
import pandas as pd

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

def Score(dna_list, motiff):
    st, end = motiff[0]
    k = end - st
    score_mat = {"A": [0]*k, "C": [0]*k, "G": [0]*k, "T": [0]*k}
    for indx, (st_nei,end_nei) in enumerate(motiff):
        idx = 0
        for nuc in str(dna_list[indx][st_nei:end_nei]):
            score_mat[nuc][idx] +=1
            idx+=1
    score = 0
    smat = list(zip(*score_mat.values()))
    for i in range(k):
            score = score + sum(smat[i]) - max(smat[i])
    return score

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
        rand = randint(0, part_end - part_st - k)
        motiff.append((rand, rand + k))      
        
    best_motif = motiff
    for j in range(N):
        i = randint(0,t-1)

        prof = Profile_creator(dna_list, best_motif[:i] + best_motif[i+1:])
        ith_motif_st, ith_motif_end = RandomMotif(dna_list[i], part_index_list[i], k, prof)

        motiff = best_motif[:i] + [(ith_motif_st,ith_motif_end)] + best_motif[i+1:]
        if Score(dna_list,motiff) < Score(dna_list,best_motif):
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
    min_score = Match*lmin
    count = 0
    while count < 10000:
        lmin_rand = randint(lmin, len_part)
        motifs = GibbsSampler(I, part_index_list, lmin_rand, len(I), min(len_part))
        ss = Score(I, motifs)
        if ss <= min_score:
            best_motifs = motifs
            min_score = ss
            print(ss)
            return best_motifs
            
            
        count += 1

    # print(best_motifs)
    
    
    return best_motifs