file = open('for_task_06.txt', 'r')
amount = []
new_dict = {}
subj = ''
ind = 0

with file:
    for data in file:
        amount = data.split(' ')
        subj = amount[0]
        subj = subj[:len(subj) - 1]
        summary = []

        for i in range(1, len(amount)):
            digit = ''

            for j in amount[i]:
                if '0' <= j <= '9':
                    digit += j

            if digit != '':
                summary.append(int(digit))

        ind = sum(summary)
        new_dict[subj] = ind

file.close()

with open('for_task_06_new.txt', 'w') as writing_file:
    writing_file.writelines(str(new_dict))
