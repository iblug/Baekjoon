import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    static Stack<Character> stk;
    static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            stk = new Stack<>();
            boolean flag = true;
            String line = br.readLine();
            if (line.equals(".")) {
                break;
            }
            for (char c : line.toCharArray()) {
                if (c == '(') {
                    stk.push(c);
                } else if (c == '[') {
                    stk.push(c);
                } else if (c == ')') {
                    if (stk.isEmpty() || stk.peek() == '[') {
                        flag = false;
                    } else {
                        stk.pop();
                    }
                } else if (c == ']') {
                    if (stk.isEmpty() || stk.peek() == '(') {
                        flag = false;
                    } else {
                        stk.pop();
                    }
                }
            }
            if (!stk.isEmpty()) {
                flag = false;
            }
            sb.append(flag ? "yes" : "no").append('\n');
        }
        System.out.println(sb);
    }
}