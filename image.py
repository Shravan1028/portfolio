import streamlit as st  


import streamlit as st
from PIL import Image, ImageDraw

def image():

    # img = Image.open("Shravan.jpg").convert("RGBA")
    # # Create an oval mask
    # mask = Image.new("L", img.size, 0)
    # draw = ImageDraw.Draw(mask)
    # draw.ellipse((0, 0, img.width, img.height), fill=255)

    # # Apply the mask to the image
    # oval_cropped = Image.new("RGBA", img.size, (0, 0, 0, 0))
    # oval_cropped.paste(img, mask=mask)

    # Open the image using PIL
    img = Image.open("Shravan.jpg").convert("RGBA")

    # Create a circular mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.width, img.height), fill=256)

    # Apply the mask to the image
    circular_cropped = Image.new("RGBA", img.size, (0, 0, 0, 0))
    circular_cropped.paste(img, mask=mask)



    st.image([circular_cropped])
