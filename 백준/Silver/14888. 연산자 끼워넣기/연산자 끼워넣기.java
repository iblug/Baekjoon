import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static int n;
    static int[] nums, ops;
    static List<Integer> ans;

    public static void main(String[] args) throws IOException {
        n = readInt();
        nums = new int[n];
        ops = new int[4];
        ans = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            nums[i] = readInt();
        }

        for (int i = 0; i < 4; i++) {
            ops[i] = readInt();
        }

        rec(nums[0], 0);

        StringBuilder sb = new StringBuilder();
        sb.append(Collections.max(ans)).append('\n').append(Collections.min(ans));

        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }

    static void rec(int t, int d) {
        if (d == n - 1) {
            ans.add(t);
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (ops[i] > 0) {
                ops[i]--;
                if (i == 0) {
                    rec(t + nums[d + 1], d + 1);
                } else if (i == 1) {
                    rec(t - nums[d + 1], d + 1);
                } else if (i == 2) {
                    rec(t * nums[d + 1], d + 1);
                } else {
                    rec(t / nums[d + 1], d + 1);
                }
                ops[i]++;
            }
        }
    }
}