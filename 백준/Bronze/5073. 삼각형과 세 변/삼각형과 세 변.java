import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a, b, c;
		StringBuilder sb = new StringBuilder();
		while (true) {
			a = readInt();
			b = readInt();
			c = readInt();
			if (a == 0 && b == 0 && c == 0) {
				break;
			}
			int[] arr = {a, b, c};
			Arrays.sort(arr);
			if (arr[0] + arr[1] <= arr[2]) {
				sb.append("Invalid\n");
			} else if (arr[0] == arr[1] && arr[0] == arr[2] && arr[1] == arr[2]) {
				sb.append("Equilateral\n");
			} else if (arr[0] == arr[1] || arr[0] == arr[2] || arr[1] == arr[2]) {
				sb.append("Isosceles\n");
			} else {
				sb.append("Scalene\n");
			}
		}
		System.out.println(sb);
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