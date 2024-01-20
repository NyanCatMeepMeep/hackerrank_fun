if __name__ == '__main__':
    students = []
    scores = []
    student_scores = {}

    for _ in range(int(input())):
        students.append(input())
        scores.append(float(input()))

    if len(students) != len(scores):
        print('ERROR: Looks like the number of scores does not match the number of students.  '
              '\n Please check your input source and try again')
        quit()

    on_entry = 0
    max_entry = len(students) - 1
    for entry in students:
        student_scores[students[on_entry]] = scores[on_entry]
        on_entry = on_entry + 1

    student_lowest_score = min(student_scores, key=student_scores.get)
    lowest_score = student_scores[student_lowest_score]

    second_lowest_score = 100

    for key, value in student_scores.items():
        curr_score = float(value)
        if curr_score > lowest_score and curr_score < second_lowest_score:
            second_lowest_score = value

    # now I want to find the keys in the dictionary (student names) that match this
    second_lowest_score_locations = []

    for key, value in student_scores.items():
        if value == second_lowest_score:
            second_lowest_score_locations.append(key)

    return_string = ''
    for item in sorted(second_lowest_score_locations):
        return_string = return_string + str(item) + '\n'

    print(return_string[:-1])