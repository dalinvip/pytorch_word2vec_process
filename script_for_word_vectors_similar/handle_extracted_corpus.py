
# @Author : bamtercelboo
# @Datetime : 2018/1/24 9:23
# @File : handle_extracted_corpus.py
# @Last Modify Time : 2018/1/24 9:23
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  handle_extracted_corpus.py
    FUNCTION : None
"""

import os
import sys
import linecache


def handle_extracted_corpus(path_extracted_corpus=None, path_extracted_corpus_handled=None):
    if os.path.exists(path_extracted_corpus_handled):
        os.remove(path_extracted_corpus_handled)
    file = open(path_extracted_corpus_handled, encoding="UTF-8", mode="w")

    with open(path_extracted_corpus, encoding="UTF-8") as f:
        now_line = 0
        word_dict = {}
        for line in f:
            now_line += 1
            sys.stdout.write("\rHandling with the {} line.".format(now_line))
            line = line.strip().split(" ")
            if line[0] not in word_dict:
                window_dict = {}
                for i in range(0, len(line[2:]), 2):
                    if line[i + 2] not in window_dict:
                        window_dict[line[i + 2]] = int(line[i + 3])
                    else:
                        window_dict[line[i + 2]] += int(line[i + 3])
                word_dict[line[0]] = window_dict
            else:
                for i in range(0, len(line[2:]), 2):
                    if line[i + 2] not in word_dict[line[0]]:
                        word_dict[line[0]][line[i + 2]] = int(line[i + 3])
                    else:
                        word_dict[line[0]][line[i + 2]] += int(line[i + 3])
    print("writing file......")
    now_word = 0
    all_word = len(word_dict)
    for k, v in word_dict.items():
        now_word += 1
        sys.stdout.write("\rHandling with the {} word, all {} words.".format(now_word, all_word))
        file.write(k + " " + str(v["count"]))
        for kv, vv in v.items():
            file.write(" " + kv + " " + str(vv))
        file.write("\n")
    print("Handle Finished")
    f.close()
    file.close()


def handle_extracted_corpus_smallmem(path_extracted_corpus=None, path_extracted_corpus_handled=None):
    if os.path.exists(path_extracted_corpus_handled):
        os.remove(path_extracted_corpus_handled)
    file = open(path_extracted_corpus_handled, encoding="UTF-8", mode="w")

    with open(path_extracted_corpus, encoding="UTF-8") as f:
        now_line = 0
        word_dict = {}
        for line in f:
            now_line += 1
            sys.stdout.write("\rHandling with the {} line.".format(now_line))
            line = line.strip().split(" ")
            if line[0] not in word_dict:
                window_dict = {}
                for i in range(0, len(line[2:]), 2):
                    if line[i + 2] not in window_dict:
                        window_dict[line[i + 2]] = int(line[i + 3])
                    else:
                        window_dict[line[i + 2]] += int(line[i + 3])
                word_dict[line[0]] = window_dict
            else:
                for i in range(0, len(line[2:]), 2):
                    if line[i + 2] not in word_dict[line[0]]:
                        word_dict[line[0]][line[i + 2]] = int(line[i + 3])
                    else:
                        word_dict[line[0]][line[i + 2]] += int(line[i + 3])

    for k, v in word_dict.items():
        file.write(k + " " + str(v["count"]))
        for kv, vv in v.items():
            file.write(" " + kv + " " + str(vv))
        file.write("\n")

    f.close()
    file.close()


if __name__ == "__main__":
    # path_data = "./Data/fullVocab.txt"
    # path_extracted_corpus = "./Embedding/enwiki-20150112_text_context_ngram_allcorpus_stastic_similar_small.txt"
    # path_extracted_corpus_handled = "./Embedding/enwiki-20150112_text_handled_stastic_small_extracted_handled.txt"

    path_extracted_corpus = "./Embedding/enwiki-20150112_text_context_ngram_allcorpus_stastic_similar_small.txt"
    path_extracted_corpus_handled = "./Embedding/enwiki-20150112_text_handled_stastic_small_extracted_handled.txt"

    # handle_extracted_corpus(path_extracted_corpus=path_extracted_corpus, path_extracted_corpus_handled=path_extracted_corpus_handled)
    handle_extracted_corpus(path_extracted_corpus=path_extracted_corpus, path_extracted_corpus_handled=path_extracted_corpus_handled)
