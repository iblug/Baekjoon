import java.io.IOException;

public class Main {
	public static void main(String args[]) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		Math.pow(2, n);
		System.out.println((int) Math.pow(Math.pow(2, n) + 1, 2));
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}
