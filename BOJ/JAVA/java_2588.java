import java.util.Scanner;

public class java_2588 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int first = in.nextInt();
        int second = in.nextInt();
        int fifth = first * (second / 100);
        int fourth = first * (second / 10 % 10);
        int third = first * (second % 10);
        System.out.printf("%d\n", third);
        System.out.printf("%d\n", fourth);
        System.out.printf("%d\n", fifth);
        System.out.println(first * second);
    }
}
