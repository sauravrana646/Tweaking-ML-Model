import pandas as pd
from sklearn.preprocessing import StandardScaler 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import keras.backend as kb
import os

#Function to add Dense Layers
def addDense(num):           
    model.add(Dense(units=num,input_shape=(13,),
                activation='relu',
                kernel_initializer="he_normal"))
    



# Read Dataset
dataset = pd.read_csv("wines.csv")

# To be Predicted is stored in y 
y = dataset["Class"]

# Removed Categorical data to avoid dummy trap
y_new = pd.get_dummies(y)

# Removed to be predicted data from input
X = dataset.drop('Class', axis =1 )  



# Scaling the data          
sc = StandardScaler()          # To get better accuracy we use scaling here
X = sc.fit_transform(X)


# Building model
model = Sequential()

# Adding layers
addDense(5)






# Adding output layer
model.add(Dense(units=3, activation='softmax'))

# Compliling the model
model.compile(optimizer= RMSprop(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])

# Training the model and fitting the data
TrainedModel = model.fit(X,y_new,epochs = 10)


kb.clear_session()

# Get Accuracy
accuracy = (TrainedModel.history['accuracy'][-1:][0])*100


with open('/root/task3/accuracy.txt' , 'w') as f:
    f.write(str(accuracy))
