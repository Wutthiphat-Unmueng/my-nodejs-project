secret_number = 572943 + next 16 digits

letters = "92270bf339b1a31d0498defb0573fc7c"
digit_to_letter = dict(zip(str(secret_number), letters))

initial_value = 2

result = int(str(initial_value) + str(secret_number))

result = int(str(result) + "9")

result = int(str(result) + "1")

result = result * 5

result = int(str(result) + "6")

result = int(str(result)[::-1])

result = int(str(result).replace("2", "3"))

result = result * 9

result = int(str(result) + "24")

result = int("17" + str(result))

result = str(result)
final_result = ""
for digit in result:
    if digit in digit_to_letter:
        final_result += digit_to_letter[digit]
    else:
        final_result += digit

print(final_result)