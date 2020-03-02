from pickle import load

from tree_execute.execute import compute_answer
from tree_execute.parser.parser import parse_data

tree_file_name = 'resources/tree.pickle'

with open(tree_file_name, 'rb') as file:
    decision_tree = load(file)

print(compute_answer(parse_data(), decision_tree))