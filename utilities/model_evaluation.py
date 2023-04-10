import pandas as pd
from sklearn import metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def reg_eval(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred, squared=True)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    adj_r2 = 1 - (1-r2_score(y_test, y_pred)) * (len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)

    print('MAE:', mae)
    print('MSE:', mse)
    print('RMSE:', rmse)
    print('Adj_R2:', adj_r2)