import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		while (true) {
			int n = readInt();
			if (n == -1) {
				break;
			}
			ArrayList<Integer> a = new ArrayList<>();
			int s = 0;
			for (int i = 1; i <= Math.sqrt(n); i++) {
				if (n % i == 0) {
					s += i + n / i;
					a.add(i);
					if (i != n / i) {
						a.add(n / i);
					}
				}
			}
			Collections.sort(a);
			s -= n;
			if (s == n) {
				a.remove(a.size() - 1);
				sb.append(n).append(" = ");
				for (int i = 0; i < a.size() - 1; i++) {
					sb.append(a.get(i)).append(" + ");
				}
				sb.append(a.get(a.size() - 1)).append("\n");
			} else {
				sb.append(n).append(" is NOT perfect.\n");
			}
		}
		System.out.print(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean flag = false;
		while ((v = System.in.read()) > 32) {
			if (v == '-') {
				flag = true;
				continue;
			}
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		if (flag) {
			return -t;
		} else {
			return t;
		}
	}
}