import java.util.Scanner;

public class java_2562 {
    public static void main(String[] args) {
        int[] numarray = new int[9];
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < 9; i++) {
            numarray[i] = input.nextInt();
        }
        int max = numarray[0];
        int max_index = 0;
        for (int i = 0; i < numarray.length; i++) {
            if (numarray[i] > max) {
                max = numarray[i];
                max_index = i;

            }
        }
        System.out.printf("%d\n", max);
        System.out.printf("%d\n", max_index + 1);
    }
}
