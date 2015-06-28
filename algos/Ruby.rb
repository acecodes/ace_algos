# Arrays for testing
unsorted_array = [5, 7, 8, 12, 1]
sorted_array = [1, 5, 9, 12, 15, 22]

# Euclid's algorithm for finding GCFs
def Euclid(p, q)
  if q == 0
    return p
  else
    r = p % q
    return Euclid(q, r)
  end
end

puts("Euclid's algorithm (10, 25): ", Euclid(10, 25))

# Factorial (n!)
def Factorial(n)
  if n <= 1
    return 1
  else
    return n*Factorial(n-1)
  end
end

puts("Factorial (5): ", Factorial(5))

# Fibonacci series
def Fibonacci(n)
  if n <= 1
    return 1
  else
    return Fibonacci(n-1) + Fibonacci(n-2)
  end
end

puts("Fibonacci (6): ", Fibonacci(6))

# Linear search
def LinearSearch(array, target)
  for item in array
    if item == target
      return array.index(item)
    end
  end
  return -1
end

puts("Linear search: ", LinearSearch(unsorted_array, 8))

# Binary search
def BinarySearch(array, target, sorted=true)
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

puts("Binary search: ", BinarySearch(sorted_array, 22))
puts("Binary search (starting with unsorted array): ", BinarySearch(unsorted_array, 8, sorted=false))
