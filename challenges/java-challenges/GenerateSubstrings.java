import java.util.*;

public class GenerateSubstrings{

     public static void main(String []args){
        String tst = "abcde";
        //            01234
        for(int i = 0; i < tst.length(); i++){ // every poss substring length
            for(int j = 0; j < tst.length()-i; j++){
                System.out.println(tst.substring(j,tst.length()-i));                
            }
        }
     }
}
