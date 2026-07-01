def timeConversion(s):
    if (s[-2:] == 'AM'):
        if(s[:2] == '12'):
            res='00'+s[2:-2]
        else:
            res=s[:-2]
    else:
        if(s[:2]=='12'):
            res=s[:-2]
        else:
            part1=int(s[:2])+12
            res=str(part1)+s[2:-2]
    return res

s=input("Enter the time in 12 hour format(hh:mm:ssPM or hh:mm:ssAM):")
print(timeConversion(s))