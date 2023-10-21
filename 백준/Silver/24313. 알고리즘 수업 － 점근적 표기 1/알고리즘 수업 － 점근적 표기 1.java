import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a1 = readInt();
		int a0 = readInt();
		int c = readInt();
		int n0 = readInt();
		if (a0 <= (c - a1) * n0 && a1 <= c) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean f = false;
		while ((v = System.in.read()) > 33) {
			if (v == 45) {
				f = true;
				continue;
			}
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return f ? -t : t;
	}

}