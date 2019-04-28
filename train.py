frames_num=15
count = 0
joint_transfer=[]
for i in range(int(len(transfer_values)/frames_num)):
    inc = count+frames_num
    joint_transfer.append([transfer_values[count:inc],labels_train[count]])
    count =inc

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
chunk_size = 2048
n_chunks = 15
rnn_size = 512
model = Sequential()
model.add(LSTM(rnn_size, input_shape=(n_chunks, chunk_size)))
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(50))
model.add(Activation(sigmoid))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(loss='mean_squared_error', optimizer='adam',metrics=['accuracy'])

data =[]
target=[]
epoch = 1500
batchS = 100
for i in joint_transfer:
    data.append(i[0])
    target.append(np.array(i[1]))
model.fit(data, target, epochs=epoch, batch_size=batchS, verbose=1)
model.save("rnn.h5", overwrite=True)
