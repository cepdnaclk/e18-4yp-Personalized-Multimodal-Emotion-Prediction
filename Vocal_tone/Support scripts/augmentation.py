import os
import cv2
import albumentations as A
from albumentations.pytorch import ToTensorV2

# Define your augmentation pipeline
transform = A.Compose([
    A.RandomBrightnessContrast(p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.Blur(blur_limit=3, p=0.2),
    A.GaussNoise(p=0.2),
    A.ToGray(p=0.2),
    ToTensorV2()
])

mood = "Fear"

# Path to the folder containing input images
input_folder = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Image\Original\\" + mood

# Path to the folder where augmented images will be saved
output_folder = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Image\Augmented\\" + mood

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(input_folder, filename)
        print(str(image_path))
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        
        # Apply augmentation multiple times to create 5 augmented images
        for i in range(5):
            augmented = transform(image=image)
            augmented_image = augmented['image']
            
            # Convert augmented image from PyTorch tensor to numpy array
            augmented_image = augmented_image.permute(1, 2, 0).numpy()  # Channels-last to match OpenCV format
            
            # Convert augmented image to BGR format before saving
            augmented_image_bgr = cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR)
            
            
            # Save the augmented image
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_aug_{i+1}.jpg")
            cv2.imwrite(output_path, augmented_image_bgr)
            
            print(f"Saved {output_path}")

