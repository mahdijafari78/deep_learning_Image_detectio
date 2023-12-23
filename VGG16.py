import time

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import os
import numpy as np
import matplotlib.pyplot as plt

image_folder_path = "image"

image_names = os.listdir(image_folder_path)
model = VGG16(weights='imagenet', input_shape=(224, 224, 3))

for image_name in image_names:
    img = image.load_img(f'{image_folder_path}/{image_name}', target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions)[0]
    # print(f"name_image: {image_name}")
    plt.imshow(img)
    plt.title(f"name_image: {image_name} || predictions:{decoded_predictions[0][1]} ")
    plt.savefig(f'out_put_img/{image_name}')
