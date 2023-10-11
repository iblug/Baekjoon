import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a, b, c;
		a = readInt();
		b = readInt();
		c = readInt();
		if (a + b + c != 180) {
			System.out.println("Error");
		} else if (a == 60 && b == 60){
			System.out.println("Equilateral");
		} else if (a == b || a == c || b == c) {
			System.out.println("Isosceles");
		} else {
			System.out.println("Scalene");
		}
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}

}