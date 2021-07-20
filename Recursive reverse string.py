def rev(s,i):
  length = len(s) -1
  base = len(s) // 2
  if(i<base):
      s[i], s[length-i] = s[length-i], s[i]
      i += 1
      rev(s,i)
  return(s)
s = rev(s,0)
return(s)
