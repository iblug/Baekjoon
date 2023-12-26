import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        new Main().solution();
    }

    private void solution() {
        LocalDateTime now = LocalDateTime.now().minusHours(9);
        System.out.println(now.getYear());
        System.out.println(now.getMonthValue());
        System.out.println(now.getDayOfMonth());
    }
}
