import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		ArrayList<Integer> x = new ArrayList<>();
		ArrayList<Integer> y = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			int a = readInt();
			int b = readInt();
			x.add(a);
			y.add(b);
		}
		System.out.println(Math.abs(Collections.max(x) - Collections.min(x)) * Math.abs(Collections.max(y) - Collections.min(y)));
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean neg = false;
		while ((v = System.in.read()) > 33) {
			if (v == 45) {
				neg = true;
				continue;
			}
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return neg? -t:t;
	}

}