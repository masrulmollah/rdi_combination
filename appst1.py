import streamlit as st
import itertools
import pandas as pd

# Define a function to find the most and least costly combinations
def find_costly_combinations(data, combination_size):
    # Generate all combinations of specified size
    combinations = list(itertools.combinations(data['name'], combination_size))

    # Calculate the net value of each combination
    nets = [data[data['name'].isin(combo)]['net'].sum() for combo in combinations]

    # Find the most and least costly combination
    max_net = max(nets)
    min_net = min(nets)

    # Find the combinations with max and min nets
    most_costly_combo = combinations[nets.index(max_net)]
    least_costly_combo = combinations[nets.index(min_net)]

    # Return the results
    return most_costly_combo, least_costly_combo, max_net, min_net

# Define the Streamlit app
def main():
    st.title("Costly RDI Combinations Finder")

    # Upload a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)

        # Get user input for the size of combinations
        combination_size = st.number_input("Enter the size of combinations:", min_value=1, max_value=len(data['name']), value=3)

        if st.button("Find Combinations"):
            # Find the most and least costly combinations
            most_costly_combo, least_costly_combo, max_net, min_net = find_costly_combinations(data, combination_size)

            # Display the results
            st.write(f"The most costly combination is: {', '.join(most_costly_combo)}")
            st.write(f"The least costly combination is: {', '.join(least_costly_combo)}")
            st.write(f"Net value of the most costly combination: {max_net}")
            st.write(f"Net value of the least costly combination: {min_net}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
