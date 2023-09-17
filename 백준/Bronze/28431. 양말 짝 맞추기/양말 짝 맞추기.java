import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
    	new Main().solution();
    	br.close();

    }
    public void solution() throws IOException {
    	int[] socks = new int[5];
    	for (int i = 0; i < 5; i++) {
    		socks[i] = Integer.parseInt(br.readLine());
    	}
    	
    	System.out.println(findSock(socks));    	
    }
    
    private int findSock(int[] socks) {
    	HashMap<Integer, Integer> sockCounts = new HashMap<>();
    	
    	for (int sock : socks) {
    		sockCounts.put(sock, sockCounts.getOrDefault(sock, 0) + 1);
    	}
    	for (int key : sockCounts.keySet()) {
    		if (sockCounts.get(key) % 2 == 1) {
    			return key;
    		}
    	}
    	return 0;
    }
}
