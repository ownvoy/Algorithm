import java.util.Scanner;

public class java_2525 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        int B = input.nextInt();
        int C = input.nextInt();
        int Cook_hour = C / 60;
        int Cook_minute = C - Cook_hour * 60;
        int real_hour = (A + Cook_hour);
        int real_minute = (B + Cook_minute);

        if (real_minute >= 60) {
            real_minute -= 60;
            real_hour += 1;
        }

        if (real_hour >= 24) {
            real_hour -= 24;
        }

        System.out.printf("%d %d", real_hour, real_minute);
    }
}