# Board-Game-Card-Deck-Prototyper (BGCDP)
This is a very minimal collection of scripts used to prototype card decks in board games.


# Introduction
Have you ever wanted to make a board game, but the amount of cards you need to make is far too many to create each of them physically? Look no further, as these scripts are perfect for you!


# How To Use
1. Download the example virtual card deck provided.
2. Put all of your cards (whether they be html, pdf, png, etc...) in the reference_deck folder, and delete the placeholders.
3. Navigate to the ```./virtual_card_deck directory.``` IMPORTANT! ONLY RUN THE PYTHON SCRIPTS WHILE IN THIS DIRECTORY! OTHERWISE IT WILL NOT WORK PROPERLY!
4. To draw a card from the cards directory, run:
```py draw.py```
5. To reset the deck, run:
```py refresh.py ```

# Notes
- As previously stated, only run the ```py draw.py``` and the ```py refresh.py``` scripts when in the ```./virtual_card_deck``` directory.
- As of right now, when you draw a card, the directory of the card is shown and then the card is moved to the discard_pile folder. To see the information on the card, you have to go into the discard_pile directory and open the card you just drew. This is hopefully going to be changed in the future.
- I am very inexperienced with python, and cannot guarantee that this will work. Even though it shouldn't damage anything, I am not responsible for any lost data or damaged hardware.
- This was made for a small project I was working on, so I probably will not update it to make it easier or nicer to use for a long time, if at all. 
