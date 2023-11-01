import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	private void solution() throws IOException {
		int[] a = new int[5];
		int s = 0;
		for (int i = 0; i < 5; i++) {
			a[i] = readInt();
			s += a[i];
		}
		StringBuilder sb = new StringBuilder();
		Arrays.sort(a);
		sb.append(s/5).append('\n').append(a[2]);
		System.out.println(sb);
		
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
