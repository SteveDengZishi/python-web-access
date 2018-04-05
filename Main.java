package Steve;

public class Main{
	public static void main(String[] args){
		System.out.println("Please input a number");
		Scanner myscanner = new Scanner(System.in);

		//scanning a int, need to consume the new line
		int num = myscanner.nextInt();
		myscanner.nextLine();

		//scanning a string
		String ans = myscanner.nextLine();
	}
}