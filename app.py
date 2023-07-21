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

    # Dropdowns for binary options (Yes or No)
    questions_binary = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]
    for question in questions_binary:
        user_input = st.selectbox(f"{question} (Select Yes or No)", ("Yes", "No"))
        binary_input = yes_no_to_binary(user_input)
        user_inputs.append(binary_input)

    # Inputs for integer numbers
    questions_integer = ["Question 6", "Question 7", "Question 8", "Question 9", "Question 10", "Question 11"]
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
