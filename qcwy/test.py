import pandas as pd

data = pd.read_csv('data/cln_data/cln_salary.csv')

city_value = [['北京',123],['上海',123]]
city_lng_lat = [[117.01799673877318,25.07868543351518,'北京']]

for item in city_value:
    print('{name:\'' + str(item[0]) + '\',value:' + str(item[1]) + '},')
print('-' * 40)
for item in city_lng_lat:
    print('\'{}\':[{},{}]'.format(item[2], item[0], item[1]))