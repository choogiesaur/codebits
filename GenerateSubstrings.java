import java.util.*;

public class GenerateSubstrings{

     public static void main(String []args){
        System.out.println("Hello World");
        Hashtable<String, Hashtable<Character, Integer>> lol;
        
        String tst = "abcde";
        //            01234
        
        for(int i = 0; i < tst.length(); i++){ // every poss substring length
            //System.out.println("Substring length: " + (tst.length()-i));
            for(int j = 0; j < tst.length()-i; j++){
                //System.out.println("j:" + j);
                System.out.println(tst.substring(j,tst.length()-i));                
            }
        }
     }
}
