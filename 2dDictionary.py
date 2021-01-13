dictionary_fields = {'first_name': ' ', 'last_name': ' ', 'dept': ' ', 'major': ' ', 'year': ' ' }
student_id = [1, 2, 3, 4, 5]
student_record = {}
#To create 5 records: We will run loop for 5 times
for i in range(0, 5):
student_record.update({student_id[i]: dict(dictionary_fields)})
#Add two items to 2D dictionary
student_record[1]['first_name'] = "John"
student_record[1]['last_name'] = "Wick"
student_record[1]['dept'] = "Engineering"
student_record[1]['major'] = "CSE"
student_record[1]['year'] = 2022
student_record[2]['first_name'] = "Albert"
student_record[2]['last_name'] = "Sons"
student_record[2]['dept'] = "Engineering"
student_record[2]['major'] = "ECE"
student_record[2]['year'] = 2023
for i in range(1, 3):
print(student_record[i])

