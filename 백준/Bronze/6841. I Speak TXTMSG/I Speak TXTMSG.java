import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Map<String, String> sf = new HashMap<>();
        sf.put("CU", "see you\n");
        sf.put(":-)", "I’m happy\n");
        sf.put(":-(", "I’m unhappy\n");
        sf.put(";-)", "wink\n");
        sf.put(":-", "stick out my tongue\n");
        sf.put("(~.~)", "sleepy\n");
        sf.put("TA", "totally awesome\n");
        sf.put("CCC", "Canadian Computing Competition\n");
        sf.put("CUZ", "because\n");
        sf.put("TY", "thank-you\n");
        sf.put("YW", "you’re welcome\n");
        sf.put("TTYL", "talk to you later");

        String s;
        while (true) {
            s = br.readLine();
            if (sf.get(s) == null) {
                bw.write(s);
                bw.write("\n");
            } else {
                bw.write(sf.get(s));
            }
            if (s.equals("TTYL")) {
                break;
            }
        }

        bw.flush();
        bw.close();
    }
}