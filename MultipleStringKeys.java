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

    public static void main(String[] args) throws IOException {
        String s1 = "LLAMA";
        String s2 = "AM";

        int result = commonChild(s1, s2);
        System.out.println(result);
    }
}
