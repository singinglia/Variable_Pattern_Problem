
from assembly import AvengersAssemble
from data_generation import *

if __name__ == '__main__':

    df = pd.DataFrame(columns=["String", "Patterns", "Location", "Exclusion"])

    num_strings = 5
    len_strings = 1000
    len_pattern = 11
    num_patterns = 7
    pats = make_pat(num_patterns, len_pattern)  # make patterns list
    pats = list(pats)
    while num_strings > 0:
        #     randomly choose the number of patters to be in this string
        #     np.random.randint(low=1, high=4, size=len_pattern)
        st = make_str_without_pats(pats, len_strings)  # create strings without pattern list
        st, locs = add_pats_to_str(pats, st)  # add patern list to string at random places with atleast 1 gap
        new_row = {"String": st, "Patterns": pats, "Location": locs}
        df = df.append(new_row, ignore_index=True)
        num_strings -= 1

    inclusion = df["String"].values
    exclusion = pats[2]
    m = 1
    l_min = len_pattern - 1

    bestPatternList, indexLists = AvengersAssemble(inclusion, "WVWVWVWVW", m, l_min, t=1000)

    print("Best Pattern List")
    print(len(bestPatternList))
    print(bestPatternList)

    bestPatternList, indexLists = AvengersAssemble(inclusion, exclusion, m, l_min, t=1000)


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

