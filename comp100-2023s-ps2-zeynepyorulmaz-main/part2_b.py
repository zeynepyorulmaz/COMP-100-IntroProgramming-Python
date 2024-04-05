def get_the_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
    seats_per_subgroup = num_of_chars // num_of_subgroups
    slots = seat_config.split('|')
    last_seat_config = ""
    reserved_seats = 0
    for slot in slots:

        empty_seats = 0
        for i in range(len(slot)):
            if slot[i] == "O":
                empty_seats += 1
        solution = slot
        while empty_seats >= seats_per_subgroup:
            solution = solution.replace("O", "S", seats_per_subgroup)
            empty_seats = 0

            for i in range(len(solution)):
                if solution[i] == "O":
                    empty_seats += 1


        last_seat_config = last_seat_config + solution + "|"
    last_seat_config = last_seat_config[:len(last_seat_config)-1:]
    for i in range(len(last_seat_config)):
        if last_seat_config[i] == "S":
            reserved_seats += 1

    if reserved_seats == num_of_chars:
        return last_seat_config
    else:
        return "X"



