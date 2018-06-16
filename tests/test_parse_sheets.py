import os
import voluptuous
from voluptuous import Any, Number

from meal_plan import parse_sheet


def get_csv_data(name):
    with open(os.path.join(os.path.dirname(__file__), 'data', 'test_parse_sheets', name), 'r') as f:
        return f.readlines()


def test_parse_csv():
    csv_data = get_csv_data('from_google_sheets.csv')
    data = parse_sheet.parse_csv(csv_data)
    voluptuous.Schema([
        {
            'name': basestring,
            'serves': Number(),
            'ingredients': [
                {
                    'name': basestring,
                    'quantity': Number(),
                    'unit': Any(None, basestring)
                }
            ]
        }
    ])(data)
    exact_data = [
        {'ingredients': [{'name': 'Onion ', 'quantity': 1.0, 'unit': ''},
                  {'name': ' Sweetcorn ', 'quantity': 1.0, 'unit': ' tin'},
                  {'name': ' Black Beans ', 'quantity': 1.0, 'unit': ' tin'},
                  {'name': ' Dried Apricots ',
                   'quantity': 40.0,
                   'unit': 'g'},
                  {'name': ' Chicken Stock Pot ',
                   'quantity': 1.0,
                   'unit': ''},
                  {'name': ' Coconut Milk ',
                   'quantity': 200.0,
                   'unit': 'ml'},
                  {'name': ' Basmati Rice ', 'quantity': 150.0, 'unit': 'g'},
                  {'name': ' Beef Mince ', 'quantity': 250.0, 'unit': 'g'},
                  {'name': ' Poudre de Colombo ',
                   'quantity': 1.5,
                   'unit': 'tsp'},
                  {'name': ' Tomato Puree ', 'quantity': 30.0, 'unit': 'g'},
                  {'name': ' Mango Chutney ', 'quantity': 40.0, 'unit': 'g'},
                  {'name': ' Coriander ', 'quantity': 1.0, 'unit': ' bunch'},
                  {'name': ' Lime ', 'quantity': 0.5, 'unit': ''}],
        'name': 'Caribbean Spiced Beef with Coconut Rice and Sweecorn Salsa',
        'serves': 2.0},
        {'ingredients': [{'name': 'Onion ', 'quantity': 1.0, 'unit': ''},
                      {'name': ' Garlic ', 'quantity': 1.0, 'unit': ' clove'},
                      {'name': ' Closed Cup Mushrooms ',
                       'quantity': 1.0,
                       'unit': ' punnet'},
                      {'name': ' Broccoli ', 'quantity': 1.0, 'unit': ''},
                      {'name': ' Sweet Potato ', 'quantity': 1.0, 'unit': ''},
                      {'name': ' Beef Mince ', 'quantity': 250.0, 'unit': 'g'},
                      {'name': ' Netherend Butter ',
                       'quantity': 15.0,
                       'unit': 'g'},
                      {'name': ' Tomato Puree ', 'quantity': 30.0, 'unit': 'g'},
                      {'name': ' Diced Tomatoes ',
                       'quantity': 1.0,
                       'unit': ' tin'},
                      {'name': ' Wrocester Sauce ',
                       'quantity': 0.5,
                       'unit': 'tbsp'},
                      {'name': ' Beef Stock Pot ', 'quantity': 0.5, 'unit': ''},
                      {'name': ' Cheddar Cheese ',
                       'quantity': 30.0,
                       'unit': 'g'}],
        'name': 'Sweet Potato Cottage Pie with Roasted Broccoli',
        'serves': 2.0}
    ]
    assert data == exact_data

