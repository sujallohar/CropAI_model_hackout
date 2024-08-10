from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_data_generators(train_dir, validation_dir, test_dir, img_width=224, img_height=224, batch_size=32):
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    validation_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(img_width, img_height), batch_size=batch_size, class_mode='categorical')
    validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size=(img_width, img_height), batch_size=batch_size, class_mode='categorical')
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(img_width, img_height), batch_size=batch_size, class_mode='categorical')

    return train_generator, validation_generator, test_generator
