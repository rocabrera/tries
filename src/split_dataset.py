from pathlib import Path

DATASET_FILENAME = "words_alpha.txt"
DATA_PATH = Path(__file__).parent.parent / "data"
DATASET_PATH = DATA_PATH / DATASET_FILENAME
DATASET_SIZE = 370105
MAX_SAMPLES_PER_SIZE = 50000
NUMBER_OF_FILES = (DATASET_SIZE//MAX_SAMPLES_PER_SIZE) + 1

count = 0
file_number = 1

with open(DATASET_PATH, "r") as d_file:


    s_file = open(DATA_PATH / "words_splited" /f"file_{file_number}.txt", "w")
    for _ in range(DATASET_SIZE):
        d_line = d_file.readline()
        s_file.write(d_line)
        
        if count == MAX_SAMPLES_PER_SIZE - 1:
            count = 0
            s_file.close()
            file_number += 1
            s_file = open(DATA_PATH / "words_splited" /f"file_{file_number}.txt", "w")

        count += 1
