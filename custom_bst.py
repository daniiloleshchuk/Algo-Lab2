from models import Hamster


class CustomBST:

    class Node:
        def __init__(self, value, parent, key):
            self.value = value
            self.parent_node = parent
            self.left_child_node = None
            self.right_child_node = None
            self.key = key
            self.is_taken = False

    def __init__(self, key_to_compare, *values):
        self._key_to_compare = key_to_compare
        self._root_node = None

        if len(values) > 0:
            for value in values:
                self.add(value)

    def _get_min_element(self):
        if self._root_node is not None:
            cur_node = self._root_node
            while cur_node.left_child_node is not None:
                cur_node = cur_node.left_child_node

            return cur_node

    def _get_max_element(self):
        if self._root_node is not None:
            cur_node = self._root_node
            while cur_node.right_child_node is not None:
                cur_node = cur_node.right_child_node

            return cur_node

    def add(self, new_value):
        cur_node = self._root_node

        if self._root_node is None:
            self._root_node = self.Node(new_value, parent=None, key=self._key_to_compare(new_value))
            return

        while True:

            if self._key_to_compare(cur_node.value) < self._key_to_compare(new_value):
                if cur_node.right_child_node is None:
                    cur_node.right_child_node = self.Node(new_value, parent=cur_node, key=self._key_to_compare(new_value))
                    return
                else:
                    cur_node = cur_node.right_child_node
            elif self._key_to_compare(cur_node.value) > self._key_to_compare(new_value):
                if cur_node.left_child_node is None:
                    cur_node.left_child_node = self.Node(new_value, parent=cur_node, key=self._key_to_compare(new_value))
                    return
                else:
                    cur_node = cur_node.left_child_node
            else:
                cur_node.value = new_value
                return

    def get_min_value(self):
        return self._get_min_element().value

    def get_max_value(self):
        return self._get_max_element().value

    def remove_min_element(self):
        min_element = self._get_min_element()
        if min_element.right_child_node is not None:
            if min_element.parent_node is None:
                min_element.right_child_node.parent_node = None
                self._root_node = min_element.right_child_node
            else:
                min_element.parent_node.left_child_node = min_element.right_child_node
        else:
            if min_element.parent_node is not None:
                min_element.parent_node.left_child_node = None
            else:
                self._root_node = None


if __name__ == '__main__':
    bst = CustomBST(lambda x: (x.daily_norm, x.greediness), Hamster(5, 0), Hamster(3, 2), Hamster(1, 4), Hamster(5, 1), Hamster(2, 2))
    print(bst.get_min_value())
    #bst.remove_min_element()
    print(bst.get_min_value())
    # Hamster(1, 2), Hamster(2, 2), Hamster(3, 1)
    # Hamster(5, 0), Hamster(2, 2), Hamster(1, 4), Hamster(5, 1)
    # Hamster(1, 50000), Hamster(1, 60000)



