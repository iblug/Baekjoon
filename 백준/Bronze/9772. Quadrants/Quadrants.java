import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        float x, y;
        StringTokenizer st;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            st = new StringTokenizer(br.readLine());
            x = Float.parseFloat(st.nextToken());
            y = Float.parseFloat(st.nextToken());

            bw.write(Quadrant(x, y));

            if (x == 0 && y == 0) {
                break;
            }

            bw.write("\n");
        }

        bw.flush();
        bw.close();
    }

    static String Quadrant(float x, float y) {
        String result;
        if (x > 0 && y > 0) {
            result = "Q1";
        } else if (x < 0 && y > 0) {
            result = "Q2";
        } else if (x < 0 && y < 0) {
            result = "Q3";
        } else if (x > 0 && y < 0) {
            result = "Q4";
        } else {
            result = "AXIS";
        }
        return result;
    }
}