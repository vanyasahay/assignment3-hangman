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

WORDS = ['abruptly','absurd','awkward','blizzard','bookworm','buffoon','croquet','daiquiri','galvanize','glowworm','microwave',
    'lengths','keyhole','nightclub','syndrome','twelfth','vaporize','triphthong','zigzagging','whiskey','waltz']
secretWord = random.choice(WORDS)

wordLength = len(secretWord)

endGame = False
attempts = 6


def hangman():
    secretWord = random.choice(WORDS)
    secretWordUpperCase = secretWord.upper()
    correctLetter = []
    blanks = len(secretWord) * '_'
    print('\n')
    print(f'This is the Secret word: {blanks}')
    print(f'{hangman_stages[0]}\n')
    
    blanks = list(blanks)
    maxLife = len(hangman_stages) - 1
    lifeUsed = maxLife

    while lifeUsed > 0:
        letter = input('\nEnter a letter between A-Z: ').upper()

        if len(letter) != 1 or not letter.isalpha():
            print('The value entered is not valid.')
            print('\n')
           
        elif letter in correctLetter:
            print('This letter has already been used. Enter other valid letter between A-Z.\n')
           
        elif letter in secretWordUpperCase:
            for j, char in enumerate(secretWordUpperCase):
                if char == letter:
                    blanks[j] = letter
            correctLetter.append(letter)
            print(''.join(blanks))
           
        else:
            correctLetter.append(letter)
            lifeUsed -= 1
            print(f'You lost a life. You have {lifeUsed} attempts left.')
            print(f'{hangman_stages[maxLife - lifeUsed]}')
            print('\n')
            

        if ''.join(blanks) == secretWordUpperCase:
            print(f'Yaaaaayyy....You won. You saved a man from death by guessing: {secretWord}.')
            break
    else:
        print(f'We have lost a good man. The secret word was: {secretWord}.')

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
print('Try to save the man in 6 attempts!')
time.sleep(1)
hangman()