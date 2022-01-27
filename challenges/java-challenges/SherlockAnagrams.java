import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SherlockAnagrams {

    // For given string s, determine how many pairs of its substrings are anagrams
    // this hashtable solution times out on HackerRank but works
    // faster way is to convert strings to char array, sort, check if equal
    static int sherlockAndAnagrams(String s) {

        ArrayList < String > subs = new ArrayList < String > ();
        for (int i = 0; i < s.length(); i++) { // every poss substring length
            for (int j = 0; j < s.length() - i; j++) {
                String sub = s.substring(j, s.length() - i);
                subs.add(sub);
            }
        }

        int pairs = 0;
        for (int i = 0; i < subs.size(); i++) {
            for (int j = i + 1; j < subs.size(); j++) {
                if (isAnagram(subs.get(i), subs.get(j))) {
                    pairs++;
                }
            }
        }
        return pairs;
    }

    public static boolean isAnagram(String s1, String s2) {
        //System.out.println(s1 + "," + s2);
        if (s1.length() != s2.length()) {
            return false;
        }

        Hashtable < Character, Integer > s1hash = new Hashtable < Character, Integer > ();
        Hashtable < Character, Integer > s2hash = new Hashtable < Character, Integer > ();

        //strings are same length so can count chars in same loop
        for (int i = 0; i < s1.length(); i++) {

            char c;
            int val;

            c = s1.charAt(i);
            if (s1hash.get(c) == null) {
                s1hash.put(c, 1);
            } else {
                val = s1hash.get(c);
                s1hash.put(c, val + 1);
            }

            c = s2.charAt(i);
            if (s2hash.get(c) == null) {
                s2hash.put(c, 1);
            } else {
                val = s2hash.get(c);
                s2hash.put(c, val + 1);
            }
        }

        //if character set not same, not anagrams
        if(s1hash.keySet().size() != s2hash.keySet().size()){
            return false;
        }

        for (Character c: s1hash.keySet()) {
            
            if(s2hash.get(c) == null || s1hash.get(c) != s2hash.get(c)){
                return false;
            } else {
                continue;
            }
        }
        
        for (Character c: s2hash.keySet()) {
            
            if(s1hash.get(c) == null || s1hash.get(c) != s2hash.get(c)){
                return false;
            } else {
                continue;
            }
        }
        
        /*
        for(Character c : s1hash.keySet()){
            System.out.println("Char: " + c + " s1count: " + s1hash.get(c) + " s2count: " + s2hash.get(c));
        }
        */
        
        System.out.println(s1 + "|" + s2 + " are anagrams");
        return true;
    }
}
