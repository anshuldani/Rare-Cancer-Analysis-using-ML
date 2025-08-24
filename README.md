# 🧠 Diagnosis and Severity Scoring of Rare Brain Tumours using Deep Learning and AI-Generated Synthetic Data

This project presents a **complete deep learning pipeline** for diagnosing brain tumours and estimating severity levels from MRI images. It combines **classical image processing, unsupervised learning, CNNs, and GANs** to overcome the scarcity of annotated medical datasets, especially for rare cancers.

---

## 📌 Overview
Manual diagnosis of rare brain tumours is time-consuming and often limited by insufficient annotated datasets. Our system addresses this by:
- Detecting abnormalities using **PCA-based anomaly detection**
- Estimating tumor severity with **unsupervised clustering (KMeans)**
- Extracting critical MRI slices from **3D DICOM volumes**
- Localising tumours via **ResNet18 CNN**
- Generating synthetic tumour data with **DCGANs**

This hybrid framework enables **automated, interpretable, and scalable diagnostic support** in clinical environments.

---

## ✨ Features
- **Anomaly Detection (PCA + Cosine Similarity):** Differentiates normal vs abnormal brains.
- **Unsupervised Clustering (KMeans):** Groups tumor severity into *mild*, *moderate*, and *severe*.
- **Critical Slice Extraction:** Identifies the most informative axial slice from DICOM scans.
- **Tumor Localization (ResNet18):** Weakly supervised heatmaps highlight tumor regions.
- **Synthetic Data Generation (DCGAN):** Produces realistic tumour slices to address class imbalance.

---

## 🛠️ Datasets
- **[Kaggle Brain Tumour Classification Dataset](https://www.kaggle.com/datasets/rishiksaisanthosh/brain-tumour-classification)** – 22,500+ labelled MRI images (glioma, meningioma, pituitary tumour, no tumour).  
- **[UPENN-GBM Dataset (TCIA)](https://www.cancerimagingarchive.net/collection/upenn-gbm/)** – Volumetric DICOM scans from glioblastoma patients.  

---

## ⚙️ Preprocessing
- Grayscale conversion & histogram equalisation for consistency.  
- Gaussian blurring for noise reduction.  
- Otsu + adaptive thresholding for ROI mask generation.  
- Resized inputs to **256×256** pixels.  

---

## 🔬 Methodology

### 🔹 1. Anomaly Detection (PCA)
- Trained PCA on *no tumor* images.  
- Used cosine similarity > 0.90 to classify as normal.  
- Achieved **>95% accuracy** in filtering healthy brains.

### 🔹 2. Severity Scoring (KMeans)
- Tumour contour areas clustered into 3 groups.  
- Severity categories:  
  - **Mild** (<5 mm²)  
  - **Moderate** (5–10 mm²)  
  - **Severe** (≥10 mm²)  

### 🔹 3. Critical Slice Extraction
- For DICOM scans, the slice with the **largest tumour region** is selected.  
- Stored as **16-bit PNG** for high fidelity.  

### 🔹 4. Tumour Localisation (ResNet18)
- CNN trained on pseudo-labelled slices.  
- Achieved **87% accuracy** in tumor region identification.  
- Generated **heatmaps** for visual interpretability.  

### 🔹 5. Synthetic Data (DCGAN)
- Generator: 5 upsampling convolutional layers.  
- Discriminator: 5 convolutional layers + batch norm.  
- Evaluation metrics:  
  - **SSIM:** 0.96  
  - **PSNR:** 39.1 dB  
  - **MSE:** 7.94  
- Generated high-quality synthetic tumour images for rare cases.  

---

## 📊 Results
- **PCA Anomaly Detection:** >95% accuracy in normal/tumour separation.  
- **Severity Scoring:** Meaningful cluster separation aligned with expert interpretation.  
- **ResNet18 CNN:** 87% classification accuracy on critical tumour slices.  
- **GANs:** Produced realistic tumour images, diversifying datasets while retaining clinical plausibility.  

### Example Outputs
- Contour-based severity classification (Mild, Moderate, Severe).  
- CNN heatmaps overlayed on MRI slices highlighting tumour regions.  
- GAN-generated tumour images showing diverse morphology.  

---

## 📈 Visualizations
- **Tumor severity clusters** (area-based).  
- **ResNet18 heatmaps** localizing tumor regions.  
- **Synthetic tumor images** generated via DCGAN.  

---

## 📝 Conclusion
This modular framework demonstrates that combining **unsupervised anomaly detection, clustering, CNN-based weak supervision, and GAN-based data augmentation** can effectively diagnose and classify rare brain tumours.  
The pipeline offers:
- Robust performance without extensive labelled data.  
- Interpretability through visual heatmaps & contour-based severity scoring.  
- Scalability for real-world clinical environments.  

**Future Work:**
- Extend to **3D CNNs** for volumetric tumor analysis.  
- Explore **conditional GANs** for class-specific tumor synthesis.  
- Collaborate with radiologists for clinical validation.  

---

## 📚 References
- Kaggle Brain Tumour Classification Dataset [1]  
- UPENN-GBM DICOM Dataset (TCIA) [2]  
- Goodfellow et al., *Generative Adversarial Nets*, NeurIPS 2014 [5]  
- Sandfort et al., *Data Augmentation using GANs in Medical Imaging*, IEEE TMI 2020 [8]  
- Full reference list available in the project report.  
