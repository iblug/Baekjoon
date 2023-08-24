import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int N = readInt();
		int[] arr = new int[N];
		int M = 0;
		int i, t;
		for (i = 0; i < N; i++) {
			t = readInt();
			M = Math.max(M, t);
			arr[i] = t;
		}
		float s = 0;
		for (i = 0; i < N; i++) {
			s += ((float) arr[i] / M)*100;
		}
		System.out.println(s/N);
		
	}
	private static int readInt() throws IOException {
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