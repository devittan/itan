#ifndef BOOKS_RECEIVED_H
#define BOOKS_RECEIVED_H

#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

class BooksReceived {
private:
   string nameBookstore;
   string dateShipped;
   int numberHardbound;
   int numberPaperback;
   vector<string> books;

public:
   // Constructors
   BooksReceived();
   BooksReceived(string name, string date, int hardbound, int paperback);

   // Setters
   void setNameBookstore(string name);
   void setDateShipped(string date);
   void setNumberHardbound(int hardbound);
   void setNumberPaperback(int paperback);

   // Getters
   string getNameBookstore() const;
   string getDateShipped() const;
   int getNumberHardbound() const;
   int getNumberPaperback() const;

   // Functions
   void addBook(string book);
   void sortBookList();
   size_t countBooksReceived() const;
   double calcHardboundPercentage() const;
   double calcPaperbackPercentage() const;

   void displayBooksReceivedInfo() const;
};

// Non-Class Functions
void readDataFromFile(BooksReceived& shipment, const string& fileName);

#endif // BOOKS_RECEIVED_H
