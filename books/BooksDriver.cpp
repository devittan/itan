#include "BooksReceived.h"
#include <iostream>
#include <string> // Ensure this line is present

using namespace std;

int main() {
   BooksReceived shipment;

   // Prompt the user for the file name
   string fileName;
   cout << "Enter the file name: ";
   getline(cin, fileName);

   // Read data from the file
   readDataFromFile(shipment, fileName);

   // Display the shipment information
   shipment.displayBooksReceivedInfo();

   return 0;
}
