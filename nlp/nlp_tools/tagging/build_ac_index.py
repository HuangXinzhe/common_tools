#endoing=utf-8
import ahocorasick
import pickle

def load_names(company_name_filepath):
    # load company name dict
    names = []
    for line in open(company_name_filepath, "r", encoding="utf-8"):
        line = line.strip().split("\t")
        names.append(line[0])
        names.append(line[1])
    return names


def build_index(names, index_path):
    # implement your coding here.
    # load company names and build an ac automaton, and store as a pickle
    A = ahocorasick.Automaton()
    for n in names:
        A.add_word(n, (n, "company_name"))
    A.make_automaton()
    pickle.dump(A, open(index_path, "wb"))
    return


if __name__ == "__main__":
    company_names = load_names("../company_names/data/org_names.txt")
    build_index(company_names, "../company_names/data/company_index.pkl")