import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		System.out.printf(":fan::fan::fan:\n:fan::%s::fan:\n:fan::fan::fan:",br.readLine());
	}
}