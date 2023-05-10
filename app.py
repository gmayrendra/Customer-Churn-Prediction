{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMCA0p9nZa6uE/7P6AAmBkY"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":12,"metadata":{"id":"3YGAMvpl_vJ3","executionInfo":{"status":"ok","timestamp":1680256160927,"user_tz":-420,"elapsed":490,"user":{"displayName":"Gege Mayrendra","userId":"04715041991527514304"}}},"outputs":[],"source":["import streamlit as st\n","import pandas as pd\n","import numpy as np\n","import pickle\n","import json\n","\n","# Load All Files\n","from tensorflow.keras.models import load_model\n","\n","with open('pipeline.pkl', 'rb') as file_1:\n","  model_pipeline = pickle.load(file_1)\n","\n","model_ann = load_model('seqimp_model.h5')\n","\n","\n","st.title('Customer Prediction')\n","membership_category= st.selectbox('Membership_category', (1,2,3,4,5,6), index=1, help='1. No Membership, 2. Basic Membership, 3.Silver Membership, 4. Gold Membership, 5. Premium Membership, 6. Platinum Membership .')\n","st.write('membership category:', membership_category)\n","avg_frequency_login_days = st.slider('Average frequency login days', 0, 100)\n","st.write(avg_frequency_login_days, '%')\n","feedback= st.selectbox('Feedback', ('Poor Product Quality','No reason specified','Too many ads','Poor Website','Poor Customer Service','Reasonable Price','User Friendly Website','Products always in Stock','Quality Customer Care'), index=1, help='Feedback provided by a customer.')\n","st.write('feedback:', feedback)\n","\n","data_inf = pd.DataFrame({\n","    'membership_category': [membership_category],\n","    'avg_frequency_login_days': [avg_frequency_login_days],\n","    'feedback': [feedback]\n","})\n","data_inf\n","\n","if st.button('Predict'):\n","    final_result_forest = model_pipeline.predict (data_inf)\n","    st.write('Prediction: ')\n","    if final_result_forest == 1:\n","        st.subheader ('Churn')\n","else:\n","        st.subheader('Not Churn')\n"]},{"cell_type":"code","source":[],"metadata":{"id":"PtRydMS2_zZK"},"execution_count":null,"outputs":[]}]}