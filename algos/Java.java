public class Java {
  private static int linear_search(int[] array, int target) {
    int len = array.length;

    for (int i = 0; i < len; i++) {
      if (array[i] == target) {
        return i;
      }
    }
    return -1;
  }


  public static void main(String[] args) {
    int[] test_array = {1, 5, 12, 9, 2, 3, 6, 21};

    System.out.println(linear_search(test_array, 9));

  }
}
