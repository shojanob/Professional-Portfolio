student_dict = {
    "student": ["Shoh", "James", "Alex"],
    "score": [56, 88, 97]
}

# Looping through dictionaries
# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "Shoh":
        print(row.score)

# Data Frame Dictionary Comprehension
# {new_key:new_value for (index,row) in df.iterrows()}