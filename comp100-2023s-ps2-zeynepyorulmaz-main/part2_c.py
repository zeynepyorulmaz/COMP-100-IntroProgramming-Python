def is_there_a_solution_C2(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
    seats_per_subgroup = num_of_chars // num_of_subgroups
    slots = seat_config.split('|')
    last_seat_config = ""
    reserved_seats = 0
    for slot in slots:

        for i in range(len(slot)):
            solution = slot
            if slot[i:seats_per_subgroup:] == "O"*seats_per_subgroup:
                solution = slot.replace("O","S")


            last_seat_config += solution + "|"
    for k in range(len(last_seat_config)):
        if last_seat_config[k] == "S":
            reserved_seats += 1
    if reserved_seats == num_of_chars:
        return "YES"
    else:
        return "NO"
print(is_there_a_solution_C2(6, 3, 2, 'OO|OX|OO|XX|XO|OO'))
print(is_there_a_solution_C2(8, 4, 4, 'OXXO|OXXO|OOOO'))
print(is_there_a_solution_C2(12, 3, 6, 'OOOOOO|OOXXO|XOOOOX'))

