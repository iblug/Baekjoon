import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String s = br.readLine();
            if (s.length() < 6 || s.length() > 9) {
                bw.write("no\n");
            } else {
                bw.write("yes\n");
            }
        }
        bw.flush();
        bw.close();
    }
}