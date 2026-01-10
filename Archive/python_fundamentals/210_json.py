"""
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

"""

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, 
# you can parse it by using the json.loads() method

def convert_from_json2python():
    # some json dict
    sample_json_text = '{"name":"Stephan","age":"25"}'

    # parse sample_json_text 
    stored_json_text = json.loads(sample_json_text)

    # the result is a Python Dictionary
    print(stored_json_text["age"])
def convert_from_python2json():
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
    sample_python_dict= {"name": "John",
                          "age":30,
                          "city":"New York"}
    # convert into JSON
    # stored_json_text = json.dumps(sample_python_dict)

    # Use the indent parameter to define the numbers of indents:
    stored_json_text = json.dumps(sample_python_dict, indent=4)

    
    # the resutl is a JSON string:
    print(stored_json_text)

#if "__name__" == (mai)
#convert_from_json2python()
convert_from_python2json()