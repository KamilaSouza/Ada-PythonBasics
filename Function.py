def hello():
    print("Hello World")


hello()


def media(value1=0, value2=0, value3=0):
    sum = value1 + value2 + value3
    media = sum / 3
    return media

print(media())

result = media(10, 19, 20)
print(result)

result2 = media(value1=1, value2=2, value3=3)
print(result2)
