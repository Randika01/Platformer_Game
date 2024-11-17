import pickle

# Load the data
with open('level3_data', 'rb') as file:
    data = pickle.load(file)

# Print the data to see its structure
print("Original data:")
for row in data:
    print(row)

# Modify the data (example: set a tile at position (x, y) to a platform (1))
x, y = 8, 18  # Example coordinates
data[y][x] = 3  # Change the value at the specified coordinates to 1 (platform)

# Print the modified data to verify changes
print("\nModified data:")
for row in data:
    print(row)

# Save the modified data
with open('level3_data', 'wb') as file:
    pickle.dump(data, file)
