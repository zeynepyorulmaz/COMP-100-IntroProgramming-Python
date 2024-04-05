def empty_seats(seat_config):
    a = 0
    for i in range(len(seat_config)):
        if seat_config[i] == "O":
            a += 1
    return a

def is_there_a_solution(num_of_chars, seat_config):

    if num_of_chars <= empty_seats(seat_config):
        return "YES"
    else:
        return "NO"


def get_the_solution(num_of_chars, seat_config):
    if is_there_a_solution(num_of_chars, seat_config) == "YES":
        solution = seat_config.replace("O","S", num_of_chars)
        return solution
    else:
        return "X"
a = [6,4]
b = [5,5]
