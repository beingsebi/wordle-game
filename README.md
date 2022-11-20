# Prerequisites
* compile main.cpp to main.exe
* run GAME.py and have fun

### for linux only, in the tools.py file 
*    comment line 36 (ctypes.windll ... )
*    comment line 47 (root.iconbitmap('ico.ico'))

# Statistics
* 11454 possible answers
* 4.0103 average guesses if played only using the helper
* 1 guess - 1 word
* 2 guesses - 43 words
* 3 guesses - 2509 words
* 4 guesses - 6512 words
* 5 guesses - 2080 words
* 6 guesses - 291 words
* 7 guesses - 18 words
* more details in _stats.txt

#Extra
* the `_stats.txt` file was obtained by running `get_stats.cpp` and it describes the sequence produced by the helper for any valid answer
* the `precomputed.txt` file was obtained by running get_precomputed.cpp and it is used to store the second guesses if the first guess was TAREI 