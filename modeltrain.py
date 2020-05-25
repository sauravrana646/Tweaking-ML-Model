import pandas as pd
from sklearn.preprocessing import StandardScaler 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import keras.backend as k

def addDense(num):
    model.add(Dense(units=num,input_shape=(13,),
                activation='relu',
                kernel_initializer="he_normal"))
    




dataset = pd.read_csv("wines.csv")


y = dataset["Class"]


y_new = pd.get_dummies(y)

X = dataset.drop('Class', axis =1 )  



# Scaling the data          
sc = StandardScaler()          # To get better accuracy we use scaling here
X = sc.fit_transform(X)



model = Sequential()

addDense(5)



model.add(Dense(units=3, activation='softmax'))


model.compile(optimizer= RMSprop(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])


TrainedModel = model.fit(X,y_new,epochs = 10)

k.clear_session()

accuracy = (TrainedModel.history['accuracy'][-1:][0])*100


print(accuracy)