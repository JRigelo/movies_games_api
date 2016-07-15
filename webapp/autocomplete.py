import unidecode
import re
class MyCompleter(object):

   def __init__(self, options):
       self.dict = options
       self.options = sorted(set(options))
       self.options = [(re.sub('[^a-z0-9]+', '', x.lower()), x) for x in self.options]

   def complete(self, text):
       results = []
       if text:
           text = re.sub('[^a-z0-9]+', '', text.lower())
           self.matches = [unidecode.unidecode(s[1]) for s in self.options
                              if text in s[0]]
       else:
           self.matches = self.options[:]
       print self.matches

       for k,v in self.dict.iteritems():
           for match in self.matches:
               if match == k and match not in results:
                   print match
                   results.append((match, v))

       return results

if __name__ =='__main__':
    names_dict = {'Spider man':123, 'Truman Show':124}
    completer = MyCompleter(names_dict)

    which_movie = completer.complete('sp')
    print 'which_movie:', which_movie
