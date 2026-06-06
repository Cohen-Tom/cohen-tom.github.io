#include <iostream>
#include <string>

using namespace std;

double surfaceQuadrilatere(double Long, double larg);

double surfaceQuadrilatere(double Long, double larg) {
    double surf;

    surf = Long*larg;
    return surf;
}

int main(){
    int x;
    string name;
    x=5;
    name="Jean";
    cout << x << endl;
    cout << name << endl;


    /*Appel de  fonction*/
    double surf1 = surfaceQuadrilatere(5, 25);
    cout << "Surface rectangle de 5 par 25cm: " << surf1 << endl;

    return 0;
}