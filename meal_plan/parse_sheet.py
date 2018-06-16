""" Module to parse input from spreadsheet
"""
import re
import logging

ingr_regex = re.compile(r'^(?P<name>[^\d]*)(?P<quantity>[\d\.]*)(?P<unit>.*)')
_log = logging.getLogger(__name__)

def parse_csv(csv_data):
    data = []
    for line in csv_data:
        name, serves, ingredients_str = line.split('\t')
        ingredients = []
        for ingredient_str in ingredients_str.split(','):
            match = ingr_regex.match(ingredient_str)
            if not match:
                _log.error('Could not read ingredient "{}"'.format(ingredient_str))
                continue
            ingredients.append(
                {
                    'name': match.group('name'),
                    'quantity': float(match.group('quantity') or 1),
                    'unit': match.group('unit')
                }
            )
        data.append({
            'name': name,
            'serves': float(serves),
            'ingredients': ingredients
        })

    return data
