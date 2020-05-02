import csv
#final desired format
# charts [["Testname",<difference of avg]]
# spreadsheet [["Testname",<current runtime>]]
timing_data = []
#with open('data.csv','r') as csv_file:
 #   file_reader = csv.reader(csv_file)
file_reader = open('data.csv','r')
file_input = csv.reader(file_reader)
for row in file_input:
    timing_data.append(row)

print(timing_data)
column_chart_data = [["Test Name","Diff from avg"]]
table_data = [["Test name","Run time (s)"]]

for row in timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_run_time = float(row[1])
    avg_run_time = float(row[2])
    diff_avg_time = current_run_time - avg_run_time
    column_chart_data.append([test_name,diff_avg_time])
    table_data.append([test_name,current_run_time])

print("Column data ##############")
print(column_chart_data)
print("########table data############")
print(table_data)
