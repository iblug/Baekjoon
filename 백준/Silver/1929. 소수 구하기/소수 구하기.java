import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a = readInt();
		int b = readInt();
		boolean[] f = new boolean[b+1];
		
		f[0] = true;
		f[1] = true;
		
		for (int i = 1; i < Math.sqrt(b) + 1; i++) {
			if (!f[i]) {
				for (int j = i*2; j <= b; j += i) {
					f[j] = true;
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		if (a <= 2 && b >= 2) {
			sb.append(2).append("\n");
			a = 3;
		}
		if (a % 2 == 0) {
			a++;
		}
		for (int i = a; i <= b; i += 2) {
			if (!f[i]) {
				sb.append(i).append("\n");
			}
		}
		System.out.println(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			 t = t * 10 + (v - 48);
		}
		return t;
	}
}