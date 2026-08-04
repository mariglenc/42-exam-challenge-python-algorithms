def assign_meeting_rooms(meetings: list[list[int]]) -> tuple[int, dict]:
    rooms: dict[int, list[list[int]]] = {}

    for meeting in sorted(meetings):
        start = meeting[0]
        for schedule in rooms.values():     # dict order == room 0, 1, 2, ...
            if schedule[-1][1] <= start:
                schedule.append(meeting)
                break
        else:
            rooms[len(rooms)] = [meeting]

    return len(rooms), rooms
