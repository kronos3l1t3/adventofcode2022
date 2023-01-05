# Count the number of trees visible from outside the grid
tree_map = [[30373, 25512, 65332, 33549, 35390],
            [41322, 61463, 54572, 64545, 51513],
            [33444, 64435, 52331, 54444, 54445],
            [45345, 54444, 22221, 54444, 54444],
            [54444, 54444, 54444, 54444, 54444]]

trees_visible = 0

for row in tree_map:
    if row[0] > 0:
        trees_visible += 1
    if row[-1] > 0:
        trees_visible += 1

for col in range(len(tree_map[0])):
    if tree_map[0][col] > 0:
        trees_visible += 1
    if tree_map[-1][col] > 0:
        trees_visible += 1

print(trees_visible)  # 21