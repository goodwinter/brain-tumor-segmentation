Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... 
... # 訓練結果數據
... epochs = [1, 5, 7, 10]
... accuracy = [0.4627, 0.9946, 1.0000, 0.9944]
... loss = [318.873, 0.0282, 0.0272, 9.172e-05]
... val_accuracy = [0.2984, 0.3147, 0.3263, 0.3590]
... val_loss = [2.0097, 9.1096, 9.6480, 9.6957]
... 
... # 創建圖表
... plt.figure(figsize=(10, 6))
... 
... # 準確率圖
... plt.subplot(1, 2, 1)
... plt.plot(epochs, accuracy, label='Training Accuracy', marker='o')
... plt.plot(epochs, val_accuracy, label='Validation Accuracy', marker='o')
... plt.title('Training and Validation Accuracy')
... plt.xlabel('Epochs')
... plt.ylabel('Accuracy')
... plt.legend()
... 
... # 損失圖
... plt.subplot(1, 2, 2)
... plt.plot(epochs, loss, label='Training Loss', marker='o')
... plt.plot(epochs, val_loss, label='Validation Loss', marker='o')
... plt.title('Training and Validation Loss')
... plt.xlabel('Epochs')
... plt.ylabel('Loss')
... plt.legend()
... 
... # 保存圖片
... plt.tight_layout()
... plt.savefig('training_results.png')
... plt.show()
