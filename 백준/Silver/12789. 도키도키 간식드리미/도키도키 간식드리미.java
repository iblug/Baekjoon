import java.io.IOException;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int cnt = 1;
        Stack<Integer> stk = new Stack<>();
        boolean flag = true;
        int current = readInt();
        while (cnt <= n && current != 0) {
            if (current == cnt) {
                cnt++;
                current = readInt();
            } else if (stk.isEmpty()) {
                stk.add(current);
                current = readInt();
            } else if (stk.peek() == cnt) {
                stk.pop();
                cnt++;
            } else if (stk.peek() < current) {
                flag = false;
                break;
            } else {
                stk.add(current);
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