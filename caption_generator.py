import os

# Define the folder with your duvet cover images
image_folder = './'  # <- Change this to your image folder

# Define your shared description
shared_description = "a duvet cover, easy, good, cool, cheap, cozy"

# File extensions considered as images
valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']

# Loop through images in the folder
for filename in os.listdir(image_folder):
    if any(filename.lower().endswith(ext) for ext in valid_extensions):
        image_path = os.path.join(image_folder, filename)
        txt_path = os.path.splitext(image_path)[0] + '.txt'

        with open(txt_path, 'w') as f:
            f.write(shared_description)

        print(f"Created label for: {filename}")

print("✅ All duvet cover labels generated!")
