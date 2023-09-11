import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int s = 0;
		for (int i = 0; i < 5; i++) {
			s += Math.pow(readInt(), 2);
		}
		System.out.print(s % 10);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}

		return t;
	}
}