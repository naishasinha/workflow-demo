import csv

# Define the path to CSV file
csv_file_path = 'example_csv.csv'

# Open the CSV file in append mode
with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the new row to CSV file
    writer.writerow(['hello'])