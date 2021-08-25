def fizzbuzz(num):
    for i in range(num):
        if i > 0 and i % 15 == 0:
            print('fizzbuzz')
        elif i > 0 and i % 5 == 0:
            print('buzz')
        elif i > 0 and i % 3 == 0:
            print('fizz')
        else:
            print(i)
fizzbuzz(61)
