import re

txt_array_list = []
tmp_sentences = []
front_paragraph_idx = -1
front_theory_idx = -1
file_path = 'sample.txt'
theory_flag = False

with open(file_path, 'r') as f:
    for s_line in f:
        res = re.match('.+\d.\d 第.+章.+節', s_line)
        if res:
            if not theory_flag:
                txt_array_list[front_paragraph_idx].append([])

            theory_flag = True

            txt_array_list[front_paragraph_idx][1].append([s_line.strip()])

            if not front_theory_idx == -1:
                txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

            tmp_sentences = []
            front_theory_idx += 1
            continue

        res = re.match('\d. 第.+章', s_line)
        if res:
            txt_array_list.append([s_line.strip()])

            if theory_flag == True \
                and not front_theory_idx == -1:
                txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

            if not theory_flag == True \
                and not front_paragraph_idx == -1:
                txt_array_list[front_paragraph_idx].append(tmp_sentences)

            tmp_sentences = []
            front_paragraph_idx += 1
            front_theory_idx = -1
            theory_flag = False
            continue

        tmp_sentences.append(s_line.strip())

if theory_flag == True \
    and not front_theory_idx == -1:
    txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

if not theory_flag == True \
    and not front_paragraph_idx == -1:
    txt_array_list[front_paragraph_idx].append(tmp_sentences)

# print(txt_array_list)
