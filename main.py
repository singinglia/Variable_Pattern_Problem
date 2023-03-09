

from assembly import AvengersAssemble
from data_generation import *
from DouglasFunctions import validate
import time
from Search import Search

if __name__ == '__main__':

    df = pd.DataFrame(columns=["String", "Patterns", "Location", "Exclusion"])

    num_strings = 5
    len_strings = 150
    len_pattern = 7
    num_patterns = 5
    num_muts = 0
    pats = make_pat(num_patterns, len_pattern)  # make patterns list
    pats = list(pats)
    while num_strings > 0:
        #     randomly choose the number of patters to be in this string
        #     np.random.randint(low=1, high=4, size=len_pattern)
        st = make_str_without_pats(pats, len_strings)  # create strings without pattern list
        st, locs = add_pats_to_str(pats, st, num_muts)  # add patern list to string at random places with atleast 1 gap
        new_row = {"String": st, "Patterns": pats, "Location": locs}
        df = df.append(new_row, ignore_index=True)
        num_strings -= 1

    inclusion = df["String"].values
    exclusion = pats[2]
    m = .7
    l_min = len_pattern - 1
    print(pats)
    print(inclusion)

    tuples = [(100,150)]*5 
    print(Search(inclusion, tuples, .9, 7))

    start = time.time()
    bestPatternList, indexLists = AvengersAssemble(inclusion, ["WVWVWVWVW"], m, l_min, t=10, jump=5)
    end = time.time()

    print("Run time:", end-start)
    print("Best Pattern List")
    print(len(bestPatternList))
    print(bestPatternList)
    print(indexLists)

    validate(inclusion, exclusion, m, l_min, indexLists)



    bestPatternList, indexLists = AvengersAssemble(inclusion, exclusion, m, l_min, t=100)


    print("Exclusion")
    print(exclusion)
    print("Best Pattern List")
    print(len(bestPatternList))
    print(bestPatternList)

    # print(inclusion)
    # print(exclusion)
    # print(m)
    # print(l_min)
    #
    # print(indexLists)

