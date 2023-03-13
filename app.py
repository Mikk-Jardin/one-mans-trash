import streamlit as st
import PIL
import cv2
import numpy as np


from detector.build_model import build_model
from detector.class_names import CLASS_NAMES, CLASS_PRICES
from detector.visualize import display_instances


st.title("One Man's Trash")
st.header(":moneybag: Learn how much your trash could be worth.")


# File uploader for uploading images for detection
uploaded_image = st.file_uploader(label="Upload an image of your trash.")

# Initialize uploaded image in session state
if not uploaded_image:
   st.warning("Please upload image.")
   st.stop()
else:
   st.session_state.uploaded_image = uploaded_image
   detect_btn = st.button("Detect Trash")


if "detectbtn_state" not in st.session_state:
   st.session_state.detectbtn_state = False


# Did user press button
if detect_btn or st.session_state.detectbtn_state:
   st.session_state.detectbtn_state = True


if st.session_state.detectbtn_state:
    # Initialize display message instance
    disp_message = st.empty()

    # Load detection model
    disp_message.write(":open_file_folder: Loading detection model...")
    model = build_model()

    # Prepare image 
    image = np.array(PIL.Image.open(st.session_state.uploaded_image))
    image_prep = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    # Call model and detect objects
    disp_message.write(":mag_right: Detecting trash objects...")
    st.session_state.detected_objs = model.detect([image_prep], verbose=0)
    st.session_state.detected_objs = st.session_state.detected_objs[0]
    disp_message.empty()


    # Compute for price
    st.session_state.worth = []
    for obj in st.session_state.detected_objs['class_ids']:
        st.session_state.worth.append(CLASS_PRICES[CLASS_NAMES[obj]])
    
    # Sum up price
    st.session_state.worth = sum(st.session_state.worth)

    # Display worth of detected objects
    st.write(f"Your trash may be worth Php {'%.2f' % st.session_state.worth}. :money_mouth_face:")

    # Display detected objects in image
    disp_message.write(":frame_with_picture: Preparing detected image...")
    st.pyplot(display_instances(image=image,
                        boxes=st.session_state.detected_objs['rois'],
                        masks=st.session_state.detected_objs['masks'],
                        class_ids=st.session_state.detected_objs['class_ids'],
                        class_names=CLASS_NAMES))
    disp_message.empty()




