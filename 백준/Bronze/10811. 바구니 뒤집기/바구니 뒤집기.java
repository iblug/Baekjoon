import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int N = readInt();
		int M = readInt();
		
		int[] arr = new int[N+1];
		int i;		
		for (i = 1; i <= N; i++) {
			arr[i] = i;
		}
		for (i = 0; i < M; i++) {
			int a = readInt();
			int b = readInt();
			for (int j = 0; j < (b - a + 1) / 2; j++) {
				int t = arr[a+j];
				arr[a+j] = arr[b-j];
				arr[b-j] = t;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (i = 1; i <= N; i++) {
			sb.append(arr[i]).append(" ");
		}
		System.out.println(sb);
	}
	private static int readInt() throws IOException {
		int v, t = 0;
		
		while ((v = System.in.read()) > 47) {
			t = t*10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}