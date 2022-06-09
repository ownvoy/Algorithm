import java.util.Scanner;

public class java_1330 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        int B = input.nextInt();

        if (A == B) {
            System.out.println("==");
        } else {
            if (A > B) {
                System.out.println(">");
            }

            else {
                System.out.println("<");
            }
        }
    }
}
