import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

def get_requirements():
    print("\nArtifical Intelligence2")
    print("\nProgram Requirements:")
    print("1. Build machine learning model")
    print("2. Predict if it will rain tomorrow (yes/no) by analyzing past data")
    print("3. Import necessary libraries")
    print("4. Research how to install any missing packages, if necessary.")
    print("5. Create at least 3 functions called by the program.")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. artificial_intelligence_2(): displays the following data.")
    print("6. Data set url (do *not* use downloaded file): https://rattle.togaware.com/weatherAUS.csv")
    print("7. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")
    print("8. Algorithms used (identify each): Logistic Regression, Random Forest, Decision Tree. Support Vector Machine:")
    print("\ta. Advantages")
    print("\tb. Disadvantages")
    print("\tc. How did each compare?")
    print("***DataFrame composed of three components: index, columns, and data. Data also known as values.***")

def artificial_intelligence2():
    #reading csv
    df = pd.read_csv("https://rattle.togaware.com/weatherAUS.csv")

    print("1.Print indexes:\n")
    df.index = pd.RangeIndex(start=0,stop=192918,step=1)
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

    print("\n14. Find null values (based upon number of records returned): ")
    print(df.count().sort_values())

    print("\n15. Cleaning Data--drop following attribures (notes in comments):\n"
	+ "Sunshine, Evaporation, Cloud3pm, Cloud9am (contain less than 60 percent data)\n"
	+ "Also, no need for Location, Date, or RISK_MM (not considering amount of rain)")

    df = df.drop(columns=['Sunshine', 'Evaporation', 'Cloud3pm', 'Cloud9am', 'Location', 'Date', 'RISK_MM'], axis=1)

    print("\n16. Print *new* number of DataFrame rows and columns (predictor variables): ")
    print(df.shape)

    print("\n17. Remove null values in df--then, print number of DataFrame rows and columns:")
    df = df.dropna(how='any')
    print(df.shape)

    print("\n18. Remove outliers--using Z-score (research: \"What is Z-score?\"):")

    z = np.abs(stats.zscore(df.select_dtypes(include=np.number)))
    df = df[(z < 3).all(axis=1)]

    print("\n19. Print *new* number of DataFrame rows and columns:")
    print(df.shape)

    print("\n20. Modify categorical columns (yes=1, no=0):")
    print("Before modification:")
    print(df['RainToday'])

    df['RainToday'].replace({'No':0, 'Yes':1}, inplace=True)
    df['RainTomorrow'].replace({'No':0, 'Yes':1}, inplace=True)
    print("After modification:")
    print(df['RainToday'])

    print("\n21. Print unique categorical column values (for each column):")
    categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
    for col in categorical_columns:
        print(np.unique(df[col]))   

    print("\n22. Convert categorical column (character) values into dummy/indicator (integer) values:")
    df = pd.get_dummies(df, columns=categorical_columns)
    print("Before normalizing data:")
    print(df.iloc[4:9])

    print("\n23. Normalize input variables to eliminate biases (differences in values used for each category.)")
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(df)
    df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
    print("After normalizing data:")
    print(df.iloc[4:9])

    print("\n24. Exploratory data analysis--identify most significant variables that will help predict ...")
    x = df.loc[:, df.columns != 'RainTomorrow']
    y = df[['RainTomorrow']]
    selector = SelectKBest(chi2, k=3)
    selector.fit(x, y)
    x_new = selector.transform(x)

    print(x.columns[selector.get_support(indices=True)])

    df = df[['Humidity3pm', 'Rainfall', 'RainToday', 'RainTomorrow']]
    x = df[['Humidity3pm']]
    y = df[['RainTomorrow']]

    print("\n25. Begin data modelng--comparing algorithims")
    print("Logistic Regression:")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    clf_logreg = LogisticRegression(random_state=0)

    clf_logreg.fit(x_train, y_train.values.ravel())

    y_pred = clf_logreg.predict(x_test)
    score = accuracy_score(y_test, y_pred)

    print("Accuracy using Random Forest Classifier (percentage): ", score)
    print("Time taken using Random Forest Classifier (seconds): ", time.time() - t0)

    print("\nDecision Tree:")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    clf_dt = DecisionTreeClassifier(random_state=0)
    clf_dt.fit(x_train, y_train.values.ravel())
    y_pred = clf_dt.predict(x_test)
    score = accuracy_score(y_test, y_pred)
    print("Accuracy using Decision Tree Classifier (percentage): ", score)
    print("Time taken using Decision Tree Classifier (seconds): ", time.time() - t0)


    print("\nSupport Vector Machine")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    clf_svc = svm.SVC(kernel='linear')
    clf_svc.fit(x_train, y_train.values.ravel())\

    y_pred = clf_svc.predict(x_test)
    score = accuracy_score(y_test, y_pred)
    print("Accuracy using Support Vector Machine Classifier (percentage): ", score)
    print("Time taken using Support Vector Machine Classifier (seconds): ", time.time() - t0)

    

def main():
    get_requirements()
    artificial_intelligence2()

main()
