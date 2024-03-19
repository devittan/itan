#include "BooksReceived.h"
#include <algorithm>

// Implement the member functions here

BooksReceived::BooksReceived() : nameBookstore(""), dateShipped(""), numberHardbound(0), numberPaperback(0) {}

BooksReceived::BooksReceived(string name, string date, int hardbound, int paperback)
   : nameBookstore(name), dateShipped(date), numberHardbound(hardbound), numberPaperback(paperback) {}

void BooksReceived::setNameBookstore(string name) { nameBookstore = name; }
void BooksReceived::setDateShipped(string date) { dateShipped = date; }
void BooksReceived::setNumberHardbound(int hardbound) { numberHardbound = hardbound; }
void BooksReceived::setNumberPaperback(int paperback) { numberPaperback = paperback; }

string BooksReceived::getNameBookstore() const { return nameBookstore; }
string BooksReceived::getDateShipped() const { return dateShipped; }
int BooksReceived::getNumberHardbound() const { return numberHardbound; }
int BooksReceived::getNumberPaperback() const { return numberPaperback; }

void BooksReceived::addBook(string book) { books.push_back(book); }
void BooksReceived::sortBookList() { sort(books.begin(), books.end()); }
size_t BooksReceived::countBooksReceived() const { return books.size(); }
double BooksReceived::calcHardboundPercentage() const { return (numberHardbound * 100.0) / (countBooksReceived() + 0.0); }
double BooksReceived::calcPaperbackPercentage() const { return (numberPaperback * 100.0) / (countBooksReceived() + 0.0); }

void BooksReceived::displayBooksReceivedInfo() const {
   cout << "Bookstore: " << nameBookstore << endl;
   cout << "Date Shipped: " << dateShipped << endl;
   cout << "Number of Hardbound Books: " << numberHardbound << endl;
   cout << "Number of Paperback Books: " << numberPaperback << endl;

   cout << "\nBook Titles:\n";
   for (const string& book : books) {
       cout << "- " << book << endl;
   }

   cout << fixed << setprecision(1);
   cout << "Percentage of Hardbound Books: " << calcHardboundPercentage() << "%" << endl;
   cout << "Percentage of Paperback Books: " << calcPaperbackPercentage() << "%" << endl;
}
