# make sure first: pip install captcha

from captcha.image import ImageCaptcha
import numpy as np
from PIL import Image
import random
import sys

# The list of letters we used for creating CAPTCHA
letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Set the length of CAPTCHA is 4.
# Generate the text for a CAPTCHA
def random_captcha_text(char_set, captcha_size=4):
    captcha_text = []  # The list of CAPTCHA letters
    for i in range(captcha_size):
        letter = random.choice(char_set)
        captcha_text.append(letter)
    return captcha_text


# Generate the CAPTCHA image
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    # Get a random CAPTCHA text
    captcha_text = random_captcha_text(char_set=letters)
    # Convert the CAPTCHA text from list to string
    captcha_text = ''.join(captcha_text)
    # Generate the CAPTCHA image
    captcha = image.generate(captcha_text)
    # Write the image
    image.write(captcha_text, 'images/' + captcha_text + '.jpg')


# The image numbers to generate.
# WARNING: the name of image is the text of CAPTCHA image, might be repeat.
# Make sure this number not too large (below 2000).
num = 500

if __name__ == '__main__':

    for i in range(num):
        gen_captcha_text_and_image()
        sys.stdout.write('\r>> Creating image %d/%d ' % (i + 1, num))
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()
    print("Generate Complete!")