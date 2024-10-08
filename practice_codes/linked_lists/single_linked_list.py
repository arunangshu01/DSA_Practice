class SingleNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = str(self.value)
        return result


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            if current_node.next:
                result += ' -> '
            current_node = current_node.next
        return result

    def insert_at_the_end(self, value):
        new_node = SingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return

    def insert_at_the_beginning(self, value):
        new_node = SingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return

    def insert_at_anywhere(self, index, value):
        new_node = SingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            self.length += 1
            return
        elif index < 0:
            raise IndexError("Index is less than 0.")
        elif index > self.length:
            raise IndexError("Index is out of bounds")
        elif index == 0:
            self.insert_at_the_beginning(value=value)
        elif index == self.length:
            self.insert_at_the_end(value=value)
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            return

    def traverse_the_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def search_in_the_linked_list_by_index(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif index < -1:
            raise Exception("Index is less than 0.")
        elif index >= self.length:
            raise Exception("Index is out of bounds.")
        elif index == 0:
            searched_node = self.head
            return searched_node.value, index
        elif index == (self.length - 1) or index == -1:
            searched_node = self.tail
            return searched_node.value, index
        else:
            searched_node, i = self.head, 0
            while i < index:
                searched_node = searched_node.next
                i += 1
            return searched_node.value, i

    def search_in_the_linked_list_by_value(self, value):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("The Linked List is empty.")
        else:
            searched_node, index = self.head, 0
            while searched_node:
                if searched_node.value == value:
                    return searched_node.value, index
                searched_node = searched_node.next
                index += 1
            raise ValueError(f"The Node Value: {value} is not present in the Linked List.")

    def get_node(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif index < -1:
            raise Exception("Index is less than 0.")
        elif index >= self.length:
            raise Exception("Index is out of bounds.")
        elif index == 0:
            fetched_node = self.head
            return fetched_node
        elif index == (self.length - 1) or index < -1:
            fetched_node = self.tail
            return fetched_node
        else:
            fetched_node = self.head
            for _ in range(index):
                fetched_node = fetched_node.next
            return fetched_node

    def set_node(self, index, value):
        node_to_set = self.get_node(index=index)
        if node_to_set:
            node_to_set.value = value

    def delete_from_the_beginning(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_from_the_end(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        return popped_node

    def delete_from_anywhere(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif self.length == 1:
            popped_node = self.head
            self.head = self.tail = None
            self.length -= 1
            return popped_node
        elif index < -1:
            raise Exception("Index is less than 0.")
        elif index >= self.length:
            raise Exception("Index is out of bounds.")
        elif index == 0:
            return self.delete_from_the_beginning()
        elif index == (self.length - 1) or index == -1:
            return self.delete_from_the_end()
        else:
            previous_node = self.get_node(index=(index - 1))
            popped_node = previous_node.next
            previous_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def delete_all_nodes(self):
        self.head = self.tail = None
        self.length = 0


if __name__ == '__main__':
    try:

        single_linked_list = SingleLinkedList()

        single_linked_list.insert_at_the_beginning(value=10)
        single_linked_list.insert_at_the_beginning(value=20)
        single_linked_list.insert_at_the_beginning(value=30)
        single_linked_list.insert_at_the_beginning(value=40)

        single_linked_list.insert_at_the_end(value=50)
        single_linked_list.insert_at_the_end(value=60)
        single_linked_list.insert_at_the_end(value=70)
        single_linked_list.insert_at_the_end(value=80)

        single_linked_list.insert_at_anywhere(index=0, value=90)
        single_linked_list.insert_at_anywhere(index=1, value=100)
        single_linked_list.insert_at_anywhere(index=7, value=110)
        single_linked_list.insert_at_anywhere(index=10, value=120)
        single_linked_list.insert_at_anywhere(index=12, value=130)

        print(single_linked_list)
        print(single_linked_list.traverse_the_linked_list())
        print(single_linked_list.search_in_the_linked_list_by_index(index=6))
        print(single_linked_list.search_in_the_linked_list_by_index(index=0))
        print(single_linked_list.search_in_the_linked_list_by_value(value=40))
        # print(single_linked_list.search_in_the_linked_list_by_value(1340))

        print(single_linked_list.get_node(index=12))
        single_linked_list.set_node(index=12, value=140)
        print(single_linked_list)
        print(single_linked_list.delete_from_the_beginning())
        print(single_linked_list)
        print(single_linked_list.delete_from_the_end())
        print(single_linked_list)
        print(single_linked_list.delete_from_anywhere(index=10))
        print(single_linked_list)
        single_linked_list.delete_all_nodes()
        print(single_linked_list.delete_from_anywhere(index=0))

    except Exception as e:
        print(e.__str__())
