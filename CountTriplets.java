import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

// HackerRank problem
// given list of numbers, count the number of times list(z) = list(y) * r = list(x) * r * r
// aka, find number of triplet subsequences where each element is the last element * r
public class CountTriplets {

    // Complete the countTriplets function below.
    static long countTriplets(List<Long> arr, long r) {
        HashMap<Long, Long> visited = new HashMap<Long,Long>();
        HashMap<Long, Long> visited2 = new HashMap<Long,Long>();
        long count = 0;
            
        for(int i = arr.size()-1; i >= 0; i--){ // go thru each number from end to start
            long curr = arr.get(i);
            System.out.println("Curr: " + curr);

            if(visited.containsKey(curr*r)){ //if we've encountered r * current num
                if(visited2.containsKey(curr*r)){ //if we've encountered r * r * current num
                    count += visited2.getOrDefault(curr*r, 0L);
                }
                long times = visited.get(curr*r);
                visited2.put(curr, visited.getOrDefault(curr,0L)+times);
                //basically increases by the number of possible ways we could have gotten there
            }
            visited.put(curr, visited.getOrDefault(curr,0L)+1); 
            //increment times we've seen curr
        }
        return count;
    }

    public static void main(String[] args) throws IOException {

    }
}
