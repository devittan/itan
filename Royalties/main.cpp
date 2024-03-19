#include <iostream>

namespace royaltyRates {
const double optionOneInitialPayment = 5000.0;
const double optionOnePublicationPayment = 20000.0;
const double optionTwoRate = 0.125;
const double optionThreeRate1 = 0.10;
const double optionThreeRate2 = 0.14;
const int optionThreeBreakpoint = 4000;
}

int main() {
    double netPrice;
    int estimatedSales;

    std::cout << "Enter the net price of each copy of the novel: ";
    std::cin >> netPrice;

    std::cout << "Enter the estimated number of copies that will be sold: ";
    std::cin >> estimatedSales;

    double optionOneRoyalties = royaltyRates::optionOneInitialPayment + royaltyRates::optionOnePublicationPayment;
    double optionTwoRoyalties = royaltyRates::optionTwoRate * netPrice * estimatedSales;
    double optionThreeRoyalties;

    if (estimatedSales <= royaltyRates::optionThreeBreakpoint) {
        optionThreeRoyalties = royaltyRates::optionThreeRate1 * netPrice * estimatedSales;
    } else {
        optionThreeRoyalties = royaltyRates::optionThreeRate1 * netPrice * royaltyRates::optionThreeBreakpoint +
                               royaltyRates::optionThreeRate2 * netPrice * (estimatedSales - royaltyRates::optionThreeBreakpoint);
    }

    // Determine and print the best option
    double bestRoyalties = std::max({optionOneRoyalties, optionTwoRoyalties, optionThreeRoyalties});
    if (bestRoyalties == optionOneRoyalties) {
        std::cout << "Option 1 is the best option with royalties: " << optionOneRoyalties << std::endl;
    } else if (bestRoyalties == optionTwoRoyalties) {
        std::cout << "Option 2 is the best option with royalties: " << optionTwoRoyalties << std::endl;
    } else {
        std::cout << "Option 3 is the best option with royalties: " << optionThreeRoyalties << std::endl;
    }

    return 0;
}