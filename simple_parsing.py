import re
def is_speakable(text):
      return re.match(r'^(pi|ka|chu)*$', text) is not None
if __name__ == '__main__':
   text_input = input('Enter text: ')
   print(is_speakable(text_input))