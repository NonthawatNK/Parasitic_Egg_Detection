import streamlit  as st
from PIL import Image


from ultralytics import YOLO
model = YOLO('./best.pt')

st.header('Parasitic Egg Detection')

col1, col2 = st.columns(2)


with col1:
    uploaded_file = st.file_uploader("เลือกรูปภาพ", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, width= 250,caption=f'{uploaded_file.name[:-4]}')
        


with col2:
    # from ultralytics import YOLO
    import matplotlib.pyplot as plt
    st.markdown('### Prediction')
    if uploaded_file is not None:
        # model = YOLO('./best.pt')
        
        img2 = Image.open(uploaded_file).convert("RGB")
        pred = model.predict(source = img2,conf = 0.5)
        
        result  = pred[0]
        boxes = result.boxes
        names = result.names
        result_image = result.plot()


        if boxes is not None and boxes.cls.numel() > 0:
            for i in range(len(boxes.cls)):
                class_id = int(boxes.cls[i])
                conf = float(boxes.conf[i])
                label = names[class_id]
                st.image(result_image)
                st.markdown(f"- พบ: **{label}** (ความมั่นใจ: `{conf:.2%}`)")
        else:
            st.info("ไม่พบพยาธิในภาพนี้")
        