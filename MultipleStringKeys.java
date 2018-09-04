import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class MultipleStringKeys {
    
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
            // dangerous because: although (x,y) == (y,x), hash((x ,y)) != hash((y,x)) 
            //return (this.s1.equals(key.s1) && this.s2.equals(key.s2)) || (this.s1.equals(key.s2) && this.s2.equals(key.s1));
            return (this.s1.equals(key.s1) && this.s2.equals(key.s2));
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

    public static void main(String[] args) throws IOException {
        Hashtable<StringKey, Integer> table = new Hashtable<StringKey, Integer>();
        
        StringKey x = new StringKey("apple","banana");
        table.put(x, 1);
        
        StringKey y = new StringKey("apple","grape");
        table.put(y, 1337);
        
        StringKey z = new StringKey("apple","pear");
        table.put(z, 999);
      	
        System.out.println(table.containsKey(x));
      	System.out.println(table.get(x));
      	System.out.println(table.get(y));
      	System.out.println(table.get(z));
    	System.out.println();
      
      	table.put(z, 91919); 
      	System.out.println(table.get(z));
      	System.out.println();	
      
      	StringKey x2 = new StringKey("banana","apple");
      	System.out.println(x.equals(x2));
      	table.put(x2, 333);
      	System.out.println(table.get(x2));
      	System.out.println(table.get(x));
      
    }
}
