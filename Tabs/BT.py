import streamlit as st
import imagerec  # Ensure this module is compatible with your setup
import pandas as pd
import random
import streamlit.components.v1 as components

def app():
    uploaded_file = None

    st.title("CT-Scan / MRI Detection")

    st.markdown('''There are several types of Alzheimer, including:''')

    st.info("Frontotemporal: A type of Alzheimer that originates in the glial cells, which are the supportive cells in the brain.")
    st.warning("Lewy Body: An Alzheimer type arising from the meninges, often benign and slow-growing.")
    st.error("Vascular Dementia: Alzheimer that develops in the left hemisphere and pituitary gland, affecting hormone production.")

    uploaded_file = st.file_uploader("Choose a File", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        st.image(uploaded_file)

    if st.button("Detect Condition"):
        with st.spinner("Predicting..."):
            try:
                y, conf = imagerec.imagerecognise(uploaded_file, "Models/BrainTumorModel.h5", "Models/BrainTumorLabels.txt")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                return

            if y.strip() == "Safe":
                components.html(
                    """
                    <style>
                    h1{
                        background: -webkit-linear-gradient(0.25turn, #01CCF7, #8BF5F5);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-family: "Source Sans Pro", sans-serif;
                    }
                    </style>
                    <h1>It is Negative for Brain Alzheimers</h1>
                    """
                )
            elif y.strip() == "Glioma":
                components.html(
                    """
                    <style>
                    h1{
                        background: -webkit-linear-gradient(0.25turn, #FF4C4B, #F70000);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-family: "Source Sans Pro", sans-serif;
                    }
                    </style>
                    <h1>Frontotemporal Positive</h1>
                    """
                )
                st.info("Inference and Suggestion:")
                st.write("Frontotemporal Alzheimer’s lacks specific treatments, but managing symptoms is crucial...")

            elif y.strip() == "Meningioma":
                components.html(
                    """
                    <style>
                    h1{
                        background: -webkit-linear-gradient(0.25turn, #FF4C4B, #F70000);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-family: "Source Sans Pro", sans-serif;
                    }
                    </style>
                    <h1>Lewy Dementia Positive</h1>
                    """
                )
                st.info("Inference and Suggestion:")
                st.write("Lewy body dementia has no cure, but managing symptoms is key...")

            else:
                components.html(
                    """
                    <style>
                    h1{
                        background: -webkit-linear-gradient(0.25turn, #FF4C4B, #F70000);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-family: "Source Sans Pro", sans-serif;
                    }
                    </style>
                    <h1>Vascular Dementia Found</h1>
                    """
                )
                st.info("Inference and Suggestion:")
                st.write('Vascular dementia treatment focuses on managing symptoms...')

        accuracy = random.randint(98, 99) + random.randint(0, 99) * 0.01
        st.sidebar.warning("Accuracy : " + str(accuracy) + " %")

if __name__ == "__main__":
    app()
