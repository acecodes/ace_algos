# Learning the basics of computation via
# "Understanding Computation" by Tom Stuart

class Number < Struct.new(:value)
end

class Add < Struct.new(:left, :right)
end

class Multiply < Struct.new(:left, :right)
end

class Number
  def to_S
    value.to_s
  end

  def inspect
    "«#{self}»"
  end
end

class Add
  def to_s
    "#{left} + #{right}"
  end

  def inspect
    "«#{self}»"
  end
end

class Multiply
  def to_s
    "#{left} * #{right}"
  end

  def inspect
    "«#{self}»"
  end
end
