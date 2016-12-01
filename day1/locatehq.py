class location():

    earthy_directions = ['north', 'east', 'south', 'west']

    def __repr__(self):
        return 'Locate the headquarters of the easter bunny'

    def __init__(self):
        self.x_axes = 0
        self.y_axes = 0
        self.cur_direction = self.earthy_directions[0]

    def set_direction(self, rotation):
        if rotation == 'R' and self.cur_direction == 'west':
            self.cur_direction =  self.earthy_directions[0]
        elif rotation == 'R':
            self.cur_direction = self.earthy_directions[self.earthy_directions.index(self.cur_direction) + 1]
        elif rotation == 'L':
            self.cur_direction = self.earthy_directions[self.earthy_directions.index(self.cur_direction) - 1]
        else:
            raise Exception

    def manipulate_coordinates(self, num_moves):
        if self.cur_direction in ('north' , 'south'):
            if self.cur_direction == 'north':
                self.y_axes += num_moves
            else:
                self.y_axes -= num_moves
        else:
            if self.cur_direction == 'west':
                self.x_axes -= num_moves
            else:
                self.x_axes += num_moves

    def move(self, instruction):
        self.set_direction(instruction[0])
        self.manipulate_coordinates(int(instruction[1:]))

if __name__ == '__main__':
    x = location()

    visited_locations = []
    input = ['L5', 'R1', 'R4', 'L5', 'L4', 'R3', 'R1', 'L1', 'R4', 'R5', 'L1', 'L3', 'R4', 'L2', 'L4', 'R2', 'L4', 'L1',
             'R3', 'R1', 'R1', 'L1', 'R1', 'L5', 'R5', 'R2', 'L5', 'R2', 'R1', 'L2', 'L4', 'L4', 'R191', 'R2', 'R5',
             'R1', 'L1', 'L2', 'R5', 'L2', 'L3', 'R4', 'L1', 'L1', 'R1', 'R50', 'L1', 'R1', 'R76', 'R5', 'R4', 'R2',
             'L5', 'L3', 'L5', 'R2', 'R1', 'L1', 'R2', 'L3', 'R4', 'R2', 'L1', 'L1', 'R4', 'L1', 'L1', 'R185', 'R1',
             'L5', 'L4', 'L5', 'L3', 'R2', 'R3', 'R1', 'L5', 'R1', 'L3', 'L2', 'L2', 'R5', 'L1', 'L1', 'L3', 'R1',
             'R4', 'L2', 'L1', 'L1', 'L3', 'L4', 'R5', 'L2', 'R3', 'R5', 'R1', 'L4', 'R5', 'L3', 'R3', 'R3', 'R1', 'R1',
             'R5', 'R2', 'L2', 'R5', 'L5', 'L4', 'R4', 'R3', 'R5', 'R1', 'L3', 'R1', 'L2', 'L2', 'R3', 'R4', 'L1', 'R4',
             'L1', 'R4', 'R3', 'L1', 'L4', 'L1', 'L5', 'L2', 'R2', 'L1', 'R1', 'L5', 'L3', 'R4', 'L1', 'R5', 'L5', 'L5',
             'L1', 'L3', 'R1', 'R5', 'L2', 'L4', 'L5', 'L1', 'L1', 'L2', 'R5', 'R5', 'L4', 'R3', 'L2', 'L1', 'L3', 'L4',
             'L5', 'L5', 'L2', 'R4', 'R3', 'L5', 'R4', 'R2', 'R1', 'L5']

    count = 0

    for i in input:
        x.move(i)
        if str(str(x.y_axes) + ',' + str(x.x_axes)) in visited_locations:
            count += 1
            print('Found same location for ' + str(count) + ' time: ' + str(str(x.y_axes) + ',' + str(x.x_axes)))
            print('Moves: ' + str(x.y_axes + x.x_axes))

        visited_locations.append(str(str(x.x_axes) + ',' + str(x.y_axes)))
        print(str(x.y_axes) + ',' + str(x.x_axes))

    print('Final Answer: ' + str(x.y_axes) + ',' + str(x.x_axes))
    print('Moves: ' + str(x.y_axes + x.x_axes))

    print('Answer Q2')
