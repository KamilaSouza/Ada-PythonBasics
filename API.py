import requests

url = "https://api.exchangerate-api.com/v6/latest"

req = requests.get(url)

print(req.status_code)

data = req.json()

print(data)

real_value = float(input("Enter the value in R$ to be converted\n"))
quotation = data["rates"]["BRL"]
print(f"R${real_value} in Real value US${(real_value / quotation):.2f} in dollar.")