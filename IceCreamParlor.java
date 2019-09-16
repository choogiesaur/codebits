import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class IceCreamParlor.java {

    // Complete the whatFlavors function below.
    static void whatFlavors(int[] cost, int money) {
        Hashtable<Integer,Integer> costFirst = new Hashtable<Integer, Integer>();
        int lesser  = -1;
        int greater = -1;
        for(int i = 0; i < cost.length; i++){
            costFirst.put(cost[i], i);
        }
        for(int i = 0; i < cost.length; i++){
            int target = money - cost[i];
            if(costFirst.containsKey(target) && costFirst.get(target) != i){
                int found = costFirst.get(target);
                if(i <= found){
                    lesser  = i + 1;
                    greater = found + 1;
                }else{
                    lesser  = found + 1;
                    greater = i + 1;
                }
                System.out.println(lesser + " " + greater);
                return;
            }
        }
    }
}
//hackerrank / ctci
