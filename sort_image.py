import os
import fnmatch


def sort_by_name(path, category_list):
    categories = {}
    for category in category_list:
        categories[str(category)] = []
    image_names = os.listdir(path)
    keys = list(categories.keys())
    for i in keys:
        for filename in image_names:
            if fnmatch.fnmatch(filename, i + '*'):
                categories.setdefault(i, []).append(filename)
    for category in categories:
        categories.setdefault(category, []).sort()
    return categories
