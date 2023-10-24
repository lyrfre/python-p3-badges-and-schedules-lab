def badge_maker(name):
    return (f"Hello, my name is {name}.")
    
print(badge_maker("Erin"))

names = ["Arel", "Carol"]



def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges
    
batches = [(f"Hello, my name is {name}.") for name in names]

print(batches)
print(batch_badge_creator(names))



def assign_rooms(names):
    rooms = range(1, 3)
    
    assignments = []
    for room in rooms:
        assignments.append(f"Hello, {names[room -1]}! You'll be assigned to room {room}!")
    
    return assignments

print(assign_rooms(names))

def printer(names):
    for batch in batches:
        print(batch)

    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)

print(printer(names))