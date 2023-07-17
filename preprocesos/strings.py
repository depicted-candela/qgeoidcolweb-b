def subset_string(string):
    start_index = string.index('/') + 1
    end_index = string.index('.')
    subset = string[start_index:end_index]
    return subset