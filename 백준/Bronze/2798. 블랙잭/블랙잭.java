import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int m = readInt();
		int[] a = new int[n];
		int r = 0;
		int s = 0;
		for (int i = 0; i < n; i++) {
			a[i] = readInt();
		}
		for (int i = 0; i < n-2; i++) {
			for (int j = i+1; j < n-1; j++) {
				for (int k = j+1; k < n; k++) {
					s = a[i] + a[j] + a[k];
					if (r < s && s <= m) {
						r = s;
					}
				}
			}
		}
		System.out.println(r);
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