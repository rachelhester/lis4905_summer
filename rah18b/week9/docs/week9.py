import matplotlib.pyplot as plt
import pandas as pd

def data_manipulation(): 
    df = pd.read_csv("imdb-movie-data.csv")

    print("26. Frequency of all values (value_counts()) in a column (here, 'genre'), returns 1st 10: ")
    df = pd.read_csv("imdb-movie-data.csv")
    print(df['Genre'].value_counts().head(10))

    print("27. Relationships between continuous variables using .corr() method: ")
    print("Pos. numbers: pos. correlation. Neg. numbers: inverse correlation. 1.0 indicates perfect correlation.")
    print("Correlation of interest: votes and revenue millions.")
    df = pd.read_csv("imdb-movie-data.csv")
    print(df.corr(method='pearson'))

    print("28. Condition selections.")
    print("28a. Display oldest and newest release years for movie in dataset: ")
    df = pd.read_csv("imdb-movie-data.csv")
    least_recent_date = df['Year'].min()
    most_recent_date = df['Year'].max()
    print("Oldest:", least_recent_date, "Newest:", most_recent_date)

    print("28b. Filter by one director, return 3 records:")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    options = ['Clint Eastwood']
    df = df.loc[df['Director'].isin(options)]
    print(df.head(3))

    print("28c. Filter by rating (>= 8.0), return 3 records")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    df = df.loc[(df['Rating'] >= 8.0)]
    print(df.head(3))
    
    print("28d. Filter by two directors (using 'or'). Logical operators | for or and & for and, return 1st 5 records")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    df = df.loc[(df['Director']=='Clint Eastwood') | (df['Director']=='James Gunn')]
    print(df.head(5))

    print("28e. Filter by same two directors (using 'isin'), return 1st 5 records")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    filter = df["Director"].isin(['Clint Eastwood','James Gunn'])
    print(df[filter].head(5))

    print("28f. Filter by all movies released between 2005 and 2010, inclusive, having rating above 8.5: ")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    df = df.loc[(df['Year'] >= 2005) & (df['Year'] <= 2010) & (df['Rating'] > 8.5)]
    print(df)

    print("28g. Filter by all movies released between 2005 and 2010, inclusive, having rating above 8.0, and made above or equal to 25th percentile in revenue: ")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    df = df.loc[(df['Year'] >= 2005) & (df['Year'] <= 2010) & (df['Rating'] > 8.0) & (df['Revenue (Millions)'] >= 25)]
    print(df)

    print("29. Create function, watch_rating(), returns yes or no based upon 8.5 or greater rating. Use Python's apply() function to pass rating attribute to function, and assign return values to new attribute watch_movie, display 1st 10 rows")
    df = pd.read_csv("imdb-movie-data.csv")
    pd.set_option('max_columns', None) 
    def watch_rating(Rating):
        if Rating >= 8.5:
            return "Yes"
        elif Rating < 8.5:
            return "No"
    df['Rating'] = df['Rating'].apply(watch_rating)
    print(df.head(10))

    print(("\n30. Plotting Recommendations: Categorical variables: bar charts and boxplots.\n")
         + "Continuous variables: Histograms, Scatterplots, Line graphs, and boxplots.\n"
         + "Create following plots: scatter, histogram, two boxplots. and one heatmap.\n"
         + "BE SURE to include your boxplot interpretations.\n")
    
    df.plot(kind='scatter',x='Rating',y='Revenue (Millions)')
    plt.show()
    df.plot(kind='hist', x='Rating', y='Runtime (Minutes)')
    plt.show()
    df = pd.read_csv('imdb-movie-data.csv')
    



def main():
    data_manipulation()

main() 
