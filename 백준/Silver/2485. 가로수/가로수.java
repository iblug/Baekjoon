import java.io.IOException;
import java.util.*;

public class Main {
	static public void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int[] a = new int[n];
		Set<Integer> set = new HashSet<>();
		a[0] = readInt();
		for (int i = 1; i < n; i++) {
			a[i] = readInt();
			set.add(a[i] - a[i-1]);
		}
		List<Integer> list = new ArrayList<>(set);
		Collections.sort(list);
		int t = list.get(0);
		for (int e : list) {
			int c = getGcd(t, e);
			if (c < t) {
				t = c;
			}
		}
		System.out.println((a[n - 1] - a[0])/t + 1 - n);
	}

	private int getGcd(int x, int y) {
		if (x == 0) {
			return y;
		}
		return getGcd(y%x, x);
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