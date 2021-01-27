from seat_picker import Venue

def test_seat_preference_order():
    ''' Ensure the preferred seat order is correct for a given row '''

    venue = Venue(5,10)
    assert venue.seat_preference_order() == [4, 5, 3, 6, 2, 7, 1, 8, 0, 9]

    venue = Venue(5,5)
    assert venue.seat_preference_order() == [2, 1, 3, 0, 4]


def test_best_available_seat():
    ''' Ensure the best seat is returned '''


    available_seats = {
        "a3": {
            "id": "a3",
            "row": "a",
            "column": 3,
            "status": "AVAILABLE"
        },
        "b4": {
            "id": "b3",
            "row": "b",
            "column": 4,
            "status": "AVAILABLE"
        }
    }

    venue = Venue(5,10)
    venue.set_seat_statuses(available_seats)
    best_seat = venue.best_available_seat()

    assert best_seat.row_letter == "a"
    assert best_seat.col == 3
