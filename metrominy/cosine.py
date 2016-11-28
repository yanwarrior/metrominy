from math import sqrt


def cosine_similarity(data_weighting_docs={}, data_weighting_query={}):
    result = {}
    for key, value in data_weighting_docs.items():
        dot_product = zip(value.values(), data_weighting_query.values())
        # dot_product = [reduce(lambda x,y: x*y, i) for i in dot_product]
        dot_product = map(lambda t: t[0] * t[1], dot_product)
        dot_product = sum(dot_product)

        length_doc = map(lambda x: x ** 2, value.values())
        length_doc = sum(length_doc)
        length_doc = sqrt(length_doc)

        length_query = map(lambda x: x ** 2, data_weighting_query.values())
        length_query = sum(length_query)
        length_query = sqrt(length_query)

        try:
            result[key] = dot_product / (length_query * length_doc)
        except:
            result[key] = 0.0

    return {k:v for k, v in result.items() if v > 0}