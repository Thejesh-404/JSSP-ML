import pickle

# Replace 'your_file.pkl' with the path to your pickle file
file_path = 'data_zhang_L2D/6_6_Seed200.pkl'

# Load the data from the pickle file
with open(file_path, 'rb') as file:
    jss_dataset = pickle.load(file)

print((jss_dataset.size))
