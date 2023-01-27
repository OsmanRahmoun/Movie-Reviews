# Project 4 - Movie Review Sentiment Analysis App
# Osman Rahmoun, 10/15/2022, CS 111, Fall Semester


# This void function prints out the menu.
def display_menu(isFirstTime):
  if isFirstTime == True:
    print("Welcome to the Movie Review Sentiment Analysis App!")
    print("1. Load word list file.")
    print("2. Load movie review file.")
    print("3. Get average score of a word.")
    print("4. Get average scores for a list of words.")
    print("5. Plot average scores for a list of words.")


# This function reads in a file of words.  Each word in the file gets stored as an item in a list, which is returned.
def make_list(file_name):
    file = open(file_name)
    lines = file.readlines()
    new_lines = []
    for x in lines:
        if x == lines[-1]:
            new_lines.append(x)
        else:
            x = x[0:-1]
            new_lines.append(x)
    file.close()
    return new_lines


# This function reads in a file of movie reviews.  Each review and associated score are stored as a key/value pair (respectively) in a dictionary, which is returned.
def make_dict(file_name):
    file = open(file_name)
    lines = file.readlines()
    dictionary= {}
    scores_list= []
    review_list=[]
    for sentence in lines:
      score = int(sentence[0])
      scores_list.append(score)
      review = sentence[2:]
      review_list.append(review)
    for i in range(0,len(review_list)):
      dictionary[review_list[i]] = scores_list[i]
    file.close()
    return(dictionary)


# This function searches the dictionary for wordToFind, counts instances of wordToFind, and calculates the average score.  The word search is case insensitive, however, search is looking for full match not partial match.
def search_word(dict, wordToFind):
  count = 0
  sum = 0
  for sentence in dict.keys():
    for words in sentence.split():
      if words.lower() == wordToFind.lower() or words.capitalize() == wordToFind.capitalize():
        count += 1
        sum += dict[sentence]
  
  if count == 0:
    average = 0
  else:
    average = sum / count

  return count,average


# This function is similar to search_word, except instead of searching for a single word, it searches for a list of words stored in list.
def search_all_words(list, dict):
  list_scores = []
  final_list = []
  num = 0
  for x in list:
    list_scores += (search_word(dict,x))
    num += 1
  list_scores = list_scores[1::2]
  total = sum(list_scores)
  avg_score = total / num
  return list_scores, avg_score

# This void function displays the words (stored in list) and their associated scores (stored in list_scores) to screen
def print_lists(list, list_scores):
  list_of_words = []
  list_of_scores = []
  i = 0
  
  while(i < len(list)):
    print(list[i]+": "+str(list_scores[i]))
    i += 1

# This is the main code.  It calls all the functions above. It sets up the interaction with the user.
if __name__ == '__main__':
  display_menu(True)
  answer = int(input("Enter a number (0 to exit): "))
  while answer != 0:
    if answer == 1:
      word_list = input("Enter word list filename: ")
      list = make_list(word_list)
      print("Word list is loaded.")
      display_menu(True)
      answer = int(input("Enter a number (0 to exit): "))
    elif answer == 2:
      dict_list = input("Enter movie review filename: ")
      dict = make_dict(dict_list)
      print("Movie reviews are loaded.")
      display_menu(True)
      answer = int(input("Enter a number (0 to exit): "))
    elif answer == 3:
      specific_word = input("Enter word to search: ")
      count,average = search_word(dict, specific_word)
      print(specific_word,"appears",count,"times")
      print("The average score for the reviews containing the word",specific_word,"is:")
      print(average)
      display_menu(True)
      answer = int(input("Enter a number (0 to exit): "))
    elif answer == 4:
      list_scores, avg_score = search_all_words(list, dict)
      print_lists(list, list_scores)
      print("Average score all of words: " + str(avg_score) + " which means this text is ", end="")
      if avg_score >= 2:
        print("positive")
      else:
        print("negative")
      display_menu(True)
      answer = int(input("Enter a number (0 to exit): "))
    else:
      display_menu(True)
      answer = int(input("Enter a number (0 to exit): "))
