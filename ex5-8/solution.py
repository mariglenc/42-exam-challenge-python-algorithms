def assign_meeting_rooms(meetings: list[list[int]]) -> tuple[int, dict]:
    if not meetings:
        return 0, {}

    rooms = {}

    for meeting in sorted(meetings):
        start = meeting[0]
        placed = False

        # first-fit: the lowest-numbered room whose last meeting has ended
        for schedule in rooms.values():
            if start >= schedule[-1][1]:
                schedule.append(meeting)
                placed = True
                break

        if not placed:
            rooms[len(rooms)] = [meeting]

    return len(rooms), rooms


if __name__ == "__main__":
    print(assign_meeting_rooms([[9, 10], [9, 12], [11, 13]]))
    # (2, {0: [[9, 10], [11, 13]], 1: [[9, 12]]})
    print(assign_meeting_rooms([[10, 20], [15, 25], [20, 30], [5, 10]]))
    # (2, {0: [[5, 10], [10, 20], [20, 30]], 1: [[15, 25]]})
