public class Power {
    public static double power(double x, int n) {
        if (n == 0) {
            return 1;
        } else if (n > 0) {
            return x * power(x, n - 1);
        } else {
            return 1 / power(x, -n);
        }
    }

    public static void main(String[] args) {
        System.out.println(power(2, 3));   // 8.0
        System.out.println(power(5, 0));   // 1.0
        System.out.println(power(2, -2));  // 0.25
    }
}
