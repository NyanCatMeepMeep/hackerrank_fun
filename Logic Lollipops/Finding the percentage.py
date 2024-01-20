if __name__ == '__main__':
    n = int(input()) # between 2 and 10
    student_marks = {} # between 0 and 100
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        # Entered in one line as: Krishna 67 68 69
        student_marks[name] = scores
    query_name = input()

    scores = student_marks[query_name]
    num_scores = len(scores)
    calc_total = 0

    for item in scores:
        calc_total = calc_total + item

    average_score = calc_total / num_scores

    print(f'{average_score:.2f}')