# MRI-Deep-Analysis

![home](images/home.png)


Detecting tumor severity using machine learning (ML) and deep learning (DL) techniques in MRI scans has become an increasingly promising area in medical research. Here’s a high-level overview of the process:

**Data Collection and Preprocessing:**
- Gathering a dataset of MRI images with labeled tumor severity levels.
- Preprocessing involves normalization, resizing, and noise reduction to standardize the images and enhance their quality.

**Feature Extraction:**
- Extracting meaningful features from the MRI images.
- For instance, in DL, this could involve using convolutional neural networks (CNNs) to automatically learn relevant features.

**Model Development:**
- Utilizing ML/DL models to classify tumor severity levels based on the extracted features.
- ML algorithms Random Forests is employed, along with DL models like CNNs-based ResNet-50 for detection tasks.
  
**Training and Validation:**
- Splitting the dataset into training, validation, and testing sets.
- Training the model on the training set and validating its performance on the validation set to fine-tune hyperparameters and avoid overfitting.
