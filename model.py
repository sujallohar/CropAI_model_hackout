from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

def build_model(input_shape=(224, 224, 3), num_classes=11):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    x = base_model.output
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(num_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=x)
    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

def train_model(model, train_generator, validation_generator, epochs=10):
    checkpoint = ModelCheckpoint('/Users/sujalpanchal/Desktop/hackathon/models/best_model.h5', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
    early_stopping = EarlyStopping(monitor='val_accuracy', patience=5, min_delta=0.001)
    
    history = model.fit(train_generator, epochs=epochs, validation_data=validation_generator, callbacks=[checkpoint, early_stopping], verbose=2)
    
    model.save('/Users/sujalpanchal/Desktop/hackathon/models/final_model.h5')
    return history
