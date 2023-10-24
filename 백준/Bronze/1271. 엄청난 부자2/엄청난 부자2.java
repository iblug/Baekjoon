import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	
	private void solution() throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		BigInteger n = new BigInteger(st.nextToken());
		BigInteger m = new BigInteger(st.nextToken());
		StringBuilder sb = new StringBuilder();
		sb.append(n.divide(m)).append('\n').append(n.remainder(m));
		System.out.println(sb);
	}
}