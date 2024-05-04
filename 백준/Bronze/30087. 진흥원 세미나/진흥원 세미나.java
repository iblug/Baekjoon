import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static Map<String, String> data;
    public static void main(String[] args) throws IOException {
        data = new HashMap<>();
        data.put("Algorithm", "204");
        data.put("DataAnalysis", "207");
        data.put("ArtificialIntelligence", "302");
        data.put("CyberSecurity", "B101");
        data.put("Network", "303");
        data.put("Startup", "501");
        data.put("TestStrategy", "105");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        while (N-- > 0) {
            String s = br.readLine();
            sb.append(data.get(s)).append('\n');
        }

        System.out.println(sb);
    }
}
