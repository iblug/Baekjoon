import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br;
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	private void solution() throws IOException {
		System.out.println(readInt()+readInt());
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
