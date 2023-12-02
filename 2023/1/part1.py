import sys 
filename = sys.argv[1]
def extract_calibration_value(word):
    # LTR first num
    val = ""
    for w in word:
        if 48<=ord(w)<=57:
            val +=w
            break
    # RTL first num
    for w in word[::-1]:
        if 48<=ord(w)<=57:
            val +=w
            break
    return int(val)
ans=0
with open(filename,'r') as doc:
    lines = doc.read().split("\n")
    for line in lines:
        ans+=extract_calibration_value(line)
print(ans)
