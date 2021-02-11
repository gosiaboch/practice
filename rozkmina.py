import random

def pass_gen_strong():
    list_a="0123456789"
    list_b="qwertyuioplkjhgfdsazxcvbnm"
    list_c="QWERTYUIOPLKJHGFDSAZXCVBNM"
    list_d="!#$%^&*<>,.?/\|"
    a=random.choices(list_a)+random.choices(list_a)+random.choices(list_a)+random.choices(list_b)+\
      random.choices(list_b)+random.choices(list_b)+random.choices(list_b)+random.choices(list_c)+random.choices(list_c)+random.choices(list_d)
    random.shuffle(a)
    result=" ".join(a)
    return result

def pass_gen_weak():
    list_a="qwertyuioplkjhgfdsazxcvbnm"
    a=random.choices(list_a)+random.choices(list_a)+random.choices(list_a)+random.choices(list_a)+random.choices(list_a)
    random.shuffle(a)
    result=" ".join(a)
    return result

while True:
    decision=input("silne haslo wybier 1, slabe wybierz 2, 3 zeby wyjsc: ")
    if decision=="1":
        print(pass_gen_strong())
    elif decision=="2":
        print("wybierz ktore chcesz")
        a=pass_gen_weak()
        print("opcja nr 1, nacisnij a: "+a)
        b=pass_gen_weak()
        print("opcja nr 2, nacisnij b: "+b)
        c=input(":")

        if c=="a":
            print(a)
        else:
            print(b)
    else:
        break