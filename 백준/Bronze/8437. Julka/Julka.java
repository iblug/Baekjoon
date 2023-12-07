import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		BigInteger n = new BigInteger(br.readLine());
		BigInteger g = new BigInteger(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		BigInteger m = n.divide(new BigInteger("2")).subtract(g.divide(new BigInteger("2")));
		sb.append(n.subtract(m)).append("\n").append(m);
		System.out.println(sb);
	}
}