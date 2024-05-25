def contact(a=7, *numbers, **phone_contacts):
    print(f'a =={a}')

    for item in numbers:
        print(f'item == {item}')

        for key, value in phone_contacts.items():
            print(key, value)



contact(9, 1, 2, 3, 4, 5, 6, Yug='+447479408387')

number = int(input("Enter a number: "))

if number % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"The number {number} is {result}.")