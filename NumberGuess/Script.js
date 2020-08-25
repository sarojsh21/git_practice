let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget()
{
  return Math.floor(Math.random()*9);
}

function compareGuesses(userGuess,compGuess,targetNum)
{
  let a = Math.abs(targetNum-userGuess);
  let b = Math.abs(targetNum-compGuess);
  if(a<=b)
    return true;
  else
    return false;
}
function updateScore(winner)
{
  if(winner === 'human')
    humanScore++;
  else
    computerScore++;
}
function advanceRound()
{
  currentRoundNumber++;
}