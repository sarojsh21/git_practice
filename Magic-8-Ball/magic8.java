public class Magic8 {
  
  public static void main(String[] args) {
    
    System.out.println("MAGIC 8-BALL: \n");
    
    int user = (int) (Math.random() * 6);
    System.out.println(user);
    
    switch(user){
        case 0:
            System.out.println("Good-Morning");
            break;
        case 1:
            System.out.println("Good-Afternoon");
            break;
        case 2:
            System.out.println("I am learning Java");
            break;
        case 3:
            System.out.println("I am coding Magic 8 ball");
            break;
        case 4:
             System.out.println("Excellent");
            break;
            
        case 5:
             System.out.println("The End");
            break;
        default:
             System.out.println("Error");
            break;
    }
    }
    
}