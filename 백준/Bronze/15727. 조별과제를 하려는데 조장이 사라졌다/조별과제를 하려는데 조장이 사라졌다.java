import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		float n = Integer.parseInt(br.readLine());
		System.out.println((int)Math.ceil(n/5));
	}
} 