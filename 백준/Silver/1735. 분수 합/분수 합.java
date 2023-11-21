import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a = readInt();
		int b = readInt();
		int c = readInt();
		int d = readInt();
		int e = a * d + c * b;
		int f = b * d;
		StringBuilder sb = new StringBuilder();
		sb.append(e / getGcm(e, f)).append(" ").append(f / getGcm(e, f));
		System.out.println(sb);

	}

	private int getGcm(int x, int y) {
		if (x > y) {
			int t = x;
			x = y;
			y = t;
		}
		while (x > 0) {
			int t = x;
			x = y % x;
			y = t;
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