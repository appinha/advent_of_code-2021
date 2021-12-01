import itertools

def is_int(object):
    return (isinstance(object, int))

def is_float(object):
    return (isinstance(object, float))

def is_number(object):
    return is_int(object) or is_float(object)

def is_str(object):
    return (isinstance(object, str))

def is_list(object):
    return (isinstance(object, list))

def is_dict(object):
    return (isinstance(object, dict))

def str_to_int(object):
    if object.isdigit():
        return int(object)
    else:
        return object

def groupby(object):
    return [
        {"element": k, "occurrences": list(v)}
        for k, v in itertools.groupby(object)
    ]

def get_unique_permutations(elements):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations
