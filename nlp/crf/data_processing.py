def feature_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_new = []
    for d in data:
        data_new.append(eval(d)[1])

    label_new = []
    for d in data:
        label_new.append(eval(d)[2])

    feature_vector = []
    for data in data_new:
        sentence_vector = []
        for sentence in data:
            sentence_vector.append(list(map(str, sentence)))

        feature_vector.append(sentence_vector)

    return feature_vector, label_new


if __name__ == "__main__":
    # print(feature_data('../../data/crf_data.txt'))
    feature_data('../../data/crf_data.txt')