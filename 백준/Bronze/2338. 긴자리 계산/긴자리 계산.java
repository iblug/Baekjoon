import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	
	private void solution() throws Exception {
		BigInteger n = new BigInteger(br.readLine());
		BigInteger m = new BigInteger(br.readLine());
		StringBuilder sb = new StringBuilder();
		sb.append(n.add(m)).append('\n').append(n.subtract(m)).append('\n').append(n.multiply(m));
		System.out.println(sb);
	}
}