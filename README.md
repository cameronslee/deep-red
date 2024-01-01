```
 ____  ____  ____  ____    ____  ____  ____  
(  _ \( ___)( ___)(  _ \  (  _ \( ___)(  _ \ 
 )(_) ))__)  )__)  )___/   )   / )__)  )(_) )
(____/(____)(____)(__)    (_)\_)(____)(____/ 
```

## Motivation
I watched a [documentary](https://youtu.be/HwF229U2ba8?si=L6WkXVUR3lsA2p53) on IBMs Deep Blue and was inspired to create a simple chess computer engine.

## Evaluation
Utlilizing [Claude E. Shannon's](https://en.wikipedia.org/wiki/Claude_Shannon#Shannon's_computer_chess_program) approach to using the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves) to evaluate positions.

Evaluation function will explore available moves at a depth of 3-5. 

## Resources
[Programming a Computer for Playing Chess by Claude E Shannon](https://www.pi.infn.it/~carosi/chess/shannon.txt)


## Further Development Plans
Create a server for users to play against the engine and have their games serve as the training data for the model
to improve. 

In the beginning, trained on no data. Just a simple evaluation function. Will grow as the user base increases.

The goal is not to have the strongest engine but merely an engine that grows with the user base

Essentially, the model will grow based upon the users on the leaderboard

Snapshots of the models strength will be taken to rate its the [ELO](https://en.wikipedia.org/wiki/Elo_rating_system)

### TODO
- Evaluation function needs to be tuned and minmax function needs to be tuned
- Implement server functions so that it can intereact with another player/computer using [Universal Chess Interface]() Protocol. Will most likely use Flask.
- UI
- Game log and evaluation. This pipeline includes:
    - Logging game data from userbase and training a neural net to serve as the evaluation for the engine
