import random
import time

hangman_stages = ['''
BYE BYE- TAKE CARE!
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
YOU ARE THE BEST - LAST CHANGE
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
I BELIEVE IN YOU - 2 MORE
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
YOU CAN DO THIS - 3 MORE
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
STILL HOPING- 4 MORE TURNS
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
YOU CAN SAVE ME- 5 TURNS TO GO
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
SAVE ME PLEASE- YOU HAVE 6 LIFELINES
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

WORDS = ['abruptly','absurd','awkward','blizzard','bookworm','buffoon','croquet','daiquiri','galvanize','glowworm','microwave',
    'lengths','keyhole','nightclub','syndrome','twelfth','vaporize','triphthong','zigzagging','whiskey','waltz']
secretWord = random.choice(WORDS)

word_length = len(secretWord)

end_of_game = False
lives = 6


def hangman():

print('''
 **      **           **           ****     **         ********        ****     ****           **           ****     **
/**     /**          ****         /**/**   /**        **//////**      /**/**   **/**          ****         /**/**   /**
/**     /**         **//**        /**//**  /**       **      //       /**//** ** /**         **//**        /**//**  /**
/**********        **  //**       /** //** /**      /**               /** //***  /**        **  //**       /** //** /**
/**//////**       **********      /**  //**/**      /**    *****      /**  //*   /**       **********      /**  //**/**
/**     /**      /**//////**      /**   //****      //**  ////**      /**   /    /**      /**//////**      /**   //****
/**     /**      /**     /**      /**    //***       //********       /**        /**      /**     /**      /**    //***
//      //       //      //       //      ///         ////////        //         //       //      //       //      /// 
''')

print('Welcome to HANGMAN game')
name= input('Please Enter Your Name: ')
print('Welcome ' + name + ' !')
print('Try to save the man in 7 attempts!')
time.sleep(1)
hangman()