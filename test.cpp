#include <iostream>
#include <string>
#include <concepts>
#include <stdexcept>
#include <cmath>

template <typename T>
concept Numeric = std::is_arithmetic_v<T>;
