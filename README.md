## About
My solutions to the daily december challenges at:
https://adventofcode.com/

## Setup

1. Copy `.env.example` to `.env`
2. Add your Advent of Code session token to `.env`
   - You can find this token in your browser's cookies after logging into adventofcode.com
   - In Chrome/Firefox: DevTools -> Application/Storage -> Cookies -> session

3. bash fetch.sh DD
The result will be saved in "inputs" folder

## .gitignore
Do not commit personalized inputs, as this could be used for reverse engineering. 
*.in -> personalized inputs
*.example -> public example inputs