import os
import math

# Specify the directory containing the txt files and images
folder_path = './'

# Initialize counters and lists
total_width = 0
total_height = 0
count = 0

widths = []
heights = []

# Iterate through the txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        txt_file_path = os.path.join(folder_path, filename)
        
        # Open the txt file for reading
        with open(txt_file_path, 'r') as file:
            for line in file:
                data = line.strip().split()
                class_id = int(data[0])  # The class ID
                
                # Only process data for class ID 2
                if class_id == 2:
                    width = float(data[3])  # Width
                    height = float(data[4])  # Height
                    total_width += width
                    total_height += height
                    widths.append(width)
                    heights.append(height)
                    count += 1

# Calculate the averages, standard deviation, min, and max
if count > 0:
    avg_width = total_width / count
    avg_height = total_height / count
    
    # Calculate standard deviation for width
    width_variance = sum((w - avg_width) ** 2 for w in widths) / count
    width_std_dev = math.sqrt(width_variance)
    
    # Calculate standard deviation for height
    height_variance = sum((h - avg_height) ** 2 for h in heights) / count
    height_std_dev = math.sqrt(height_variance)
    
    # Calculate min and max for width and height
    min_width = min(widths)
    max_width = max(widths)
    min_height = min(heights)
    max_height = max(heights)
    
    # Print the results
    print(f"Average width for class 2 objects: {avg_width*100:.2f}%")
    print(f"Standard deviation of width: {width_std_dev*100:.2f}")
    print(f"Minimum width: {min_width*100:.2f}%")
    print(f"Maximum width: {max_width*100:.2f}%\n")
    
    print(f"Average height for class 2 objects: {avg_height*100:.2f}%")
    print(f"Standard deviation of height: {height_std_dev*100:.2f}")
    print(f"Minimum height: {min_height*100:.2f}%")
    print(f"Maximum height: {max_height*100:.2f}%")
else:
    print("No objects found for class 2.")

