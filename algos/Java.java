import java.util.Arrays;

public class Java {
  private static int linear_search(int[] array, int target) {
    // Linear search - slow, but you will eventually get the right answer
    int len = array.length;

    for (int i = 0; i < len; i++) {
      if (array[i] == target) {
        return i;
      }
    }
    return -1;
  }

  private static int binary_search(int[] array, int target, boolean unsorted) {

    if (unsorted == true) {
      // If we are fed an unsorted array, sort it
      System.out.println("Sorting unsorted array...");
      Arrays.sort(array);
    }

    // Binary search - fastest possible search, needs a sorted collection
    int first = 0;
    int last = array.length - 1;
    int middle = (first + last) / 2;
    int pos = -1;

    while (first <= last) {
      if (array[middle] < target) {
        first = middle + 1;
      }
      else if (array[middle] == target) {
        pos = middle;
        return pos;
      }
      else {
        last = middle - 1;
      }

      middle = (first + last) / 2;
    }

    return pos;
  }

  private static int factorial(int n) {
    // Recursive factorial
    if (n <= 0) {
      return 1;
    } else {
      return n * factorial(n-1);
    }
  }

  public static void main(String[] args) {
    int[] test_array = {1, 5, 12, 9, 2, 3, 6, 21};
    int[] sorted_array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    System.out.println(linear_search(test_array, 9));
    System.out.println(factorial(5));
    System.out.println(binary_search(test_array, 9, true));
    System.out.println(binary_search(sorted_array, 3, false));
  }
}
