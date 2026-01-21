import datetime

start = '2026-01-05'
end = '2026-01-05'

format = '%Y-%m-%d'
start_date = datetime.datetime.strptime(start, format)
end_date = datetime.datetime.strptime(end, format)
##

## Test
test_start = datetime.datetime.strptime("2026-01-03", format)
test_end = datetime.datetime.strptime("2026-01-06", format)

start_between = test_start <= start_date <= test_end
end_between = test_start <= end_date <= test_end
overlap = (start_date <= test_start) & (end_date >= test_end)

if start_between or end_between or overlap:
  print("Invalid!")
else:
  print(start_between, end_between, overlap)