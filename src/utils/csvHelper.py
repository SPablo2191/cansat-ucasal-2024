import pandas as pd

csv_file = r'C:\Flight_2030.csv'  # Path to the CSV file

# Function to write data to the CSV file
def write_to_csv(data):
    try:
        # Try to load the CSV file if it exists
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        df = pd.DataFrame()

    # Create a new DataFrame with the provided data
    new_df = pd.DataFrame([data])

    # Concatenate the new DataFrame with the existing one (if any)
    df = pd.concat([df, new_df], ignore_index=True)

    # Write the DataFrame to the CSV file
    df.to_csv(csv_file, index=False)





