import java.util.Scanner;

public class java_10818 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();

        int[] numarray = new int[number];

        for (int i = 0; i < numarray.length; i++) {
            numarray[i] = input.nextInt();
        }
        int min = numarray[0];
        int max = numarray[0];

        for (int i = 1; i < numarray.length; i++) {
            if (max < numarray[i]) {
                max = numarray[i];
            }
            if (min > numarray[i]) {
                min = numarray[i];
            }
        }
        System.out.printf("%d %d", min, max);
    }

}
