#Q_1
my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict['name'])
my_dict['age']=32
my_dict['workplace']='GSG'
print(my_dict)
#Q_2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
dict={value: key for key, value in my_tuple}
print(dict)
#Q_3
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
print({**dic1,**dic2,**dic3})
#Q_4
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
print(max(my_dict.values()))
print(min(my_dict.values()))
#Q_5
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
print(my_dict.keys()=='id')
#Q_6
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'], 'Market Share %': [27.99, 15.9, 9.36, 6.67]}
lists = zip(Languages2023['Programming Language'], Languages2023['Market Share %'])
list = list(map(lambda x: {'Programming Language': x[0], 'Market Share %': x[1]}, lists))
print(list)

