def Reverse_iter(s,out=""):
     if len(s)==len(out):
         print(out)
         return out
     else:
         out= s[len(out)]+out
         i=len(out)
         out = Reverse_iter(s,out)
         return out
Reverse_iter("ABC")


def Reverse_iter2(s,out=""):
     if len(s)==len(out):
         print(out)
         return out
     else:
         out= s[len(out)]+out
         i=len(out)
         out = Reverse_iter(s,out)
         return out
Reverse_iter2("ABC")
