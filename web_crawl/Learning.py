import numpy as np
x1 = np.array([range(100), range(311, 411), range(100)])
x2 = np.array([range(501, 601), range(711,811), range(100)])

y1 = np.array([range(100, 200), range(311,411), range(100,200)])

x1 = np.transpose(x1)
x2 = np.transpose(x2)
y1 = np.transpose(y1)

print(x1.shape) # (100, 3)
print(x2.shape) # (100, 3)
print(y1.shape) # (100, 3)

from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(
    x1, y1, random_state=66, train_size=0.6, shuffle=False
)
x1_val, x1_test, y1_val, y1_test = train_test_split(
    x1_test, y1_test, random_state=66, test_size=0.5, shuffle = False
)   

x2_train, x2_test = train_test_split(
    x2, random_state=66, train_size=0.6, shuffle=False
)
x2_val, x2_test = train_test_split(
    x2_test, random_state=66, test_size=0.5, shuffle = False
)

# 2.모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
# model = Sequential()

input1 = Input(shape=(6,1))
xx = Dense(5, activation='relu')(input1)
xx = Dense(4)(xx)
xx = Dense(3)(xx)
xx = Dense(3)(xx)
middle1 = Dense(3)(xx)

input2 = Input(shape=(6,1))
xx = Dense(4, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(5)(xx)
middle2 = Dense(6)(xx)

input3 = Input(shape=(6,1))
xx = Dense(4, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(5)(xx)
middle3 = Dense(6)(xx)

input4 = Input(shape=(6,1))
xx = Dense(4, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(5)(xx)
middle4 = Dense(6)(xx)

input5 = Input(shape=(6,1))
xx = Dense(4, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(5)(xx)
middle5 = Dense(6)(xx)

input6 = Input(shape=(6,1))
xx = Dense(4, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(5)(xx)
middle6 = Dense(6)(xx)
# concatenate  사슬처럼 엮다.
from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2, middle3, middle4, middle5, middle6])

output1 = Dense(10)(merge1)
output1 = Dense(9)(output1)
output1 = Dense(1)(output1)

model = Model(inputs = [input1, input2, input3, input4, input5, input6], outputs = output1)
model.summary()

# 3.훈련
# model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.compile(loss='mse', optimizer='adam', metrics=['mse'])
# model.fit(x_train, y_train, epochs=100, batch_size=1)
model.fit([x1_train,x2_train],y1_train, epochs=100, batch_size=1, validation_data=([x1_val, x2_val],y1_val))

# 4.평가예측
mse = model.evaluate([x1_test, x2_test], y1_test, batch_size=1)
print("mse : ", mse)
# print("loss : ", loss)

y1_predict = model.predict([x1_test, x2_test])
print(y1_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
RMSE1 = RMSE(y1_test, y1_predict)
print("RMSE_y1 : ", RMSE1)


# R2 구하기
from sklearn.metrics import r2_score
r2_y1_predict = r2_score(y1_test, y1_predict)
print("R2_y1 : ",r2_y1_predict)
