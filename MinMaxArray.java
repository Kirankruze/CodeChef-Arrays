import java.util.Scanner;
public class MinMaxArray{
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
	//max and min
	int max,min;
	max=min=array[0];
	for(int i=1;i<array.length;i++){
	     if(array[i]>max)
	          max=array[i];
	     if(array[i]<min)
	           min=array[i];
	   }
	//display
	System.out.println("max element="+max+" "+"min element="+min);
	sc.close();
           }
}
	  
	