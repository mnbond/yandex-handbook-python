def to_string(*elements, sep=" ", end="\n"):
    return sep.join(map(str, elements)) + end
