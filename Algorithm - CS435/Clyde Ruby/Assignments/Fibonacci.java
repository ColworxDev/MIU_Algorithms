
public class Fibonacci {

	static int counter = 0;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("The result of FIB using recursive is: " + fibByBruteForce(30));
		System.out.println("The number of recursives is: " + counter);
		counter = 0;
		System.out.println("The result of FIB using memory is: " + fibByMemorized(30));
		System.out.println("The number of memorized recursives is: " + counter);
	}

	static int fibByBruteForce(int n){
		counter++;
		if (n <= 1) {
			return n;
		}
		else {
//			System.out.println("The recursive #: " + ++counter);
			return fibByBruteForce(n-1) + fibByBruteForce(n-2);
		}
	}
	
	static int[] fMem;
	static int counter2 = 0;
	static int fibByMemorized(int n) {
		fMem = new int[n+1];
		
		for(int i=0; i<=n; i++) {
			fMem[i] = -1;
		}
 
		return fibo(n);
	}
	
	static int fibo(int n) {
		counter++;
		if(fMem[n] < 0) {
			if(n == 0) {
				fMem[n] = 0; //store fib value if n = 0
			}
			else {
				if(n == 1) {
					fMem[n] = 1; //store fib value if n = 1
				}
				else {
//					System.out.println("The memorized recursive #: " + ++counter);
					fMem[n] = fibo(n-1) + fibo(n-2); 
				}
			}
		}
		return fMem[n];
	}
}
