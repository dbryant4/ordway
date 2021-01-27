# Venue Seat Picker

A Python class that returns the best available seat for a given Venue's availability.

## Limitations
  - The seating layout must be rectangular, that is, each row much have the same number of columns.
  - The max number of rows is "z". This class does not support double letters such as "aa".
  - This class only returns one seat.

## Requirements
  - Python 3
  - Venue JSON Blob (see example below)
  - pytest (`pip3 install pytest`)

## Usage

### Command Line

This class can operate as a command line tool. Example usage, `python3 ./seat_picker.py venue.json`

### To Run Tests

To run tests, ensure `pytest` is installed for Python 3. Then run, `PYTHONPATH=. pytest` from the root of this repo.


## Example Venue JSON

```
{
  "venue": {
    "layout": {
      "rows": 10,
      "columns": 50
    }
  },
  "seats": {
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
}
```
