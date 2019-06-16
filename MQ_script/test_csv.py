import csv

d = list(range(38685))
with open('./kinetics_test.csv') as f1:
    f_csv = csv.DictReader(f1)
    for i, row in enumerate(f_csv):
        print(row)
        key1 = 'label'
        value1 = 'test'
        row[key1] = value1
        key2 = 'is_cc'
        value2 = '0'
        row[key2] = value2
        d[i] = row
f1.close()
headers = ['label', 'youtube_id', 'time_start', 'time_end', 'split', 'is_cc']
with open('./kinetics_test_new_.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(d)
f.close()
with open('./kinetics_test_new_.csv', 'rt') as fin:
    lines = ''
    for line in fin:
        if line != '\n':
            lines += line
with open('./kinetics_test_new.csv', 'wt')as fout:
    fout.write(lines)
