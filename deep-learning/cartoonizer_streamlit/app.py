import cv2
import numpy as np
import streamlit as st
from PIL import Image

def stylized_painting_image(img: np.ndarray) -> np.ndarray:
    # Smooth detail without blurring edges
    smoothed = cv2.edgePreservingFilter(img, flags=1, sigma_s=64, sigma_r=0.4)

    # Increase color depth and warmth
    lab = cv2.cvtColor(smoothed, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    enhanced = cv2.merge((l, a, b))
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

    # Subtle oil painting feel
    oil_paint = cv2.xphoto.oilPainting(enhanced, size=7, dynRatio=1)

    return oil_paint

# --- Streamlit App UI ---

st.set_page_config(page_title="Enhanced Cartoonizer")
st.title("🎨 Enhanced Cartoonizer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = np.array(Image.open(uploaded_file).convert("RGB"))
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cartoon_bgr = stylized_painting_image(img_bgr)
    cartoon_rgb = cv2.cvtColor(cartoon_bgr, cv2.COLOR_BGR2RGB)

    st.image(cartoon_rgb, caption="🖼️ Cartoonized Output", use_column_width=True)

    # Save to disk
    cv2.imwrite("cartoon_output.png", cartoon_bgr)
    st.success("Image saved as cartoon_output.png 🎉")
