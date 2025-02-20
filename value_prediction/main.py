from sklearn.metrics import r2_score, mean_absolute_error

from model import Prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value, plot: bool = False) -> Prediction:
    if len(inputs) != len(outputs):
        raise Exception('inputs and outputs must have same length')

    # Create a data frame
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the data using Numpy(X: inputs, y: outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    y = np.array(df['outputs']).reshape(-1, 1)

    # Split the data into training data to test our model
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.2)

    # Initialize the data and test it
    model = LinearRegression()
    model.fit(train_X, train_y)

    # Predict
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # test for accuracy
    y_test_prediction = model.predict(test_X)

    # Plot
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)

    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y, y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y, y_test_prediction))


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('inputs')
    plt.ylabel('outputs')
    plt.plot(inputs, y_line, color='r')
    plt.show()


if __name__ == '__main__':
    years: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    earnings: list[int] = [100, 80, 200, 250, 280, 300, 450, 480, 500, 590 , 670, 760]
    my_input: int = 20

    prediction: Prediction = make_prediction(inputs=years, outputs=earnings, input_value=my_input, plot=False)
    print('Input', my_input)
    print('Prediction', prediction)
    print('Mean', prediction.mean_absolute_error)
