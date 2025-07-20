import os
import pydicom
import numpy as np
import cv2
import imageio

def load_dicom_series(folder_path):
    dicom_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".dcm")]
    if not dicom_files:
        return None
    slices = []
    for f in dicom_files:
        try:
            ds = pydicom.dcmread(f)
            if hasattr(ds, "InstanceNumber"):
                slices.append((ds.InstanceNumber, ds.pixel_array))
        except Exception as e:
            print(f"Failed to read {f}: {e}")
    if not slices:
        return None
    slices.sort(key=lambda x: x[0])
    volume = np.stack([s[1] for s in slices])
    return volume

def find_largest_tumor_slice(volume):
    max_area = 0
    max_slice_idx = 0
    for i, slice in enumerate(volume):
        img = cv2.normalize(slice.astype(np.float32), None, 0, 255, cv2.NORM_MINMAX)
        img = img.astype(np.uint8)
        _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        total_area = sum(cv2.contourArea(cnt) for cnt in contours)
        if total_area > max_area:
            max_area = total_area
            max_slice_idx = i
    return max_slice_idx

def save_slice_as_image(slice_img, output_path):
    # Step 1: Resize first
    resized_img = cv2.resize(slice_img, (256, 256), interpolation=cv2.INTER_AREA)

    # Step 2: Normalize to full 16-bit range [0, 65535]
    norm_img = cv2.normalize(resized_img.astype(np.float32), None, 0, 65535, cv2.NORM_MINMAX)
    img_16bit = norm_img.astype(np.uint16)

    # Step 3: Save using imageio as 16-bit PNG
    imageio.imwrite(output_path, img_16bit)

def process_all_patients(root_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for root, dirs, files in os.walk(root_folder):
        if any(f.endswith(".dcm") for f in files):
            try:
                volume = load_dicom_series(root)
                if volume is None:
                    continue
                idx = find_largest_tumor_slice(volume)
                slice_img = volume[idx]
                patient_id = root.split("UPENN-GBM")[-1].replace("/", "_")
                filename = f"UPENN-GBM{patient_id}.png"
                save_slice_as_image(slice_img, os.path.join(output_folder, filename))
                print(f"✅ Saved: {filename}")
            except Exception as e:
                print(f"❌ Failed processing {root}: {e}")

if __name__ == "__main__":
    dicom_root = "/Users/baljeetsingh/Downloads/DICOM Database"  # Update to your root
    output_dir = "tumor_slices_16bit"

    print("📂 Processing all patient folders...")
    process_all_patients(dicom_root, output_dir)
    print("✅ Done!")
