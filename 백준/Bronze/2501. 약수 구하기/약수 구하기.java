import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int a = readInt();
		
		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = 1; i <= Math.sqrt(n); i++) {
			if (n % i == 0) {
				arr.add(i);
				if (i != n / i) {
					arr.add(n / i);
				}
			}
		}
		Collections.sort(arr);

		if (arr.size() >= a) {
			System.out.print(arr.get(a - 1));
		} else {
			System.out.print(0);
		}
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);

		}
		return t;
	}
}