import re

def _remov_hashtag(input_string):
  no_hastag_string = re.sub(r'#[\w]+','',input_string)
  return no_hastag_string

if __name__ == '__main__':
    user_input = raw_input("Text input: ")
    new_string = _remov_hashtag(user_input)
    if len(new_string) < len(user_input):
        print('No hastags!')
    print(new_string)
