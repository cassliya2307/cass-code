/*
prompt the user to enter three grades
save them in separate variables
determine the average and save it in a variablr
check if the average is less than or equals to 90 and less than or equals to 100, if it is display "A"
check if the average is less than or equals to 80 and less than 90, if it is display "B"
check if the average is less than or equals to 70 and less than 80, if it is display "C"
check if the average is less than or equals to 60 and less than 70, if it is display "D"
check if the average is less than or equals to 0 and less than 60, if it is diaplay "E"

*/
import java.util.Scanner;
public class Grade4{

public static void main(String[] args){

Scanner scanner = new Scanner(System.in);



System.out.print("Enter first grade");
int first = scanner.nextInt();
System.out.print("Enter second grade");
int second = scanner.nextInt();
System.out.print("Enter third grade");
int third = scanner.nextInt();

int average = first + second + third / 3;


if(average <= 90 && average <= 100){

System.out.print("A");

}
else if(average <= 80 && average < 90){


System.out.print("B");


}
else if(average <= 70 && average < 80){


System.out.print("C");


}
else if(average <= 60 && average < 70){


System.out.print("D");


}
else if(average <= 0 && average < 60){


System.out.print("E");


}













}


}