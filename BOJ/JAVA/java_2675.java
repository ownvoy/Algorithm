import java.util.Scanner;

public class java_2675 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int test_case = input.nextInt();
        int[] repeat = new int[test_case];

        for (int i = 0; i < test_case; i++) {
            repeat[i] = input.nextInt();
            String line = input.next();
            char[] line_array = line.toCharArray();

            for (int j = 0; j < line_array.length; j++) {
                for (int k = 0; k < repeat[i]; k++) {
                    System.out.printf("%c", line_array[j]);
                }
            }
            System.out.printf("\n");

        }

    }
}
