import cv2
import os

# Define the input folder containing your images
input_folder = r'C:\Users\jagad\OneDrive\Desktop\AccuFace-Logix\Images'

# Loop through the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Read the image
        img = cv2.imread(os.path.join(input_folder, filename))
        if img is not None:
            # Resize the image to 216x216 pixels
            resized_img = cv2.resize(img, (216, 216))
            # Save the resized image with the same name in the same folder
            output_path = os.path.join(input_folder, filename)
            cv2.imwrite(output_path, resized_img)

print("All images resized and saved in the same folder.")
