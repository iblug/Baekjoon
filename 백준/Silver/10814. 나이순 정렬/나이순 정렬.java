import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		List<Pair> list = new ArrayList<>();
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			list.add(new Pair(age, name));
		}
		
		Collections.sort(list);
		
		StringBuilder sb = new StringBuilder();
		
		for (Pair p : list) {
			sb.append(p.age).append(" ").append(p.name).append("\n");
		}
		
		System.out.println(sb);
		
	}
	
	class Pair implements Comparable<Pair> {
        int age;
        String name;
        
        Pair(int age, String name) {
            this.age = age;
            this.name = name;
        }
        
        @Override
        public int compareTo(Pair o) {
            return this.age - o.age;
        }
    }
}