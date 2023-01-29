car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get('model'))
#Mustang


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['year']=2020
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['color']='red'
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#{'brand': 'Ford', 'year': 1964}


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#{}