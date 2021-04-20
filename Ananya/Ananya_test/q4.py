# 4 Code for Cause operations

x = int(input())
seq = []
def operation(s, seq):
    if(s[0] == "E"):
        course = int(s[1])
        roll = int(s[2])
        if(seq == []):
            seq.append((course, roll))
        else:
            i = 0
            while(i!=len(seq)):
                if(seq[i][0] == course):
                    break
                i += 1
            if(i < len(seq)-1):
                seq = seq[:i+1] + [(course, roll)] + seq[i+1:]
            else:
                seq.append((course, roll))
    else:
        print(seq.pop(0))
    
    return seq
            
for _ in range(x):
    seq = operation(input(), seq)