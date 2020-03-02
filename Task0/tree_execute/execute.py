def compute_answer(data, decision_tree_node):
    while decision_tree_node.children:
        decision_tree_node = decision_tree_node.children[data[decision_tree_node.value.value]]

    return decision_tree_node.value
