#endocing=utf-8
import pickle
import time


def tagging_query(query, seg_list, ac_trie):
    # tagging思路：分词结果和ac_trie匹配结果的融合
    s = time.time()
    #seg_list = jieba.cut(query)
    #seg_list = list(seg_list)
    seg_pos = []

    if len(seg_list) > 0:
        begin = 0
        for i in range(0, len(seg_list)):
            end = begin + len(seg_list[i])
            seg_pos.append((begin, end))
            begin = end

    entity_pos = parse_string(query, ac_trie)
    merge_result = {}

    if len(seg_list) > 0:
        s_end = 0
        s_begin = 0
        i = 0
        while i < len(seg_pos):
            s_begin, s_end = seg_pos[i]
            max_j = i
            for j in range(i, len(seg_pos)):
                _, s_j_end = seg_pos[j]
                if (s_begin, s_j_end) in entity_pos:
                    s_end = s_j_end
                    max_j = j
            if (s_begin, s_end) in entity_pos:
                merge_result[(s_begin, s_end)] = entity_pos[(s_begin, s_end)]
            i = max_j + 1
    else:
        merge_result = entity_pos

    return merge_result

def parse_string(s, ac_trie):
    '''
     对s:string进行实体词匹配
    '''
    result = {}
    for end_index, x in ac_trie.iter(s):
        #print(x)
        key, value = x
        end_index = end_index + 1
        start_index = end_index - len(key)
        result[(start_index, end_index)] = value
        #print query[start_index:end_index], start_index, end_index, value
    return result

def file_parsing(filepath, outputpath, ac_trie):
    writer = open(outputpath, "w", encoding="utf-8")
    for line in open(filepath, "r", encoding="utf-8"):
        line = line.strip().split("\t")
        query = line[0]
        seg_list = line[1].split(" ")
        result_list = tagging_query(query, seg_list, ac_trie)
        result_str = ""
        for s, e in result_list:
            result_str += query[s:e] + "," + str(s) + "-" + str(e) + "," + result_list[(s, e)] + ":::"
        if result_list:
            writer.write(query + "\t" + " ".join(seg_list) + "\t" + result_str + "\n")
    writer.close()

if __name__ == "__main__":
    ac_trie = pickle.load(open("./data/index/company_index.pkl", "rb"))
    file_parsing("./data/clean_data/sentences_technews.txt", "./data/ner_result/technews_tagging.txt", ac_trie)
