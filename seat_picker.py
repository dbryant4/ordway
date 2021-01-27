import json
import argparse

class Seat(object):
    ''' A seat within a Venue().

        Parameters:
            - `row` is the numerical row starting at 0.
            - `col` is the column starting at 0.
            - `status` is a string representing the status of the Seat.

    '''

    def __init__(self, row, col, status):
        self.row = row
        self.row_letter = chr(self.row + ord("a") - 1)
        self.col = col
        self.status = status

    def __repr__(self):
        return 'Seat %s%s: %s' % (self.row_letter, self.col, self.status)


class Venue(object):
    ''' Venue seating availablity.

        All seats are initialized as 'UNAVAILABLE'. Use `set_seat_statuses()` to
        bulk set seating status.
    '''

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._init_seat_map()


    def _init_seat_map(self):
        ''' Initilize Venue seat map '''

        self.seats = []
        for row in range(0, self.rows):
            self.seats.append([])
            for col in range(0, self.columns):
                self.seats[row].append(Seat(row+1, col+1, 'UNAVAILABLE'))


    def set_seat_statuses(self, seat_status):
        '''
            Bulk set seat status.

            `seat_status` is a JSON blob as described below.

            ```
            {
                "a1": {
                  "id": "a1",
                  "row": "a",
                  "column": 1,
                  "status": "AVAILABLE"
                },
                "b5": {
                  "id": "b5",
                  "row": "b",
                  "column": 5,
                  "status": "AVAILABLE"
                },
                "h7": {
                  "id": "h7",
                  "row": "h",
                  "column": 7,
                  "status": "AVAILABLE"
                }
            }
            ```
        '''

        for seat, seat_details in seat_status.items():
            row = seat_details['row']
            col = seat_details['column']
            self.set_seat_status(row, col, seat_details['status'])


    def set_seat_status(self, row, col, status):
        ''' Set the status of a seat.

            - `row` can be either a string or integer.
                Strings will be converted to a numeric value.

            - `col` is an integer starting at 1. For example, seat "b1" is the
                first seat in the second row.
        '''

        if isinstance(row, str):
            row = ord(row) - ord('a')
        col = col - 1

        self.seats[row][col].status = status


    def seat_preference_order(self):
        '''
            Generate the preferred seating order within a row. Column is 0 indexed.

            Example, for a 5 column wide row, the preferred seating order is
                [2,1,3,0,4]
        '''

        center = round(self.columns / 2)
        seat_position_order = []
        for position in range(0, center):
            seat_position_order.append(self.columns-position-1)
            seat_position_order.append(position)

        if (self.columns % 2) != 0:
            seat_position_order.append(center)

        seat_position_order.reverse()
        return seat_position_order


    def best_available_seat(self):
        ''' Return the best available Seat() in the Venue() '''

        seat_order = self.seat_preference_order()

        for row, seats in enumerate(self.seats):
            for col in seat_order:
                if self.seats[row][col].status == 'AVAILABLE':
                    return self.seats[row][col]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find the best available seat in a venue.')

    parser.add_argument('json_file', metavar='JSON_FILE', type=str,
                        help='File describing the Venue and available seats.')
    args = parser.parse_args()

    with open(args.json_file) as json_file:
        json_data = json.load(json_file)

    venue_rows = json_data['venue']['layout']['rows']
    venue_columns = json_data['venue']['layout']['columns']
    available_seats = json_data.get('seats')

    venue = Venue(venue_rows, venue_columns)
    venue.set_seat_statuses(available_seats)

    best_seat = venue.best_available_seat()
    print('Best available seat: %s' % best_seat)
