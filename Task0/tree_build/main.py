from pickle import *

from model.attributes import Attribute
from tree_build.dataset import dataset
from tree_build.decision_tree import build_decision_tree

decision_tree = build_decision_tree(dataset, [attr for attr in Attribute])
tree_file_name = "resources/tree.pickle"

with open(tree_file_name, 'wb') as tree_file:
    dump(decision_tree, tree_file)
