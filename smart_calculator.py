# write your code here
exit_phrase = "/exit"

while True:
    numbers = input()
    if numbers == exit_phrase:
        break
    numbers = numbers.split(" ")
    if numbers[0] == '':
        continue
    elif len(numbers) == 1:
        print(numbers[0])
    else:
        print(int(numbers[0]) + int(numbers[1]))

print("Bye!")
