movie_name = input()
student = 0
standard = 0
kid = 0
total_tickets = 0
hall_full = 0
all_tickets = 0

while movie_name != 'Finish':
    free_seats = int(input())

    for i in range(1, free_seats + 1):
        ticket_type = input()

        if ticket_type == 'End':
            hall_full = (total_tickets / free_seats) * 100
            print(f"{movie_name} - {hall_full:.2f}% full.")
            break

        elif ticket_type == 'student':
            student += 1

        elif ticket_type == 'standard':
            standard += 1

        elif ticket_type == 'kid':
            kid += 1
        total_tickets += 1
        if i == free_seats:
            hall_full = (total_tickets / free_seats) * 100
            print(f"{movie_name} - {hall_full:.2f}% full.")
            break

    all_tickets += total_tickets
    total_tickets = 0

    movie_name = input()

else:
    print(f"Total tickets: {all_tickets}")
    print(f"{((student / all_tickets) * 100):.2f}% student tickets.")
    print(f"{((standard / all_tickets) * 100):.2f}% standard tickets.")
    print(f"{((kid / all_tickets) * 100):.2f}% kids tickets.")