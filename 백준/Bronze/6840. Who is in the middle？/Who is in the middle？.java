import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int[] a = new int[3];
		for (int i = 0; i < 3; i++) {
			a[i] = readInt();
		}
		Arrays.sort(a);
		System.out.println(a[1]);
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