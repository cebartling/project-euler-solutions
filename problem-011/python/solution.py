#!/usr/bin/env python3

import os

def calculate_greatest_product_horizontally(current_greatest_product, rows):
    result = current_greatest_product
    for row_index in range(len(rows)):
        for column_index in range(len(row) - 3):
            product = rows[row_index][column_index] * rows[row_index][column_index + 1] * rows[row_index][column_index + 2] * rows[row_index][column_index + 3]
            if product > result:
                result = product
    return result

def calculate_greatest_product_vertically(current_greatest_product, rows):
    result = current_greatest_product
    for row_index in range(len(rows) - 3):
        for column_index in range(len(rows[row_index])):
            product = rows[row_index][column_index] * rows[row_index + 1][column_index] * rows[row_index + 2][column_index] * rows[row_index + 3][column_index]
            if product > result:
                result = product
    return result

def calculate_greatest_product_diagonally_right(current_greatest_product, rows):
    result = current_greatest_product
    for row_index in range(len(rows) - 3):
        for column_index in range(len(rows[row_index]) - 3):
            product = rows[row_index][column_index] * rows[row_index + 1][column_index + 1] * rows[row_index + 2][column_index + 2] * rows[row_index + 3][column_index + 3]
            if product > result:
                result = product
    return result

def calculate_greatest_product_diagonally_left(current_greatest_product, rows):
    result = current_greatest_product
    for row_index in range(len(rows) - 3):
        for column_index in range(len(rows[row_index]) - 3):
            product = rows[row_index][column_index + 3] * rows[row_index + 1][column_index + 2] * rows[row_index + 2][column_index + 1] * rows[row_index + 3][column_index]
            if product > result:
                result = product
    return result

path = os.path.dirname(os.path.abspath(__file__))
data_filename = os.path.join(path, 'data.txt')
rows = []
with open(data_filename, 'r') as file:
    for line in file:
        row = [int(x) for x in line.replace('\n', '').split()]
        rows.append(row)

greatest_product = 0
greatest_product = calculate_greatest_product_horizontally(greatest_product, rows)
greatest_product = calculate_greatest_product_vertically(greatest_product, rows)
greatest_product = calculate_greatest_product_diagonally_left(greatest_product, rows)
greatest_product = calculate_greatest_product_diagonally_right(greatest_product, rows)
print('Greatest product: {0}'.format(greatest_product))

