import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] dis = new int[n - 1];
        int[] price = new int[n];

        for (int i = 0; i < n - 1; i++) {
            dis[i] = readInt();
        }

        for (int i = 0; i < n; i++) {
            price[i] = readInt();
        }

        int idx = 0;
        int min_price = price[0];
        int result = 0;
        int sum = 0;
        while (idx < n - 1) {
            if (min_price >= price[idx + 1]) {
                sum += dis[idx];
                result += min_price * sum;
                min_price = price[idx + 1];
                sum = 0;
            } else if (min_price < price[idx + 1]) {
                sum += dis[idx];
            }
            idx++;
        }
        result += min_price * sum;

        System.out.println(result);

    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }

        return t;
    }
}