import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

// HackerRank problem to find size of largest common child of two strings
// Example of using a helper object to hash multiple values at once, in this case (String, String)
// TODO: pull out hashtable logic, not needed with current algo
public class LargestCommonChild {
    
    // helper class; a (String, String) key pair that can be hashed
    public static class StringKey {
        
        public final String s1;
        public final String s2;
        
        public StringKey(String s1, String s2){
            this.s1=s1;
            this.s2=s2;
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof StringKey)) return false;
            StringKey key = (StringKey) o;
            // might need to not be this lenient? as is, (x,y) == (y,x)
            return (this.s1.equals(key.s1) && this.s2.equals(key.s2)) || (this.s1.equals(key.s2) && this.s2.equals(key.s1));
        }
        
        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = result * prime + this.s1.hashCode();
            result = result * prime + this.s2.hashCode();
            return result;
        }
    }
    
    // Complete the commonChild function below.
    static int commonChild(String s1, String s2) {
        // longest child
        Hashtable<StringKey, Integer> tab = new Hashtable<StringKey, Integer>();
        int max = 0;
        int res = 0;
        
        // on each iteration, clip first character, then find LCC of curr s1_substring and s2
        for(int i = 0; i < s1.length(); i++){
            String s1Sub = s1.substring(i,s1.length());
            StringKey key = new StringKey(s1Sub, s2);
            
            if(tab.containsKey(key) == false){
                res = longestChild(s1Sub,s2);
                tab.put(key, res);
            } else {
                res = tab.get(key);
            }
            
            max = Math.max(max, res);
        }
        return max;
    }
    
    // this method finds first common character and grows child from there
    // will not see a larger child that starts at a later position
    // so, we call it for every starting position in string 1
    static int longestChild(String s1, String s2){
        // longest child
        int lastUsed=-1;
        int max = 0;
        String child = "";
        for(int i = 0; i < s1.length(); i++){
            for(int j = lastUsed+1; j < s2.length(); j++){ // start right after last used character in string 2
                if(s1.charAt(i) == s2.charAt(j)){
                    child = child + s2.charAt(j);
                    max = Math.max(max, child.length());
                    lastUsed=j;
                    break;
                }
            }
        }
        System.out.println(max);
        return max;        
    }

    public static void main(String[] args) throws IOException {
        String s1 = "LLAMA";
        String s2 = "AM";

        int result = commonChild(s1, s2);
        System.out.println(result);
    }
}
