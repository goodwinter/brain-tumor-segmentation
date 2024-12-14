# Brain Tumor Segmentation

This project aims to classify and segment brain tumor images using deep learning. 
It is implemented with TensorFlow and trained on a custom brain tumor dataset.


## Training Results

The model was trained for 10 epochs on the brain tumor dataset. Below are the results:

| Epoch | Accuracy | Loss    | Validation Accuracy | Validation Loss |
|-------|----------|---------|---------------------|-----------------|
| 1     | 0.4627   | 318.873 | 0.2984              | 2.0097          |
| 5     | 0.9946   | 0.0282  | 0.3147              | 9.1096          |
| 7     | 1.0000   | 0.0272  | 0.3263              | 9.6480          |
| 10    | 0.9944   | 9.172e-05 | 0.3590            | 9.6957          |

### Observations:
- The training accuracy reached 100% by epoch 7, but the validation accuracy remained low (~36%), indicating potential overfitting.
- Further tuning of the model or regularization techniques may be required to improve validation performance.

## 3.Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/goodwinter/brain-tumor-segmentation.git
   cd brain-tumor-segmentation
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Download and extract the dataset:
   ```bash
   python scripts/download.py


---

### 4. **Training the Model**
Steps to train the model, including commands to execute:

```markdown
## Training

To train the model, run:
```bash
python scripts/train.py







