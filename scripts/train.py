import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(data_dir):
    """
    加載數據並進行預處理
    """
    train_dir = f"{data_dir}/train"
    valid_dir = f"{data_dir}/valid"
    test_dir = f"{data_dir}/test"

    # 使用 Keras 的 ImageDataGenerator 進行數據增強
    train_datagen = ImageDataGenerator(rescale=1.0/255, horizontal_flip=True, rotation_range=30)
    valid_datagen = ImageDataGenerator(rescale=1.0/255)
    test_datagen = ImageDataGenerator(rescale=1.0/255)

    # 加載數據
    train_data = train_datagen.flow_from_directory(
        train_dir, target_size=(128, 128), batch_size=32, class_mode='categorical')
    valid_data = valid_datagen.flow_from_directory(
        valid_dir, target_size=(128, 128), batch_size=32, class_mode='categorical')
    test_data = test_datagen.flow_from_directory(
        test_dir, target_size=(128, 128), batch_size=32, class_mode='categorical')

    return train_data, valid_data, test_data

def build_model():
    """
    構建簡單的 CNN 模型
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')  # 假設有 3 個類別
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    """
    訓練模型
    """
    # 加載數據
    data_dir = "data"
    train_data, valid_data, test_data = load_data(data_dir)

    # 構建模型
    model = build_model()

    # 訓練模型
    model.fit(
        train_data,
        validation_data=valid_data,
        epochs=10  # 設置訓練輪數
    )

    # 評估模型
    test_loss, test_acc = model.evaluate(test_data)
    print(f"測試集準確率: {test_acc:.2f}")

if __name__ == "__main__":
    train_model()

