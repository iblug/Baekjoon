import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int cnt = 1;
        Deque<Integer> stk = new ArrayDeque<>();
        boolean flag = true;
        int current = readInt();
        while (cnt <= n && current != 0) {
            if (current == cnt) {
                cnt++;
                current = readInt();
            } else if (stk.isEmpty()) {
                stk.push(current);
                current = readInt();
            } else if (stk.peek() == cnt) {
                stk.pop();
                cnt++;
            } else if (stk.peek() < current) {
                flag = false;
                break;
            } else {
                stk.push(current);
                current = readInt();
            }
        }
        System.out.println(flag ? "Nice" : "Sad");
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
}