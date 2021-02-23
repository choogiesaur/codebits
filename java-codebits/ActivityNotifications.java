public class ActivityNotifications {
    // Complete the activityNotifications function below.
    static int activityNotifications(int[] expenditure, int d) {
        int n = expenditure.length;
        int notifications = 0;
        for(int i = d; i < n; i++){
            int[] window = Arrays.copyOfRange(expenditure, i - d, i);
            Arrays.sort(window);
            double median = findMedian(window);
            if(expenditure[i] >= median*2){
                notifications++;
            }
        }
        return notifications;
    }

    static double findMedian(int[] arr){
        int n = arr.length;
        if(n % 2 == 0){
            return (double) (arr[n/2] + arr[n/2-1])/2;
        }else{
            return (double) arr[n/2];
        }
    }
}

//from hackerrank
//TODO: implement counting sort to speed it up
