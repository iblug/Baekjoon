import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	private void solution() throws IOException {
		int n = readInt();
		int k = readInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = readInt();
		}
		Arrays.sort(a);
		System.out.println(a[n-k]);
		
		
	}
	private int readInt() throws IOException {
		int v, t = 0;
		while((v = System.in.read()) > 47) {
			t = 10 * t + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}