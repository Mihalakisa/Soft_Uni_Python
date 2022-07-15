def start_spring(**kwargs):
    new_dict = {}
    # result = []
    for key, value in kwargs.items():
        if value not in new_dict.keys():
            new_dict[value] = []
        new_dict[value].append(key)

    # for key in sorted(new_dict.keys(), key=lambda x: (-len(x[1]), x[0])):
    #     result.append(f"{key}:")
    #     for value in sorted(new_dict[key]):
    #         result.append(f"-{value}")
    # return "\n".join(result)
    sorted_items = sorted(new_dict.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in sorted_items:
        result += f"{key}:" + '\n' '-'
        sorted_values = sorted(value)
        result += '\n''-'.join(sorted_values) + '\n'

    return result.strip()

# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower"}
#
#
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))