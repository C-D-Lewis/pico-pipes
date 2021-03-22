import sys
import time
import csv

file_name = sys.argv[1]
tracks = sys.argv[2]

data = {
  'timeline': []
}

# The main function
def main():
  # Load CSV file
  with open(file_name) as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      # Headers
      if line_count == 0:
        line_count += 1
      else:
        data['timeline'].append({
          'track': int(row[0]),
          'is_on': bool(row[1]),
          'pitch': int(row[2]),
          'at': float(row[3])
        })
        line_count += 1
    print(f"Read {line_count} lines.")

  # 'Play' events
  for i, row in enumerate(data['timeline']):
    print(row)
    time_to_next = data['timeline'][i + 1]['at'] - row['at']
    time.sleep(time_to_next)

if '__main__' in __name__:
  main()
