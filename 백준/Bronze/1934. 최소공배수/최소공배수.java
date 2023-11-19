import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		StringBuilder sb = new StringBuilder();
		while (n-- > 0) {
			int a = readInt();
			int b = readInt();
			sb.append(getLcm(a, b)).append("\n");
		}
		System.out.println(sb);
	}

	private int getLcm(int x, int y) {
		int gcd = getGcd(x, y);
		return x * y / gcd;
	}
	
	private int getGcd(int x, int y) {
		if (x > y) {
			int t = x;
			x = y;
			y = t;
		}
		while (x > 0) {
			int r = y % x;
			y = x;
			x = r;
		}
		return y;
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