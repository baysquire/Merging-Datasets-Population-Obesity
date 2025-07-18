import pandas as pd

def analyze(factbook_pop: str, factbook_obesity: str) -> pd.DataFrame:
    # read c2228.csv
    sample1 = pd.read_csv("data/c2228.csv")
        
    # read c2119.csv
    sample2 = pd.read_csv("data/c2119.csv")
        
    # rename column sample 1
    sample1.rename(
    columns = {
      "Pos":"Position",
      "Name":"Country",
      "Value":"Obesity Rate"
    }, inplace = True
    )
    # rename column sample 2
    sample2.rename(
    columns = {
      "Pos":"Position",
      "Name":"Country",
      "Value":"Population"
    }, inplace = True
    )
    
    # join the tables and extract Country, Population and Obesity Rate columns
    joinedTable = pd.merge(sample1,sample2, how="left", on="Country")
    joinedTable1 = joinedTable[["Country","Population", "Obesity Rate"]]
    
    #Obesity higher than 20 and population higher than 10,000,000
    obesity_population = joinedTable1.loc[(joinedTable1["Population"] > 10000000) & (joinedTable1["Obesity Rate"] > 20)]
    
    # sorting
    sorting = obesity_population.sort_values(by="Obesity Rate", ascending=False)
    
    #Top 10 and indexing
    topTen = sorting.head(10)
    topTen.index = range(1,11)
    
    return topTen
    
    
    
    
