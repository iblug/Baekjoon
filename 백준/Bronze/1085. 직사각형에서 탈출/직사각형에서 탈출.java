import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int x = readInt();
		int y = readInt();
		int w = readInt();
		int h = readInt();

		int[] a = new int[] { x, w - x, y, h - y };

		int min = a[0];
		for (int m : a) {
			if (m < min) {
				min = m;
			}
		}
		System.out.println(min);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}
