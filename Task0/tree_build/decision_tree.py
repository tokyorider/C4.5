from math import log2

from model.tree_node import TreeNode


def gain_ratio(set, attribute):
    return gain(set, attribute) / split_info(set, attribute)


def gain(set, attribute):
    return entropy(set) - entropy(set, attribute)


def entropy(set, attribute=None):
    if attribute is not None:
        sub_sets = [{data: answer for data, answer in set.items() if data[attribute.value] == attr_value}
                    for attr_value in attribute.values()]

        return sum([len(sub_set) / len(set) * entropy(sub_set) for sub_set in sub_sets if len(sub_set) > 0])

    true_prob = list(set.values()).count(True) / len(set) if len(set) > 0 else 0
    false_prob = 1 - true_prob
    return -1 * (true_prob * (log2(true_prob) if true_prob > 0 else 0)
                 + false_prob * (log2(false_prob) if false_prob > 0 else 0))


def split_info(set, attribute):
    sub_sets = [{data: answer for data, answer in set.items() if data[attribute.value] == attr_value}
                for attr_value in attribute.values()]

    return -1 * sum(
        [len(sub_set) / len(set) * log2(len(sub_set) / len(set)) for sub_set in sub_sets if len(sub_set) > 0])


def build_decision_tree(sub_dataset, attributes, parent_set=None):
    if len(sub_dataset) <= 1 or len(attributes) == 0:
        if parent_set is not None:
            return TreeNode(list(parent_set.values()).count(True) >= list(parent_set.values()).count(False), [])

        return None

    gain_ratios = {attribute: gain_ratio(sub_dataset, attribute) for attribute in attributes}
    best_attribute = max(gain_ratios, key=gain_ratios.get)
    attributes.remove(best_attribute)

    children = [build_decision_tree(
        {data: answer for data, answer in sub_dataset.items() if data[best_attribute.value] == attr_value},
        attributes, sub_dataset)
        for attr_value in best_attribute.values()]

    return TreeNode(best_attribute, children)
