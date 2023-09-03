def most_frequent_digits(a):
        # Initialize a dictionary to store the number of times each digit occurs in the array.
    digit_counts = {}
    for i in range(len(a)):
      digit = a[i] % 10
      if digit not in digit_counts:
        digit_counts[digit] = 0
      digit_counts[digit] += 1


      # Find the digit that occurs the most number of times in the array.
    most_frequent_digit = 0
    most_frequent_digit_count = 0
    for digit, count in digit_counts.items():
      if count > most_frequent_digit_count:
        most_frequent_digit = digit
        most_frequent_digit_count = count

    # Initialize an array to store the most frequent digits.
    most_frequent_digits = []


    for digit, count in digit_counts.items():
      if count == most_frequent_digit_count:
        most_frequent_digits.append(digit)


    # Sort the `most_frequent_digits` array in ascending order.
    most_frequent_digits.sort()

    return most_frequent_digits 


a = [25, 2, 3, 57, 38, 41]
print(most_frequent_digits(a))

