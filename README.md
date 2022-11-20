# Proiect `Wordle`
Echipa formată din:

-**Popa Sebastian** (grupa 151)

-**Apostol Alin-Constantin** (grupa 151)

## Descriere
Jocul *„Wordle”* a devenit popular pe **Twitter** la sfârșitul lui decembrie 2021, datorită simplității acestuia precum și unui feature de partajare adăugat de **Josh Wardle** (creatorul jocului), care permite utilizatorilor să-și copieze rezultatele sub forma unei grile de emoji pătrate colorate.

Cum se joacă? Scopul este să ghicești un cuvânt din 5 litere din cât mai puține încercări, numărul maxim fiind 6. O dată introdus un cuvânt valid, primești anumite indicii:

1. Dacă o literă din cuvântul introdus nu apare în cuvântul de ghicit, va fi colorată cu <span style="color:grey"> `gri`</span>.

2. Dacă o literă din cuvântul introdus apare în răspuns, dar nu pe acea poziție, va fi colorată cu <span style="color:#e6e600"> `galben`</span>.

3. Dacă o literă din cuvântul introdus apare în răspuns și pe poziția corespunzătoare, va fi colorată cu <span style="color:green"> `verde`</span>.

Exemplu:![](https://i.guim.co.uk/img/media/b4977654b509967eef77b87c256fa639f0ef807a/65_137_887_532/master/887.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=9c01405913e4ecbfc72818af2bf65132)

Astfel, aplicația pe care am creat-o dispune de mai multe opțiuni, precum: alegerea dificultății (3/6/12/∞ încercări admise), resetarea jocului, dar și un buton de `ajutor` care oferă jucătorului cel mai bun răspuns posibil având în vedere încercările anterioare. Acest cuvânt este determinat folosind entropia lui Shannon.

## Statistici
* sunt 11454 de cuvinte valide ce pot fi răspunsuri

* numărul mediu de încercări per cuvânt obținut este `4,0151` (dacă se folosește doar *helper-ul*)

![](tabel.crtx)

## Prerequisites
* compile `main.cpp` to `main.exe`
* run `GAME.py` and have fun

### for `linux` only, in the `tools.py` file 
*    comment line `36` (ctypes.windll ... )
*    comment line `47` (root.iconbitmap('ico.ico'))


## Extra
* the `_stats.txt` (`solutii.txt`) file was obtained by running `get_stats.cpp` and it describes the sequence produced by the helper for any valid answer
* the `precomputed.txt` file was obtained by running get_precomputed.cpp and it is used to store the second guesses if the first guess was TAREI 


## Referințe:
* [https://en.wikipedia.org/wiki/Wordle](https://en.wikipedia.org/wiki/Wordle)
* [https://www.theguardian.com/games/2021/dec/23/what-is-wordle-the-new-viral-word-game-delighting-the-internet](https://www.theguardian.com/games/2021/dec/23/what-is-wordle-the-new-viral-word-game-delighting-the-internet)
* [https://www.nytimes.com/games/wordle/index.html](https://www.nytimes.com/games/wordle/index.html)
* [https://www.youtube.com/watch?v=v68zYyaEmEA](https://www.youtube.com/watch?v=v68zYyaEmEA)
* [https://www.pythontutorial.net/tkinter/](https://www.pythontutorial.net/tkinter/)
* [https://www.markdownguide.org/getting-started/](https://www.markdownguide.org/getting-started/)