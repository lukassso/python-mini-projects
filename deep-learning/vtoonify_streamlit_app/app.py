import sys
import os

# Add VToonify directory to PYTHONPATH so we can import 'model'
sys.path.append(os.path.abspath("VToonify"))

import streamlit as st
import torch
import numpy as np
from PIL import Image
from torchvision import transforms

from model.vtoonify_model import VToonify


# Load pretrained model
@st.cache_resource
def load_model():
    model = VToonify()
    checkpoint = torch.load("checkpoint/G.pth", map_location=torch.device("cpu"))
    model.load_state_dict(checkpoint["g_ema"])
    model.eval()
    return model

# Prepare uploaded image
def preprocess(image):
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)

# Postprocess output to display
def postprocess(tensor):
    image = tensor.squeeze().detach().numpy()
    image = np.transpose(image, (1, 2, 0))
    image = (image * 255).clip(0, 255).astype(np.uint8)
    return Image.fromarray(image)

# Streamlit UI
st.set_page_config(page_title="VToonify Streamlit")
st.title("🖼️ VToonify – Realistic Cartoon Stylization")

uploaded_file = st.file_uploader("Upload a face photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file).convert("RGB")
    st.image(input_image, caption="Original Image", use_column_width=True)

    if st.button("✨ Cartoonize"):
        with st.spinner("Processing..."):
            model = load_model()
            input_tensor = preprocess(input_image)
            with torch.no_grad():
                output_tensor = model(input_tensor)
            cartoon_image = postprocess(output_tensor)
        st.image(cartoon_image, caption="Cartoonized Output", use_column_width=True)
