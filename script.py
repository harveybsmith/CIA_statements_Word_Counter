sentences_cia = pd.read_csv("sentences_cia.csv")

from collections import Counter
def find_most_common_by_year(year, sentences_cia):
    data = sentences_cia[sentences_cia["year"] == year]
    combined_statement = " ".join(data["cleaned_statement"])
    statement_split = combined_statement.split(" ")
    counter = Counter([s for s in statement_split if len(s) > 4])
    return counter.most_common(2)

common_2000 = find_most_common_by_year("2000", sentences_cia)
common_2002 = find_most_common_by_year("2002", sentences_cia)
common_2013 = find_most_common_by_year("2013", sentences_cia)
