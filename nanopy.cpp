#include<iostream>
#include<fstream>
#include<string>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    string file_name;
    cout<<"Enter file name: ";
    cin>>file_name;
    std::ifstream input(file_name);
    for( std::string line; getline( input, line ); )
    {
        cout<<line<<"\n";
    }
    cout << "\033[F";
    cout << "\033[F";
    std::string s;
    std::getline(std::cin, s, '$');
    std::cout << s << std::endl;
    return 0;
}