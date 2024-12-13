from PIL import Image, ImageFilter
import numpy as np

def open_image(file_path):
    """Open an image from a file path."""
    return Image.open(file_path)

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return image.convert("L")

def apply_blur(image):
    """Apply a blur effect to an image."""
    return image.filter(ImageFilter.BLUR)

def apply_contour(image):
    """Apply a contour effect to an image."""
    return image.filter(ImageFilter.CONTOUR)

def save_image(image, save_path):
    """Save the processed image to a specified path."""
    image.save(save_path)

def main():
    # Path to the image file
    file_path = "path/to/your/image.jpg"  # Change this to your image path
    image = open_image(file_path)

    # Display original image
    image.show(title="Original Image")

    # Convert to grayscale
    gray_image = convert_to_grayscale(image)
    gray_image.show(title="image Grayscale")

    # Apply blur effect
    blurred_image = apply_blur(image)
    blurred_image.show(title="Images with Contour Effects")

    # Apply contour effect
    contour_image = apply_contour(image)
    contour_image.show(title="Images with Contour Effects")

    # Save processed images
    save_image(gray_image, "processed_image_gray.png")
    save_image(blurred_image, "processed_image_blur.png")
    save_image(contour_image, "processed_image_contour.png")

    print("The processed image has been saved.")

if __name__ == "__main__":
    main()