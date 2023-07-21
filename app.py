import streamlit as st
import numpy as np
import pickle
# Function to convert 'Yes' and 'No' options to 1 and 0 respectively
def yes_no_to_binary(val):
    return 1 if val == 'Yes' else 0

def predict_loan_approval(user_inputs_array):
    loaded_model = pickle.load(open('loan prediction model', 'rb'))
    predictions = loaded_model.predict(user_inputs_array)
    return predictions

def main():
    # Set the title of the app
    st.title("Loan Prediction App")

    # Initialize empty list to store user inputs
    user_inputs = []

    gender_options = {
        "Female": 0,
        "Male": 1
    }

    # Dropdown for gender selection
    selected_gender = st.selectbox("Select Gender", list(gender_options.keys()))

    # Get the corresponding value based on the selected label
    gender_value = gender_options[selected_gender]
    user_inputs.append( gender_value)

    dependency_options = {
        "1": 1,
        "2": 2,
        "3 or more": 3
    }

    # Dropdown for family size selection
    selected_dependency = st.selectbox("Select dependeny", list(dependency_options.keys()))
    
    # Get the corresponding value based on the selected label
    dependency_value =dependency_options[selected_dependency]
    user_inputs.append( dependency_value)
    # Dropdowns for binary options (Yes or No)
    
    questions_binary = ["Select Marital status", "select employedment status", "Property_Area"]
    for question in questions_binary:
        user_input = st.selectbox(f"{question} (Select Yes or No)", ("Yes", "No"))
        binary_input = yes_no_to_binary(user_input)
        user_inputs.append(binary_input)
    
    education_op = {
        "graduate": 1,
        "Not graduate": 0
    }
    selected_education = st.selectbox("Select educational status", list(education_op.keys()))

    # Get the corresponding value based on the selected label
    education_value = education_op[selected_education]
    user_inputs.append(education_value)

    # Inputs for integer numbers
    questions_integer = ["Enter ApplicantIncome", "Enter CoapplicantIncome", "Enter LoanAmount", "Enter Loan_Amount_Term", "Enter Credit_History	", "Property_Area"]
    for i in range(6):
        question = questions_integer[i]
        question_input = st.text_input(f"{question} (Integer Number)", value="0")
        user_input = int(question_input)
        user_inputs.append(user_input)

    # Convert user_inputs list to a 2D array
    user_inputs_array = np.array(user_inputs).reshape(1, -1)

    # Predict button
    if st.button("Predict"):
        loan_prediction = predict_loan_approval(user_inputs_array)

        # Display the prediction result
        if loan_prediction == 1:
            st.header("Loan Approved!")
        else:
            st.header("Loan Not Approved!")

if __name__ == "__main__":
    main()
