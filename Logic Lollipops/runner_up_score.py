if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score_array = []
    for item in arr:
        score_array.append(item)

    max_score = -100
    for item in score_array:
        if item > max_score:
            max_score = item

    runner_up_score = -100
    for item in score_array:
        if item > runner_up_score and item < max_score:
            runner_up_score = item

    print(runner_up_score)