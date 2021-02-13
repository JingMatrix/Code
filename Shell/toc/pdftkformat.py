#! python3
import sys


TAB = '\t'
shift = 0
for line in sys.stdin:
    if "d=" in line:
        shift = int(line[2:].strip())
        continue
    level = 1 + line.count(TAB)
    line = line.strip()
    commaIndex = line.rfind(',')
    title = line[:commaIndex]
    try:
        pageNo = int(line[commaIndex + 1:].strip())
    except ValueError:
        print("Page number error at line:" + line, file=sys.stderr)
        continue
    print("BookmarkBegin")
    print("BookmarkTitle:", title.strip())
    print("BookmarkLevel:", level)
    print("BookmarkPageNumber:", pageNo + shift)
