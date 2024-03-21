import pytesseract
from PIL import Image


img = Image.open('src/docs/080c869f-8e81-45d7-91ea-7b1c1b6a7025_dawn_theme_enhancement_p2.jpg')
text = pytesseract.image_to_string(img)
print(text)