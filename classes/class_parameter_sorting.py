

class ClassName:
    """Class for sorting function testing"""

    def __init__(self, attribute_1, attribute_2, attribute_3=1):
        """Constructor"""
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
        self.attribute_3 = attribute_3

    def get_all_info(self):
        """Returns all parameters of the class"""

        all_info = f'Attribute_1 = {self.attribute_1}; Attribute_2 = {self.attribute_2}, ' \
                   f'Attribute_3 = {self.attribute_3}.'
        return all_info


def sort_class_attributes(*args):  # gets multiple parameters --> use class objects as parameters

    sorted_list_of_argument = sorted(args, key=lambda x: x.attribute_1)  # create a list of sorted objects parameters
    result = sorted_list_of_argument[0].attribute_1
    return result


# obj_1 = ClassName('Aa', 'Bb')
# obj_2 = ClassName('Zz', 'Yy')
#
# print(sort_class_attributes(obj_1, obj_2))
