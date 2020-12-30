def get_freq(text):
   res = {}
   for letter in text:
      if(letter not in res):
         res[letter] = 0
      res[letter] += 1
   return res

res = get_freq("hello world!")
print(res)