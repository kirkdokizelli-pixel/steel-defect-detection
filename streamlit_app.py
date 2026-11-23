import streamlit as st
from ultralytics import YOLO
from PIL import Image

model = YOLO("best.pt")

st.title("Steel Surface Defect Detection")
st.write("Upload a steel surface image to detect defects.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)

    results = model.predict(image, conf=0.25)
    result_img = results[0].plot()

    st.image(result_img, caption="Detection result", use_container_width=True)

    for box in results[0].boxes:
        cls = results[0].names[int(box.cls)]
        conf = float(box.conf)
        st.write(f"**{cls}** — confidence: {conf*100:.1f}%")
