#include "math.h"
#include <iostream>

int main(){
    int a;
    int b;
    std::cin >> a;
    std::cin >> b;

    std::cout << add(a, b) << std::endl;
    std::cout << multiply(a, b) << std::endl;
    return 0;
}