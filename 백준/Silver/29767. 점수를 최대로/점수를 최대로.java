import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		long[] c = new long[n];
		for (int i = 0; i < n; i++) {
			c[i] = Long.parseLong(st.nextToken());
		}
		
		PriorityQueue<Long> queue = new PriorityQueue<>();
		
		long accSum = c[0];
		queue.offer(accSum);
		
		for (int i = 1; i < n; i++) {
			accSum += c[i];
			queue.offer(accSum);
			
			if (queue.size() > k) {
				queue.poll();
			}
		}
		
		long sumTopKElements = 0;
		while (!queue.isEmpty()) {
			sumTopKElements += queue.poll();
		}
		
		System.out.println(sumTopKElements);
	}
}