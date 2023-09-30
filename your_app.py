
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
import time 

import pickle  #to load a saved model
import base64  #to ope

import plotly.graph_objs as go  # Add this import statement
import plotly.offline as py  # Add this import statement




# Define a function to map values from a dictionary
def get_fvalue(val):
    feature_dict = {"No": 1, "Yes": 2}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

# Create a dictionary (you can replace this with your own data)
my_dict = {"Home": "This is the Home page.", "Prediction": "This is the Prediction page."}

# Sidebar to select the page
app_mode = st.sidebar.selectbox('Select Page', list(my_dict.keys()))

# Display content based on the selected page
if app_mode == "Home":
    st.markdown("Welcome to the Home page!")
    st.markdown("It consists of 10000 observations and 14 variables.")



elif app_mode == "Prediction":
    st.markdown("Welcome to the Prediction page!")
    st.markdown("Here you can perform predictions.")

    # Continue with content for the Prediction page

# You can add more pages and logic as needed




st.title ("Bank Customer Churn Project")
#st.header("this is the markdown")
st.markdown("It consists of 10000 observations and 14 variables. Independent variables contain information about customers. Dependent variable refers to customer abandonment status.")
st.markdown("Variables:")
st.markdown("1. **RowNumber** — corresponds to the record (row) number and has no effect on the output. This column will be removed.")
st.markdown("2. **CustomerId** — contains random values and has no effect on customer leaving the bank. This column will be removed.")
st.markdown("3. **Surname** — the surname of a customer has no impact on their decision to leave the bank. This column will be removed.")
st.markdown("4. **CreditScore** — can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.")
st.markdown("5. **Geography** — a customer’s location can affect their decision to leave the bank. We’ll keep this column.")
st.markdown("6. **Gender** — it’s interesting to explore whether gender plays a role in a customer leaving the bank. We’ll include this column, too.")
st.markdown("7. **Age** — this is certainly relevant, since older customers are less likely to leave their bank than younger ones.")
st.markdown("8. **Tenure** — refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.")
st.markdown("9. **Balance** — also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.")
st.markdown("10. **NumOfProducts** — refers to the number of products that a customer has purchased through the bank.")
st.markdown("11. **HasCrCard** — denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank. (0=No, 1=Yes)")
st.markdown("12. **IsActiveMember** — active customers are less likely to leave the bank, so we’ll keep this. (0=No, 1=Yes)")
st.markdown("13. **EstimatedSalary** — as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.")
st.markdown("14. **Exited** — whether or not the customer left the bank. This is what we have to predict. (0=No, 1=Yes)")


#st.subheader("this is the subheader")
#st.caption("this is the caption")
#st.code("x=2021")
#st.latex(r''' a+a r^1+a r^2+a r^3 ''')


# Load the data from the CSV file
df = pd.read_csv("E:/Academic/MSc Coventry University/Machine Learning/Assignment/Churn_pred.csv")

# Basic information about the dataset
#st.subheader("this is the subheader")
#st.write(f"Number of rows: {df.shape[0]}")
#st.write(f"Number of columns: {df.shape[1]}")
#st.write(f"Column names: {', '.join(df.columns)}")



# Show the first few rows of the dataset
st.subheader("Sample Data")
st.write(df.head())


st.subheader("Bank Customer Churn")

# Calculate the counts of churn and non-churn customers
churn_counts = df['Exited'].value_counts()
total_customers = len(df)






# Calculate the percentages
churn_percentage = (churn_counts[1] / total_customers) * 100
non_churn_percentage = (churn_counts[0] / total_customers) * 100

# Create a donut chart
fig = px.pie(names=['Churn', 'Non-Churn'],
             values=[churn_percentage, non_churn_percentage],
             title="Churn vs. Non-Churn Customers",
             hole=0.5,
             labels=['Churn', 'Non-Churn'],
             color_discrete_sequence=px.colors.qualitative.Plotly)

# Add text annotation in the center
fig.add_annotation(
    text=f"Total Customers: {total_customers}",
    x=0.5,
    y=0.5,
    showarrow=False,
    font=dict(size=20)
)

# Display the donut chart in Streamlit
st.plotly_chart(fig)



st.subheader("Bank Customer Churn vs Age")

# Calculate churn percentages
churn_percentage = df.groupby(['Gender', 'Exited']).size().unstack(fill_value=0).reset_index()
churn_percentage['Total'] = churn_percentage[0] + churn_percentage[1]
churn_percentage['Churn_Percentage'] = churn_percentage[1] / churn_percentage['Total']
churn_percentage['Non_Churn_Percentage'] = churn_percentage[0] / churn_percentage['Total']

# Create a stacked bar chart
fig_gender_churn_percentage = px.bar(churn_percentage, x='Gender', y=['Churn_Percentage', 'Non_Churn_Percentage'],
                                      #color_discrete_sequence=['#1f77b4', '#ff7f0e'],
                                      color_discrete_sequence=px.colors.qualitative.Plotly,
                                      labels={'Exited': 'Churn Status', 'value': 'Percentage'},
                                      title='Churn Percentage by Gender', text=['Churn_Percentage', 'Non_Churn_Percentage'])

fig_gender_churn_percentage.update_traces(texttemplate='%{text:.1%}', textposition='outside')

# Display the stacked bar chart in Streamlit
st.plotly_chart(fig_gender_churn_percentage)






# Create a histogram of customer ages
st.subheader("Age Distribution")
fig_age_hist = px.histogram(df, x='Age', nbins=20, title='Age Distribution', color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_age_hist)


#st.title("Bank Customer Churn Project")
st.header("Geography vs age") 
# Create a bar chart
fig = px.bar(df, y="Exited", x="Age", color="Geography")
# Display the bar chart in Streamlit
st.plotly_chart(fig)



# Create a box plot to visualize the distribution of credit scores
st.subheader("Credit Score Distribution")
fig_credit_box = px.box(df, y='CreditScore', title='Credit Score Distribution', color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_credit_box)



# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap using Plotly
#import plotly.express as px

fig = px.imshow(correlation_matrix,
                x=correlation_matrix.index,
                y=correlation_matrix.columns,
                color_continuous_scale='Viridis',
                title='Correlation Matrix Heatmap')

# Adjust the size of the heatmap
fig.update_layout(
    width=1000,  # Set the width
    height=600 ) # Set the height

# Display the heatmap in Streamlit
st.write(fig)


# Load the model from the pickle file
#with open('model.pkl', 'rb') as file:
 #   model = pickle.load(file)
    
    
 
 
st.subheader("Please enter data")
#st.checkbox('yes')
#st.button('Click')
st.date_input('Submited Date')
st.number_input('Age', min_value=18,max_value=100)
st.radio('Pick your Gender',['Male','Female'])  
st.selectbox('Pick your Country',['France','Spain', 'Germany'])
#st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick your Credit Score', 0,700)
st.number_input('Number of Products', 0,5)
st.text_input('Bank Balance Appoximately')
st.radio('Has a credit card', ['Yes','No'])   
st.text_area('EstimatedSalary')
#st.file_uploader('Upload a photo')
#st.color_picker('Choose your favorite color')





