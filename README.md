# eecs-203-logic-game
 
# Introduction
 EECS 203 Winter 203 introduced a logic puzzle in Groupwork 2. The homework described the game as follows:
>You are observing Grace, the former 203 GSI, giving two IAs a logical test to prepare 
them for the upcoming semester. The conversation proceeds as follows:
>
>* Grace: "I am giving you each a slip of paper with a non-negative integer on it."
>* Abigail looks down at her paper and sees 6.
>* Emma looks down at her paper and sees 4.
>
>Grace tells them that their numbers sum to either 8 or 10, but does not tell them which. 
>It is Abigail and Emma's job to figure out whether their numbers sum to 8, or whether 
they sum to 10, without looking at each other's papers.
Grace asks each of them, alternating back and forth, starting with Abigail, if the sum of 
the numbers is 8 or if the sum of the numbers is 10. They can either pass, or 
guess. If either guess correctly, they succeed; otherwise, they fail.

In solving this problem, Nolan and I developed a strategy that allows the players to win every time (see Piazza for an explanation of what we came up with). To allow for easier use of the strategy when testing, we also developed a script that does all the "thinking" for each player. We thought we'd share this script with the class to use to play along, as it does feel pretty "magical" being able to always win such a strange game.

# Setup
1. Download `assist.py`. 
2. If you have an arbiter (a "Grace"), have each player launch an instance of the script and follow the prompts! The terminal will output what you should do each round based on what the other player did previously and your number.

If you don't have an aribter, download `arbiter_host.py` on one player's machine and `arbiter_client.py` on the other. 
1. Before the game, run `arbiter_host.py` and follow the prompts to enter the other player's IP address (ensure you are on the same network!). 
2. Run the client script, and press enter to generate numbers for a game and send them. 

Each player will see only their number in terminal output, and from there follow the steps above to play the game!