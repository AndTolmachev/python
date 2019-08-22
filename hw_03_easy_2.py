def lucky_ticket(ticket_number):
    if (int(str(ticket_number)[0]) + int(str(ticket_number)[1]) +
            int(str(ticket_number)[2]) == int(str(ticket_number)[3]) +
            int(str(ticket_number)[4]) + int(str(ticket_number)[5])):
        return True
    else:
        return False


print(lucky_ticket(123006))

