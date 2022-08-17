#include <iostream> 
#include <fstream> 
#include <string>
using namespace std; 
 
int main() 
{ 
    fstream fileobject("my_file.txt");
	string file;
    while ( fileobject >> file ) {
		count++;
    } 
    cout<<count;
    fileobject.close(); 
    return 0; 
}

