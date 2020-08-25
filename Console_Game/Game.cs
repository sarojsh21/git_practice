using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string keyPressed,out int x,out int y)
    {
    x = 0;
    y = 0;
    switch (keyPressed)
    {
    case "LeftArrow":
    x--;
    break;
    case "RightArrow":
    x++;
    break;
    case "UpArrow":
    y--;
    break;
    case "DownArrow":
    y++;
    break;
    
    default:
    Console.WriteLine("You have preesed wrong key");
    break;
    }
   }
    
    public new static char UpdateCursor (string keyPressed)
    {
    switch (keyPressed)
    {
    case "LeftArrow":
    return '<';
    break;
    
    case "RightArrow":
    return '>';
    break;
    
    case "UpArrow":
    return '^';
    break;
    
    case "DownArrow":
    return 'v';
    break;
    
    default:
    return 'X';
    break;
    }
    }
    
    public new static int KeepInBounds(int co, int maxval)
    {
    
    if (co > maxval)
    {
    return 0;
    }
    else if (co < 0)
    {
    return maxval;
    }
    else
    {
    return co;
    }
    
    }
    
    public new static bool DidScore(int x, int y, int fruitx, int fruity)
    {
    if ((x == fruitx) && (y ==fruity))
    {
    return true;
    }
    else{
    return false;
    }
    
    }
  }
}