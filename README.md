
# **Hangman**

Hangman is a Python based game which is deployed on Heroku. 

Link to live site: [here](https://hangman-assignment3.herokuapp.com/)
 
  ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665699779/Hangman/Landing_page_sqmc1e.png)
  
Github Repository -> https://github.com/vanyasahay/hangman-assignment3
 

## **How to Play**
 
- This is version of the classic letter guessing game called Hangman.
- You are shown a set of blank letters that match a word or phrase and you have to guess what these letters are to reveal the hidden word. 
- You guess by picking letters from those displayed on the sides. If you pick a letter that is in the word, letter is revealed from the blank letters; however, if you pick a letter that is not in the word, then a stickman is slowly drawn. 
- With each wrong letter guess, the man is drawn more and more. 
- When the man is finished, he is hung and the game is lost. This is why the game is called 'Hangman'. 
- If you can reveal all the letters in the word before the man is hung then you are successful and the full word is revealed.
- Players can preess 'ENTER' to play again
 
  
**Target Audience:**

Players of all ages are welcome.. 

 
##  **Features**

Existing Features

 Intro. 

 The user is welcomed to the game.

   ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665699779/Hangman/Landing_page_sqmc1e.png)

 Option to read rules: 

 Player is displayed rules of the game and then game will start after 5 seconds.
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707246/Hangman/rules_y9fuln.png)

 A message will displayed to start the game and Player can start by pressing ENTER.
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665708048/Hangman/startGame_oh2upe.png)
 


 Stages of man hangning:

 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/1_leppxj.png)
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/2_evggux.png)
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/3_mnka9l.png)
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/4_qwdniu.png)
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/5_j1l3m5.png)
 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/6_mucbkg.png)

 
 Game win - follows the story

  ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665699779/Hangman/won_tvpzkp.png)

 Loose Game 

  ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665699779/Hangman/lost_ii2gt7.png)

 Option to play again: Yes

  ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665700148/Hangman/PlayAgain_cuqyqn.png)

 Invalid Entry:

 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665699779/Hangman/invalid_ufosia.png)

Already Used Letter

 ![This is an image](https://res.cloudinary.com/dk2fqntmr/image/upload/v1665707694/Hangman/4_qwdniu.png)

Future Features

* Create Username
* Multiplayer game
* Show valid letters


## TECHNOLOGIES USED: 

Python

## **Testing**

- When the Player win then winning message is shown with the word.
- When the player lost, then messahe is displayed with complete word.
- Validation message is thrown when invalid entry is made.
- Message is displayed when used letters are pressed again.


## Bugs

 - Play again was not working as expected. So did a minor change to make this work.
 - Hangman diagram stages were up side down so made correction.
 - Validation message was not thrown when an invalid entry was made.

# Validator testing

 - Pep 8 no longer running. So used code level instruction for validation. 
 - Built into Code Institute template. Add-ons allow for error checking.
 - There are some errors showing but ignored as code is working fine.

## **Code Deployment from Github to Heroku**

 - Clone this repository - gh repo clone vanyasahay/hangman-assignment3
 - Create account on Heroku 
 - If your using a creds.json file then go to Heroku settings and click "reveal config vars".
 - In key type CREDS and in value paste your whole creds.json file text.
 - Again if you don't need to use creds.json file then skip to next step.
 - Set the buildbacks to Python and NodeJS in that order
 - Link the Heroku app to the repository
 - Click Manual/Automatic deploy.

## **Credits**

> * 'Welcome to Hangman ASCII letters- https://patorjk.com/software/taag/#p=display&v=0&f=Alphabet&t=%20%20WELCOME%0A%20%20%20%20to%20%0AH%20A%20N%20G%20M%20A%20N
> * Hangman Diagram - https://codegolf.stackexchange.com/questions/135936/ascii-hangman-in-progress
> * GITHUB part used for words collection - https://github.com/edlavairee/hangman-game/blob/master/words.txt 
> * Rules are referred from here  - https://www.gamestolearnenglish.com/hangman/

## RESOURCES USED:

* Stack Overflow
* Google
* W3 Schools
* Tutor support from Code Institute
* YouTube
* Github Projects

---
