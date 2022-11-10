import java.util.Scanner;
public class SumOfEvenOdd {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("enter no of elements");
        int n=sc.nextInt();
        System.out.println("enter elements into array");
        int[] arr=new int[n];
        for (int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int even=0,odd=0;
        for (int i=0;i<arr.length;i++){
            if(arr[i]%2==0){
                even+=arr[i];
            }
            else if(arr[i]%2!=0){
                odd+=arr[i];
            }
        }
        System.out.println("sum of even numbers:"+even+" Sum of odd elements is:"+odd);

    }
}
