import os

#чтение из файла
path_to_input = os.path.dirname(__file__) + '/input/2.html'

input_file = open(path_to_input, 'r')

text = ''.join(input_file.readlines())

input_file.close()

#сбор массива строк с <colgroup>
colgroup_string = []
col_counter = 0
lines = text
while(lines.find('<colgroup>') != -1):
    start = lines.find('<colgroup>')
    end = lines.find('</colgroup>') + 11
    colgroup_string.append(lines[start:end])
    lines = lines.replace(lines[start:end], '', 1)

#подсчёт суммы в пределах одного тега colgroup
sum_arr = []
for colgroup in colgroup_string:
    sum = 0
    while(colgroup.find('width="') != -1):
        start = colgroup.find('width="') + 6
        colgroup = colgroup.replace('"', '', 1)
        end = colgroup.find('"')
        sum += int(colgroup[start:end])
        colgroup = colgroup.replace('"', '', 1)
    sum_arr.append(sum)

# замена абсолютной величины на относительную
i = 0
output = ''
end_colgroup = len(text)
while(sum_arr != []):
    start_colgroup = text.find('<colgroup>')
    end_colgroup = text.find('</colgroup>') + 11
    string = text[start_colgroup:end_colgroup].split('<col')
    result = []
    for i in string:
        start_col = i.find('width="') + 7
        end_col = i.find('"', start_col)
        if i.find('width="') != -1:
            to_replace = str(round(int(i[start_col:end_col])/sum_arr[0] * 100)) + '%'
            i = i.replace(i[start_col:end_col], to_replace, 1)
        result.append(i)
    sum_arr.pop(0)
    result = '<col'.join(result)
    text = text.replace(text[start_colgroup:end_colgroup], result, 1)
    output += text[0:end_colgroup]
    text = text[end_colgroup:]

# обработка  тегов <td>
output += text
lines = output.split('\n')
result = []
for line in lines:
    start_td = line.find('<td ')
    if start_td != -1:
        start_width = line.find('width:')
        end_width = line.find(';', start_width) + 1
        line = line.replace(line[start_width:end_width], '', 1)
        end_td = line.find('>', start_td) + 1
        if line.find('\"\"', start_td, end_td) != -1:
            line = line.replace(line[start_td:end_td], '<td>', 1)
    result.append(line)

output = '\n'.join(result)
print(output)
    
#вывод
path_to_output = os.path.dirname(__file__) + '/output/2.html'

output_file = open(path_to_output, 'w')

output_file.write(output)

output_file.close()