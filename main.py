import os
import sys
import datetime

args = sys.argv

if __name__ == "__main__":
    if len(args) > 0:
        src_path = args[1]
        if os.path.isfile(src_path):
            with open(src_path + ".srt", "x") as w:
                lines = open(src_path, "r")
                index = 1
                dt = datetime.datetime.now()
                dt = dt.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
                for line in lines:
                    result = line.replace(b'\\ufeff'.decode("unicode-escape"), "").replace(b'\\u305a\\u3093\\u3060\\u3082\\u3093(\\u30ce\\u30fc\\u30de\\u30eb),'.decode("unicode-escape"), "")
                    if len(result) > 0:
                        print(index, dt, result)
                        text = f'{dt:%X,%f}'[:-3]
                        text = text + " --> "
                        add = int(len(result) / 6.25)
                        print(add)
                        if (dt.second + add > 59):
                            dt = dt.replace(minute = dt.minute + 1)
                            dt = dt.replace(second = dt.second + add - 60)
                        else:
                            dt = dt.replace(second = dt.second + add)
                        text = text + f'{dt:%X,%f}'[:-3]
                        if (index > 1):
                            w.write("\n\n")
                        w.write(str(index) + "\n")
                        w.write(text + "\n")
                        w.write(result)
                        index = index + 1
                lines.close()
                w.close()