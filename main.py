
from DouglasFunctions import *
from assembly import AvengersAssemble
from data_generation import *

if __name__ == '__main__':

    df = pd.DataFrame(columns=["String", "Patterns", "Location", "Exclusion"])

    num_strings = 5
    len_strings = 40
    len_pattern = 4
    num_patterns = 3
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


    bestPatternList = AvengersAssemble(df["String"].values, "WDWDWDW", .80, 4, t=100)