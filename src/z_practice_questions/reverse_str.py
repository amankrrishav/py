# write a reverse string without start,end,step . instead use LOOP

def rev_str(s):
    result = ""
    for char in s:
        result =char +result

    return result

print(rev_str("amankumar"))        