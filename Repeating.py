city_names = ["São Paulo", "London", "Tokyo", "Paris"]
for name in city_names:
    print(name)

counter = 0
city_names = ["São Paulo", "London", "Tokyo", "Paris"]
while counter < len(city_names):
    print(city_names[counter])
    counter = counter + 1

city = {
    "name": "São Paulo",
    "state": "São Paulo",
    "population_million": 12.5
}

for key in city:
    print(f"{key}: {city[key]}")

for position in range(len(city_names)):
    city_names[position] = "Rio de Janeiro"
print(city_names)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))
