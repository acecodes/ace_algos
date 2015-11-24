class Recursion
  def Euclid(p, q)
    # Euclid's algorithm for finding GCFs
    if q == 0
      return p
    else
      r = p % q
      return Euclid(q, r)
    end
  end

  def Factorial(n)
    # Factorial (n!)
    if n <= 1
      return 1
    else
      return n*Factorial(n-1)
    end
  end

  def Fibonacci(n)
    # Fibonacci series
    if n <= 1
      return 1
    else
      return Fibonacci(n-1) + Fibonacci(n-2)
    end
  end

  def Summer(n)
    # Recursively sum up to n
    if n > 0
      return n + Summer(n-1)
    else
      return 0
    end
  end

  def Power(n, power)
    # Recursively get n to power
    if power == 1
      return n
    else
      return n * Power(n, power-1)
    end
  end
end

class Search
  def LinearSearch(array, target)
    # Linear search
    for item in array
      if item == target
        return array.index(item)
      end
    end
    return -1
  end

  def BinarySearch(array, target, sorted=true)
    # Binary search
    if sorted == false
      array.sort()
    end
    low = 0
    high = array.length - 1
    middle = Integer((low + high)/2)

    return nil if high < low

    while (low <= high)
      if array[middle] < target
        low = middle + 1
      elsif array[middle] == target
        return middle
      else
        high = middle - 1
      end
      middle = Integer((low + high)/2)
    end
  return -1
  end
end

class Sorting
    def Merge(left, right)
        # Merge function of merge sort
        result = []

        while left.size > 0 && right.size > 0
            result << if left[0] <= right[0]
                left.shift
            else
                right.shift
            end
        end

        return result.concat(left).concat(right)
    end

    def MergeSort(arr)
        # Actual merge sort
        return arr if arr.size <= 1
        left = MergeSort(arr[0, arr.size / 2])
        right = MergeSort(arr[arr.size / 2, arr.size])

        self.Merge(left, right)
    end 
end

class Solutions
  def Palindrome(string)
    return string == string.reverse
  end
end


recur = Recursion.new()
search = Search.new()
sorting = Sorting.new()
solutions = Solutions.new()

# Arrays for testing
unsorted_array = [5, 7, 8, 12, 1]
sorted_array = [1, 5, 9, 12, 15, 22]

puts("Euclid's algorithm (10, 25): ", recur.Euclid(10, 25))
puts("Factorial (5): ", recur.Factorial(5))
puts("Fibonacci (6): ", recur.Fibonacci(6))

puts("Linear search: ", search.LinearSearch(unsorted_array, 8))
puts("Binary search: ", search.BinarySearch(sorted_array, 22))
puts("Binary search (starting with unsorted array): ", search.BinarySearch(unsorted_array, 8, sorted=false))
puts("Merge sort: ", sorting.MergeSort(unsorted_array))
puts("Summing up to 5: ", recur.Summer(5))
puts("5 to the power of 3: ", recur.Power(5, 3))
puts("Is 'dude' a palindrome? ", solutions.Palindrome('dude'))
puts("Is 'dood' a plaindrome? ", solutions.Palindrome('dood'))