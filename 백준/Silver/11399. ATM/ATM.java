import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = readInt();
        }

        Arrays.sort(arr);

        int s = 0;
        int r = 0;
        for (int i = 0; i < n; i++) {
            s += arr[i];
            r += s;
        }

        System.out.println(r);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            
        }
        return t;
    }
}