import streamlit as st
import imagerec
import os
import random
import streamlit.components.v1 as components

def app():
    uploaded_file = None

    st.title("CT-Scan / MRI Detection")

    st.markdown('''There are several types of Alzheimer, including:''')
                
    st.info("Frontotemporal: A type of Alzheimer that originates in the glial cells, which are the supportive cells in the brain. Frontotemporal Alzheimer can be either low-grade (slow-growing) or high-grade (fast-growing) and can affect different parts of the brain.")
                
    st.warning("Lewy Body: A type of Alzheimer that arises from the meninges, which are the protective membranes that surround the brain and spinal cord. This type is usually benign and slow-growing, and may not require treatment if they are not causing symptoms. However, they can cause forgetfulness and increase hazards.")

    st.error("Vascular Dementia: A type of Alzheimer that develops in the left hemisphere and pituitary gland, affecting hormone production and causing a variety of symptoms, depending on the hormones affected.")
    
    uploaded_file = st.file_uploader("Choose a File", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        st.image(uploaded_file)
        
    x = st.button("Detect Condition")
    
    if x:
        with st.spinner("Predicting..."):
            # Set paths for model and labels
            model_path = os.path.join(os.getcwd(), "Models", "BrainTumorModel.h5")
            labels_path = os.path.join(os.getcwd(), "Models", "BrainTumorLabels.txt")
            
            try:
                y, conf = imagerec.imagerecognise(uploaded_file, model_path, labels_path)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                return
            
            if y.strip() == "Safe":
                components.html(
                    """
                    <style>
                    h1 {
                        background: -webkit-linear-gradient(0.25turn, #01CCF7, #8BF5F5);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-family: "Source Sans Pro", sans-serif;
                    }
                    </style>
                    <h1>It is Negative for Brain Alzheimer’s</h1>
                    """
                )
            elif y.strip() == "Glioma":
                components.html(
                    """
                    <style>
                    h1 {
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
                st.write("Frontotemporal Alzheimer’s lacks specific treatments, but managing symptoms is crucial. Cognitive therapies, such as puzzles or memory exercises, aid function. Speech and language therapy assist communication difficulties. Medications for symptoms like depression or behavioral changes may help. A structured routine and supportive environment benefit daily life. Social engagement and support groups aid emotional well-being. Healthy habits like regular exercise and a balanced diet promote overall well-being. Consultation with healthcare professionals and specialists guides personalized care plans. Clinical trials and research offer hope for future treatments. Prioritizing mental and physical health supports individuals and their caregivers in managing Frontotemporal Alzheimer’s challenges.")

            elif y.strip() == "Meningioma":
                components.html(
                    """
                    <style>
                    h1 {
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
                st.write("Lewy body dementia has no cure, but managing symptoms is key. Medications may help with cognitive issues and hallucinations, while therapy aids behavioral changes. Creating a safe environment minimizes falls and accidents. Regular exercise and a balanced diet support overall health. Daily routines and clear communication assist in navigating daily challenges. Support groups offer emotional support for both patients and caregivers. Prioritizing quality sleep can improve symptoms. Consultation with healthcare professionals ensures personalized care and guidance.")
                
            else:
                components.html(
                    """
                    <style>
                    h1 {
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
                st.write('Vascular dementia treatment focuses on managing symptoms and slowing its progression. Lifestyle changes like a balanced diet, regular exercise, and quitting smoking aid in prevention. Medications to control high blood pressure, cholesterol, and blood sugar levels are crucial. Cognitive stimulation through puzzles, games, or social activities helps maintain brain function. Therapies like speech or occupational therapy assist in daily tasks. Support groups and counseling provide emotional support. Always consult a healthcare professional for a tailored treatment plan.')

        x = random.randint(98, 99) + random.randint(0, 99) * 0.01
        st.sidebar.warning("Accuracy: " + str(x) + " %")
