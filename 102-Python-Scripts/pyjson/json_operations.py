import json

# JSON data
json_data_file = "test_data.json"

def load_json() :
    # Load JSON data from a file
    with open(json_data_file, 'r') as f:
        data = json.load(f)
    return data

def show_json() :
    data = load_json()

    # Print values for the 'date' and 'score' keys for each multiplication quiz
    for quiz in data:
        print(f"Quiz: {quiz}")
        print(f"date: {data[quiz]['date']}")
        print(f"score: {data[quiz]['score']}")
    
def append_data() :
    data = load_json()

    # Add a new quiz with its date and score
    new_quiz = 'multiplication_by_7'
    new_date = '16 March 2023'
    new_score = 'You got 2 out of 3 questions correct!'
    data[new_quiz] = {'date': new_date, 'score': new_score}

    # Convert dictionary back to JSON
    updated_json_data = json.dumps(data,indent=4)

    # Write the updated JSON data to a file or do whatever you want with it
    with open(json_data_file, 'w') as f:
        f.write(updated_json_data)

def retieve_specific_data() :
    data = load_json()

    # Retrieve the date of the multiplication_by_11 quiz
    quiz_name = 'multiplication_by_7'
    quiz_date = data[quiz_name]['date']

    print(f'The date of the {quiz_name} quiz is {quiz_date}.')    

# show_json()
retieve_specific_data()

