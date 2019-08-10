MS=input()
 
if((MS>='a' and MS<='z') or (MS>='A' and MS<='Z')):
  if(MS=='a' or MS=='A' or MS=='e' or MS=='E' or MS=='i' or MS=='I' or MS=='o' or MS=='O' or MS=='u' or MS=='U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
