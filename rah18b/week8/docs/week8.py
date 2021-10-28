import pandas as pd


def get_requirements():
    print("Data Manipulation\n")
    print("Program Requirements:")
    print("1. Data Cleaning and Manipulation.")
    print("2. Import necessary libraries.")
    print("3. Reasearch how to install any missing packages.")
    print("4. Create at least three functions that are called by the program:")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. data_manipulation(): displays the following data.")
    print("5. Use imdb-movie-data.csv dataset.")
    print("6. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")

def data_manipulation():
    df = pd.read_csv("imdb-movie-data.csv")

    print("1.Print indexes:\n")
    df.index = pd.RangeIndex(start=0,stop=1000,step=1)
    print(df.index)

    print("2.Print columns:\n")
    print(df.columns)

    print("3.Print data frame:\n")
    print("Note: pandas displays max_rows number of rows (default, first, and last 5). Other rows are truncated. Value can be changed--research how! :")
    print(df)

    print("4.Print type:")
    print(type(df))

    print("5.Print attribute data types --object type represents strings")
    print(df.dtypes)

    print("6. Print values (truncated list), in array format:")
    print(df.values)

    print("7. Print first 5 records, in non-array format:")
    print(df.head(5))

    print("8. Print index of all DataFrame column names:")
    print(list(df))

    print("9. Print DataFrame info (i.e., summary, similar to 'describe tablename;' in MySQL")
    print(df.info(verbose=True))

    print("10. Print *only* number of DataFrame rows:")
    print(len(df))

    print("11. Print *only* number of DataFrame columns")
    print(len(df.columns))

    print("12. Print number of DataFrame rows and columns: ")
    print(df.shape)

    print("13. Print number of DataFrame elements (i.e. rows * columns")
    print(df.size)

    print("14. Series: one-dimensional labeled array, can hold disparate data types (e.g., integer, string, float, Boolean, Python objects, etc.):")
    ser = pd.Series([1,'Hello World', 3.5, True, 6, {"banana", "cherry", "apple"}])
    print(ser)

    print("15. DataFrame: multi-dimensional table, essentially, two Series.\n Note: Various ways to create DataFrame.\n Here, create dictionary (key:value pairs), ordered (since 3.7), mutable, and does not allow duplicate. \n Then, pass it to pandas DataFrame constructor (Note: indexes automatically provided.")
    dic = {'vegetables': [3,2,0,1,5,4,7,6],'fruits':[0,3,7,2,1,6,4,5]}
    df1 = pd.DataFrame(dic)
    print(df1)
    print('Then, add customer names as indexes:')
    index = ['Bob','Jane','Joe','Peter','Viola','Thomas','Raquel','Nicole']
    df1 = pd.DataFrame(dic, index = index)
    print(df1)
    
    print("16. Locate customer's order by name:")
    print(df1.loc['Jane',:])

    print("17. Convert DataFrame to following file types: .csv and .json (save to same directory):")
    df1.to_csv('produce_list.csv')
    df1.to_json('produce_list.json')
    
    print("18. Create DataFrame for imdb-movie-data.csv, designate movie ***titles*** as index, and print 1st five records:")
    df = pd.read_csv('imdb-movie-data.csv')
    df = df.set_index('Title')
    print(df.head())
    
    print("19. Display last three records:")
    print(df.tail(3))
    
    print("20. Handling duplicates using append(). (Note: twice as many rows.)")
    df = df.append(df)
    print(df.shape)
    
    print("21. Cleaning duplicates using drop_duplicates():")
    df = df.drop_duplicates()
    print(df.shape)
    
    print("22. Cleaning column names using rename(), and list comprehension. \n Original column names:")
    print(df.columns)

    print("\t22a. Remove parentheses using rename():")
    df = df.rename(columns = {'Revenue (Millions)':" Revenue_millions"})
    print(df.columns)
    
    print("\t22b. Make column names lower case, manually using list assignment")
    columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
    df.columns = columns
    print(df.columns)
    
    print("\t22c. Make column names lower case using list comprehension and lower():")
    df.columns = [i.lower() for i in df.columns]
    print(df.columns)
    
    print("23. Working with missing (null) values: 1) remove, or 2) replace (imputation).")
    
    print("\tStep 1: Identify null cells:")
    print(df.isna())
    
    print("\tStep2: Count number of nulls in each column:")
    print(df.isna().sum())
    
    print("\t23a. NB: Remove nulls, *only* with small amount of missing data (<5%): \n Note: dropna() removes rows w/at least one null value, \n and returns new DataFrame, w/o affecting original. \n axis=0 (rows default), axis = 1 columns \n Where does \'axis\' come from? Remember: df.shape returns rows(0)/cols(1).")
    print(df.dropna(axis=0))

    print("\t23b. Remove nulls (columns):")
    print(df.dropna(axis=1))

    print("\t23c. Imputation: Replace missing values with guessed/estimated value. \n Use data and relationships among non-missing predictors to estimate missing values.\n One (simple) way: Apply central tendency values (i.e., mean, median, mode).")
    print("\tStep 1: Extract column with null values into variable, and print 1st 5 records: \n Note: \"Title\" index remains.")
    print(df["revenue_millions"].head())
    
    print("\tStep 2: Return mean value:")
    print(df["revenue_millions"].mean())
    
    print("\tStep 3: Impute mean value using fillna() and inplace=True, then print nulls. \n Remember: inplace=True affects original DataFrame.")
    df["revenue_millions"].fillna(df["revenue_millions"].mean(),inplace=True)
    print(df.isna().sum())
   
    print("24. Basic statistical analyses using describe(), summary of *continuous* variables. \n Understanding data values (e.g., continuous vs. categorical) assists when determining plot types.")
    print(df.describe())
    
    print("25. Basic statistical analyses using describe(), summary of *categorical* variable (here, only *one* attribute). \n Returns row count, unique count of categories, top category, and freq of top categor(y/ies).")
    print(df['genre'].describe())

def main():
        get_requirements()
        data_manipulation()
        
main() 
    