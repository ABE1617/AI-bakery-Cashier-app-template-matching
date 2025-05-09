# 🥐 Template Matching Bakery Cashier App - ABE

This Python project uses **OpenCV's template matching** to detect and count specific bakery items in a static image. Each recognized item adds its price to a total, and the final amount is printed as a virtual shopping cart. It's a lightweight alternative to object detection using deep learning.

---

## ✅ What This App Does

- Uses OpenCV's `matchTemplate()` method to find predefined bakery items in an image.
- Detects and counts occurrences of each item.
- Calculates and prints the total price.
- Draws bounding boxes and item labels on the original image for visual confirmation.

---

## 🍞 How It Works

- Grayscale input image (`Test4.jpg`) is compared against template images like `B1.jpg`, `B2.jpg`, etc.
- Matching is based on a defined similarity threshold (default: `0.6`).
- Matching areas are grouped using `cv.groupRectangles` to avoid duplicate detections.
- Each successful match updates a shopping cart dictionary with counts and prices.

---

## 📂 Template and Image Setup

Put all image files in the same directory:


---

## 💰 Price List

You can manually edit this section in the script:

```python
items = {
    'B1.jpg': 2.50,
    'B2.jpg': 1.80,
    'B3.jpg': 3.00,
    # Add more as needed
}
```
## 🛠️ Requirements
Install required libraries with:
```batch
pip install opencv-python matplotlib numpy

```
## ▶️ Run the Script
```batch
python detect_bakery.py
```
You’ll see output like:
```python
Shopping Cart:
B1.jpg: 2
B3.jpg: 1
Total Price: $8.00
```

## 📝 Notes
Templates must be cropped tightly and clearly represent the items.

Adjust the threshold value for better matching accuracy depending on your images:
```python
threshold = 0.6
```
This approach is not scale- or rotation-invariant — templates should match test image size.
