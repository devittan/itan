#ifndef COMPLEX_H
#define COMPLEX_H

#include <iostream>

using namespace std;

class Complex {
private:
    float real;
    float imaginary;

public:
    // Default constructor
    Complex() : real(0), imaginary(0) {}

    // Parameterized constructor
    Complex(float r, float i) : real(r), imaginary(i) {}

    // Overloaded addition operator
    Complex operator+(const Complex& rhs) const {
        return Complex(real + rhs.real, imaginary + rhs.imaginary);
    }

    // Overloaded subtraction operator
    Complex operator-(const Complex& rhs) const {
        return Complex(real - rhs.real, imaginary - rhs.imaginary);
    }

    // Overloaded multiplication operator
    Complex operator*(const Complex& other) const {
        return Complex(real * other.real - imaginary * other.imaginary,
                       real * other.imaginary + imaginary * other.real);
    }

    // Overloaded division operator
    Complex operator/(const Complex& other) const {
        float denominator = other.real * other.real + other.imaginary * other.imaginary;
        return Complex((real * other.real + imaginary * other.imaginary) / denominator,
                       (imaginary * other.real - real * other.imaginary) / denominator);
    }

    // Conjugate method
    Complex conjugate() const {
        return Complex(real, -imaginary);
    }

    // Friend function for printing Complex numbers
    friend ostream& operator<<(ostream& os, const Complex& c) {
        os << c.real << " + " << c.imaginary << "i";
        return os;
    }
};

#endif