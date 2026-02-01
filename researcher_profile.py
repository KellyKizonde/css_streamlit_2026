# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 15:17:11 2026

@author: User
"""

import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Researcher Profile", layout="wide")


name = "Mr. Kizonde Bihindi Kelly"
cellphone = "0810770400"
designation = "Lab assistant, Electronic engineering"
email = "kellykizonde78@gmail.com"


st.title(name)
st.subheader(designation)

st.header("📫 Contact Information")
st.markdown(f"""
- **Number:** {cellphone}  
- **Email:** [{email}](mailto:{email})  
""")

st.header("📖 Biography")
st.write(
    "I am a Laboratory Assistant and Master of Engineering candidate in the "
    "Department of Electrical Engineering at Vaal University of Technology. "
    "My research focuses on Non-Intrusive Load Monitoring (NILM), involving "
    "the application of signal processing and machine learning techniques "
    "to estimate individual appliance-level power consumption from "
    "aggregate electricity meter data."
)


st.header("🔬 Research Interests")
st.markdown("""
- Electrical and Electronic  
- Iot 
- Load Monitoring
- Smart system design 
- Machine Learning  
""")


st.header("📄Publications")
publications = [
    "-  B.K. Kizonde, TND Mathaba and HM Langa (2024),’ A Non-Intrusive Load Monitoring Technique For Real-Time Energy Management’ in proceedings of the 9th smart city applications, Tangier, Morocco, 02-04 Oct. 2024.",
    "-	B. K. Kizonde, T. N. D. Mathaba and H. M. Langa,' Design of an IoT-Based Energy Monitoring Node,' 2023 International Conference on Electrical, Computer and Energy Technologies (ICECET), Cape Town, South Africa, 2023, pp. 1-6."
]

for pub in publications:
    st.write("•", pub)
    
    
    



st.markdown("---")

st.write("© 2026 Researcher Profile App")

