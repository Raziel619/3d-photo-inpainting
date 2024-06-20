import os
import subprocess
import sys
import time

if __name__ == "__main__":
    input_dir = sys.argv[1]
    dirs = [f.path for f in os.scandir(input_dir) if f.is_dir()]

    for x in dirs:
        file_count = len([f for f in os.listdir(x) if os.path.isfile(os.path.join(x, f))])
        if "_ls" in x or file_count > 1:
            continue

        print(f"Processing - {x}")
        start_time = time.time()
        subprocess.run([sys.executable, f"main.py", "--src_folder", x, "--video_folder", x])
        job_time = int(time.time() - start_time)
        print(f"Completed Job in {job_time} seconds")
