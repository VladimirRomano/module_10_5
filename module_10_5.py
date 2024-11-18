from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            file.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
start = datetime.now()
for f in filenames:
    read_info(f)
finish = datetime.now()
result = finish - start
print(result)
# Многопроцессный
# if __name__ == '__main__':
#     start_ = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     finish_ = datetime.now()
#     result_ = finish_ - start_
#     print(result_)

