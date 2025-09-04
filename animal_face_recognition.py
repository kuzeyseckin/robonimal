from imutils import paths
import face_recognition
import pickle
import cv2
import os

animals = ["dog", "cat"]

for animal in animals:
    dataset_path = os.path.join("dataset", animal)
    encodings_path = f"{animal}.pickle"
    
    print(f"[INFO] {animal} faces are being loaded...")
    
    if not os.path.exists(dataset_path):
        print(f"[ERROR] Dataset directory not found: {dataset_path}. Skipping.")
        continue
    
    imagePaths = list(paths.list_images(dataset_path))
    
    if not imagePaths:
        print(f"[INFO] No images found in {dataset_path}. Skipping.")
        continue

    knownEncodings = []
    knownNames = []

    for(i, imagePath) in enumerate(imagePaths):
        print(f"[INFO] Processing {animal} faces {i + 1}/{len(imagePaths)}")
        name = imagePath.split(os.path.sep)[-2]

        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_encodings(rgb, model="hog")

        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    print(f"[INFO] Serializing encodings for {animal}...")
    data = {"encodings": knownEncodings, "names": knownNames}
    with open(encodings_path, "wb") as f:
        f.write(pickle.dumps(data))

print("[INFO] All facial encodings have been created. You can now run the main script.")
