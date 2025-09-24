/*Prompt the user to enter two things:
	The father's age 
	The son's age 
save both of them in a variable
initialize another variable to store the number of years and assign value o to it
initialize another variable to store the son's age times 2
Check if the fathers age is greater than twice the son's age, if it is
Determine how many years ago the fathers age was twice the sons age and display the number of years, if not
Check if the fathers age is less than twice the sons age, if it is
Determine the number of years it will take for the fathers age to be twice the sons age and display the number of years, if not
Check if the fathers age is equal to twice the sons age, if it is display the number of years as zero
*/

import java.util.Scanner;
public class Age3{
public static void main(String[] args){

Scanner scanner = new Scanner(System.in);

System.out.print("Enter father's age: ");
int father = scanner.nextInt();
System.out.print("Enter son's age: ");
int son = scanner.nextInt();

int years = 0;

int son2 = 2 * son;

if(father > son2){

years = father - 2 * son;
System.out.print("The number of years is" + years + " yrs");



}

else if(father < son2){

years = 2 * son - father;
System.out.printf("The number of years is %d yrs", years);



}

else if(father == son2){
;

System.out.print("The number of years is" + years + " yrs");


}




}



}