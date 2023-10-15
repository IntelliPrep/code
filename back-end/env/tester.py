from algorithm import algo
from datetime import date

test1 = {
  "name": "1554",
  "date": "2023-10-18",
  "topics": ["Matrices", "Eigenvalues", "Linear independence"],
  "priorities": ["Low", "High", "Medium"]
}
test2 = {
  "name": "1331",
  "date": "2023-10-17",
  "topics": ["Inheritance", "Abstract classes", "Polymorphism", "Visibility"],
  "priorities": ["Medium", "Low", "High", "Low"]
}

test_array = [test1, test2]

weekday_array = ["3:30", "6:30"]
weekend_array = ["10:30", "12:30"]

arr = algo.create_schedule(test_array, weekday_array, weekend_array, date.today())

print(arr)