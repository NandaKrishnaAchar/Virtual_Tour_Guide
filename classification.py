# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:33:51 2020

@author: Nanda Krishna K S
"""


from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 3, activation = 'softmax'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         samples_per_epoch = 4413,
                         nb_epoch = 20,
                         validation_data = test_set,
                         nb_val_samples = 1119)


#Predicting
from keras.preprocessing import image
import numpy as np

img = image.load_img('test0.jpg', target_size=(64,64))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
classes = classifier.predict_classes(x, batch_size=10)
print(classes)



#Saving Model
from keras.models import load_model
classifier.save('my_model.h5')


clf = load_model('my_model.h5')

img = image.load_img('test0.jpg', target_size=(64,64))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
classes = clf.predict_classes(x, batch_size=10)
print(classes)
