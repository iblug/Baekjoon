import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		boolean [] arr = new boolean[42];
		for (int i = 0; i < 10; i++) {
			arr[readInt()%42] = true;
		}
		int s = 0;
		for ( boolean e : arr ) {
			if (e) {
				s += 1;
			}
		}
		System.out.println(s);
	}
	private static int readInt() throws IOException {
		int v, t = System.in.read() & 15;
		while ((v = System.in.read()) > 32)
			t = (t << 3) + (t << 1) + (v & 15);
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}