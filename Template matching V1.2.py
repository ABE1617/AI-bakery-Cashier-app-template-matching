import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the input image
img = cv.imread('Test4.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Define the bakery items and their prices
items = {
    'B1.jpg': 2.50,
    'B2.jpg': 1.80,
    'B3.jpg': 3.00,
    # Add more items and prices as needed
}

# Threshold for template matching
threshold = 0.6

# Initialize the shopping cart and total price
shopping_cart = {}
total_price = 0.0

# Detect items and add them to the shopping cart
for item_name, template in items.items():
    template_img = cv.imread(item_name, cv.IMREAD_GRAYSCALE)
    assert template_img is not None, f"{item_name} could not be read, check with os.path.exists()"
    w, h = template_img.shape[::-1]

    res = cv.matchTemplate(img, template_img, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    rects = []
    for pt in zip(*loc[::-1]):
        rects.append([pt[0], pt[1], pt[0] + w, pt[1] + h])
    rects, weights = cv.groupRectangles(rects, groupThreshold=1, eps=0.5)
    for idx, (x1, y1, x2, y2) in enumerate(rects):
        if item_name not in shopping_cart:
            shopping_cart[item_name] = 0
        shopping_cart[item_name] += 1
        total_price += items[item_name]

        cv.rectangle(img, (x1, y1), (x2, y2), 255, 2)
        cv.putText(img, f"{item_name} - ${items[item_name]}", (x1, y1-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 2)

# Print the shopping cart and total price
print("Shopping Cart:")
for item_name, count in shopping_cart.items():
    print(f"{item_name}: {count}")
print(f"Total Price: ${total_price:.2f}")

# Display the result
plt.imshow(img, cmap='gray')
plt.title('Detected Bakery Items')
plt.axis('off')
plt.show()


