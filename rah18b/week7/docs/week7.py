import os
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

df = pd.read_csv("pima-indians-diabetes.csv")

def get_requirements():
    print("Deep Learning\n")
    print("Program Requirements:")
    print("1. Build deep-learning model to detect diabetes possibility.")
    print("2. Import necessary libraries.")
    print("3. Reasearch how to install any missing packages.")
    print("4. Create at least three functions that are called by the program:")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. deep_learning(): displays the following data.")
    print("5. Create neural network model.")
    print("\ta. Define neural network.")
    print("\tb. Compile model.")
    print("\tc. Train model with data.")
    print("\td. Evaluate model.")
    print("\te. Make predictions.")
    print("6. Use pima-indians-diabetes.csv dataset.")
    print("7. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")
    print("8. Provide pithy answers to the following questions:")
    print("\ta. What are deep learning and neural network models?")
    print("\tb. Advantages")
    print("\tc. Disadvantages")
    print("\td. What are hidden layers?")

def deep_learning():

    print("1.Print indexes:\n")
    df.index = pd.RangeIndex(start=0,stop=767,step=1)
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

    print("\n14. Split into input (x) and output (y) variables: Indicate how x/y variables are split.")
    x = df.iloc[:, 0:8]
    y = df.iloc[:, 8]

    print("\n\ta. Display input (x) variables:")
    print(x)

    print("\n\tb. Display output (y) variable (class): diabetic (1), non-diabetic (0):")
    print(y)

    print("\n15. Define, compile, fit, and evaluate keras model on dataset:")
    model = Sequential()

    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='relu'))

    #compile keras model
    model.compile(loss='binary_crossentropy',
        optimizer='adam', metrics=['accuracy'])

    #evaluate keras model in Jupyter notebook (turn off progress bars, verbose=0, to avoid notebook errors)
    model.fit(x,y, epochs=150, batch_size=10, verbose=0)

    #evaluate keras model using training dataset using evaluate() function on model
    _, accuracy = model.evaluate(x, y, verbose=0)
    print('Accuracy: %.2f' % (accuracy * 100))

    #make class predictions with model
    predictions = model.predict_classes(x)

    # summarize first 10 cases:
    for i in range(1-10):
        print('%s => %d (expected %d' % (x[i].tolist(), predictions[i], y[i]))

def main():
    get_requirements()
    deep_learning()

main()


    