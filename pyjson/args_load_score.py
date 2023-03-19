import json
import sys

# Check if the user provided an input file name
if len(sys.argv) != 2:
    print('Usage: python script.py input_file.json')
    sys.exit(1)

# Load JSON data from the input file
input_file_name = sys.argv[1]
with open(input_file_name, 'r') as f:
    data = json.load(f)



# Add a new quiz with its date and score
new_quiz = 'multiplication_by_11'
new_date = '16 March 2023'
new_score = 'You got 222 out of 300 questions correct!'
data[new_quiz] = {'date': new_date, 'score': new_score}

# Write the updated JSON data to a file or do whatever you want with it
output_file_name = "updated_data.json"
with open(output_file_name, 'w') as f:
    json.dump(data, f)

print(f'Successfully updated {output_file_name} with new quiz {new_quiz}.')
