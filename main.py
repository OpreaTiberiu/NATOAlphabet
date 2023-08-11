import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_to_nato_dict = {row.letter: row.code for (_, row) in student_data_frame.iterrows()}


keep_going = True
while keep_going:
    user_input = input("Enter a word to continue or Q to exit:")
    if user_input == "Q":
        break
    result = [letter_to_nato_dict[l.capitalize()] for l in user_input]
    print(result)
