# ## Problem: Meeting Room Scheduler Using Dictionary

# You are given a list of meeting time intervals. Each meeting is represented as a list containing a start time and an end time:

# ```python
# [start_time, end_time]
# ```

# There are multiple rooms available. Your task is to assign every meeting to a room so that no two meetings overlap in the same room.

# Write a function:

# ```python
# def assign_meeting_rooms(meetings):
# ```

# The function should:

# 1. Calculate the minimum number of rooms required.
# 2. Assign each meeting to a room.
# 3. Return a dictionary where:

#    * The keys represent room numbers.
#    * The values are lists of meetings assigned to that room.

# The function should also return the total number of rooms needed.

# Two meetings can be placed in the same room if the next meeting starts at the same time or after the previous meeting ends.

# ---

# ### Example 1

# Input:

# ```python
# meetings = [
#     [9, 10],
#     [9, 12],
#     [11, 13]
# ]
# ```

# Output:

# ```python
# rooms_needed = 2

# rooms = {
#     0: [
#         [9, 10],
#         [11, 13]
#     ],
#     1: [
#         [9, 12]
#     ]
# }
# ```

# Explanation:

# * Room 0 contains `[9,10]` and `[11,13]` because they do not overlap.
# * Room 1 contains `[9,12]` because it overlaps with both meetings in Room 0.

# ---

# ### Example 2

# Input:

# ```python
# meetings = [
#     [8, 9],
#     [9, 10],
#     [10, 11]
# ]
# ```

# Output:

# ```python
# rooms_needed = 1

# rooms = {
#     0: [
#         [8, 9],
#         [9, 10],
#         [10, 11]
#     ]
# }
# ```

# # ---

# # ### Example 3

# # Input:

# # ```python
# # meetings = [
# #     [10, 20],
# #     [15, 25],
# #     [20, 30],
# #     [5, 10]
# # ]
# # ```

# # Output:

# # ```python
# # rooms_needed = 2

# # rooms = {
# #     0: [
# #         [5, 10],
# #         [10, 20],
# #         [20, 30]
# #     ],
# #     1: [
# #         [15, 25]
# #     ]
# # }
# # ```

# # ---

# # ### Expected return format:

# # ```python
# # return rooms_needed, rooms
# # ```

# # Example:

# # ```python
# # (
# #     2,
# #     {
# #         0: [[9,10], [11,13]],
# #         1: [[9,12]]
# #     }
# # )
# # ```


def assign_meeting_rooms(meetings):
    if not meetings:
        return 0, {}

    meetings.sort()

    rooms = {}

    room_number = 0

    for meeting in meetings:
        start = meeting[0]
        end = meeting[1]

        placed = False

        # kontrollojmë dhomat ekzistuese
        for room, schedule in rooms.items():

            # koha kur mbaron takimi i fundit në këtë dhomë
            last_end = schedule[-1][1]

            # nëse dhoma është e lirë
            if start >= last_end:
                schedule.append(meeting)
                placed = True
                break

        # nëse nuk gjetëm dhomë të lirë
        if not placed:
            rooms[room_number] = [meeting]
            room_number += 1

    return len(rooms), rooms


meetings = [
    [9, 10],
    [9, 12],
    [11, 13]
]

rooms_needed, rooms = assign_meeting_rooms(meetings)

print("Rooms needed:", rooms_needed)

for room, schedule in rooms.items():
    print(f"Room {room}: {schedule}")

