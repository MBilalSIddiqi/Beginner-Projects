def Two_sum(numbers, target):
    answers = []
    a = len(numbers)
    for i in range(a):
        for j in range(i + 1, a):
            if numbers[i] + numbers[j] == target:
                answers.append([numbers[i], numbers[j]])

        return answers


print(Two_sum([1, 2, 3, 4, 5], 5))
