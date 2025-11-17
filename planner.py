import pickle
import pandas as pd
import streamlit as st

with open(r'study_planner_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Personalised Study Planner")
subject = st.selectbox('Subject', ['Math', 'Science', 'English', 'History', 'Programming'])
difficulty = st.slider('Difficulty', min_value = 1, max_value = 5, value = 3)
performance = st.slider('Performance Score', min_value = 1, max_value = 100, value = 40)
days = st.slider("Days Left", min_value = 1, max_value = 100, value = 15)
priority = st.selectbox('Priority Level', ['Low', 'Medium', 'High'])

input_df = pd.DataFrame({
    'Subject' : [subject],
    'Difficulty' : [difficulty],
    'Performance_Score' : [performance],
    'Days_Left' : [days],
    'Priority_Level' : [priority]
})

prediction = model.predict(input_df)

st.success(f'You are recommeded to study {prediction[0]:.2f} hours in a day')
