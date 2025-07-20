# Rare-Cancer-Analysis-using-ML
Diagnosis and Severity Scoring of Rare Brain Tumor using Deep Learning and AI-Generated Synthetic Data

Diagnosis of Rare Cancer with AI-Generated Images
What the Project Does:
This repository includes tools and notebooks to:
Extract the largest tumour slice from 3D brain MRI DICOM volumes (extract_all_max_tumor_slices_16bit.py)
Perform tumour localization and severity classification using deep learning and clustering (ml-project.ipynb, fork-of-cancer-proj.ipynb)
Generate synthetic brain MRI images using a GAN model (GANs.ipynb)

Why the Project Is Useful:
Automatically selects the most diagnostically relevant MRI slice per patient
Enables automated tumour severity scoring for research or AI training
Supports medical image augmentation via GANs, especially useful for rare tumour cases
Speeds up preprocessing in medical imaging pipelines for academic and clinical AI work

How to Get Started
Clone the Repository & Navigate git clone <repo_url>
cd <repo_folder>
Install Required Dependencies You can install everything using pip
	
Run the Script to Extract Tumor Slices Edit paths in extract_all_max_tumor_slices_16bit.py
output_dir = "tumor_slices_16bit" 
Open and Run Notebooks Launch: jupyter notebook
Then run:
ml-project.ipynb – Classification Pipeline
fork-of-cancer-proj.ipynb – Preprocessing and clustering variations
GANs.ipynb – Generative image synthesis of tumour slices

Dependencies:
Make sure you have Python 3.7+ installed. Required packages:
numpy
pandas
matplotlib
opencv-python
imageio
pydicom
scikit-learn
tensorflow
keras
seaborn
jupyterlab

Install with:
pip install numpy pandas matplotlib opencv-python imageio pydicom scikit-learn tensorflow keras seaborn jupyterlab

Author:
Anshul Dani
