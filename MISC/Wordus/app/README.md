![Guemjamme](https://user-images.githubusercontent.com/44942598/121183900-d6be1b80-c864-11eb-9491-651835ae6d04.png)

Guemjamme 2021 takes place here and now!

# Installation

This project requires NodeJS (with NPM installed).
For the first installation, you need to execute ``npm install`` in order to install the NPM modules used in the project.

After editing the JavaScript files, (client/game.js, client/index.js, client/join.js) you need to use Borwserify to bundle those.
In order to do that, you need to execute ``browserify input-file -o output-file``, where ``input-file`` is to be replaced by each JavaScript file contained in the ``js/client/`` folder (the output file name is the same as the original name, with "_bundle" added as a suffix, in the same folder).

> EX : Editing js/client/game.js  
> ``browserify js/client/game.js -o js/cient/game_bundle.js``

# About Game

Play the game here https://wordus.xyz

The concept of this game is to type as fast as possible and as many **Latin** / **French** / **English** words as possible in the time allotted at the beginning of the game.

During the game the words are chosen randomly from a bank of **2600 Latin words**, **68000 English words**, **320000 French words**.  

If a word is well written it will bring back points once the key ``ENTER`` is pressed but for that you will have to be the **fastest** to type it.  

The number of players per game is limited to 6 in order to keep the game simple and easy on the eyes.  

You will be able to choose to give yourself time by putting up to **3 minutes** or on the contrary to test your capacity to type on computer by giving you only **30 seconds**.  

You can also change the number of words that appear on the screen at the beginning of the game **between 1 to 8**.  

We recommend that you set a small number of words if you have a lot of players.  

If you are not convinced of the preferences you can change them at the end of the game before starting a new one.

In case of bug or error please contact by discord ``Hokanosekai#0001``.

