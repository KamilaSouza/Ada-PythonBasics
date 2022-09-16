def media(*args, margin):
    sum1 = sum(args)
    media = sum1 / len(args)
    return media + margin


print(media(10, 8, 9, margin=0.3))

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(name="Kami", lastName = "Souza")
