#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
    string file_name,text;
    fstream file;
    file.open(file_name+".txt");
    cout<<"enter file name here:";
    cin>>file_name;
    cout<<"enter text here:";
    cin>>text;
    file<<text;
    return 0;
}