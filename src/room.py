# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return (f'You are now in {self.name}. {self.description}. From here you have a choice:')
    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None
    def get_rooms(self):
        rooms = []
        if self.n_to:
            rooms.append(f"north to the {self.n_to.name}")
        if self.s_to:
            rooms.append(f"south to the {self.s_to.name}")
        if self.e_to:
            rooms.append(f"east to the {self.e_to.name}")
        if self.w_to:
            rooms.append(f"west to the {self.w_to.name}")
        return rooms
    def get_rooms_string(self):
        return f"You can go {', '.join(self.get_rooms())}"
