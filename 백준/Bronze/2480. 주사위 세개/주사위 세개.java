import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	static void solution() throws IOException {
		String[] data = br.readLine().split(" ");
		int a = Integer.parseInt(data[0]);
		int b = Integer.parseInt(data[1]);
		int c = Integer.parseInt(data[2]);
		
		if (a == b && a == c && b == c) {
			System.out.println(10000+a*1000);
		} else if (a == b || a == c) {
			System.out.println(1000+a*100);
		} else if (b == c) {
			System.out.println(1000+b*100);
		} else {
			if (a > b && a > c) {
				System.out.println(a*100);
			} else if (b > a && b > c) {
				System.out.println(b*100);
			} else {
				System.out.println(c*100);				
			}
		}
	}
}