def meeting_room_scheduler(meetings: list[list[int]]) -> dict:

    rooms = []

    for start, end in sorted(meetings):
        room = min(rooms, key=lambda r: r[-1][1], default=None)

        if room is not None and room[-1][1] <= start:
            room.append([start, end])
        else:
            rooms.append([[start, end]])

    return {
        "rooms_needed": len(rooms),
        "room_assignments": dict(enumerate(rooms)),
    }

if __name__ == "__main__":
    print(meeting_room_scheduler([[0, 30], [5, 10], [15, 20]]))
    print(meeting_room_scheduler([[9, 10], [9, 12], [11, 13]]))