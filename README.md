```
______                 ______         _ 
|  _  \                | ___ \       | |
| | | |___  ___ _ __   | |_/ /___  __| |
| | | / _ \/ _ \ '_ \  |    // _ \/ _` |
| |/ /  __/  __/ |_) | | |\ \  __/ (_| |
|___/ \___|\___| .__/  \_| \_\___|\__,_|
               | |                      
               |_|                      
```

## Motivation
I watched a [documentary](https://youtu.be/HwF229U2ba8?si=L6WkXVUR3lsA2p53) on IBMs Deep Blue and was inspired to create a simple chess computer engine.

## Evaluation
Utlilizing [Claude E. Shannon's](https://en.wikipedia.org/wiki/Claude_Shannon#Shannon's_computer_chess_program) approach to using the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves) to evaluate positions.

Goal is to explore available moves at a depth of 3-5.

## Stretch Goals

- Implement server functions so that it can intereact with another player/computer using [Universal Chess Interface]() Protocol. Will most likely use Flask.
- UI
- Game log and evaluation

## Resources
[Programming a Computer for Playing Chess by Claude E Shannon](https://www.pi.infn.it/~carosi/chess/shannon.txt)




