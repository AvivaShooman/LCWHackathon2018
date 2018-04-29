package Task_1;

public class Friedrich_Gauss {

	public static void main(String[] args) {

		calculate();

	}
//will add up all numbers from 1 (2) through 1000 excluding perfect squares
	private static void calculate() {
		int num;
		int sum = 0;
		for(int i=1;i<1001;i++) {//loop will run through all integers 1 through 100
			num =  (int) Math.sqrt(i);//get square root in int form
			if(i ==num*num) {//if the integer square roots multiply to original number then original is perfect square
				//System.out.println(i+ " is a perfect square of number " +num);
				continue;//number should not be counted start loop again
			}else {
				sum+=i;//if not perfect square should be added to total
			}
		}
		System.out.println("The sum is "+ sum);//display total
		
	}
	

}
