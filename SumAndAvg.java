import java.util.Scanner;
public class SumAndAvg{
  public static void main(String [] args){
	System.out.println("how many elements u want to enter?");
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	int [] array= new int [n];
	System.out.println("enter elements into the array ");
	//reading elements
	for(int i=0;i<n;i++){
	     array[i]=sc.nextInt();
	}
	int sum=0,avg;
	for(int i=0;i<n;i++)
	{
	  sum+=array[i];
	   }
	avg=sum/n;
	//display
	System.out.println("sum="+sum+" "+"average="+avg);
	sc.close();
           }
}
	  
	