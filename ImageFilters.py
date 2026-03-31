# Lab 9 – Image Processing
# Name: Nidhi Agarwal
# Date: 03/31/2026
# Assignment: Change color

from PIL import Image

def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size

    # TODO: Loop through every pixel and swap green and blue values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]   # get RGB values

            # Swap green and blue
            pixels[x, y] = (r, b, g)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    # TODO: Loop through every pixel and reduce RGB values by amount
    # Make sure values do not go below 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]

            # Reduce brightness safely
            r = max(0, r - amount)
            g = max(0, g - amount)
            b = max(0, b - amount)

            pixels[x, y] = (r, g, b)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    bwFilter(myImg)

    # Uncomment each function as you complete it
    swapGreenBlue(myImg)
    darken(myImg, 20)


if __name__ == "__main__":
    main()
