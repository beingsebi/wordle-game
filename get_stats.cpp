#include <bits/stdc++.h>
#include "cpp_tools.h"
using namespace std;

ofstream xgx("_stats.txt");
int solve(string x)
{
    {
        ofstream gg("pipe.txt");
        gg << "";
    }
    int cnt = 0;
    while (true)
    {
        string s = prediction();
        xgx << s << " ";
        cnt++;
        if (s == x)
            break;
        string q = encode(s, x);
        vector<string> aux;
        {
            ifstream f("pipe.txt");
            string sss;
            while (f >> sss)
                aux.push_back(sss);
        }
        ofstream g("pipe.txt");
        for (auto i : aux)
            g << i << '\n';
        g << q << '\n'
          << s;
    }
    return cnt;
}
int main()
{
    vector<string> v = get_all_words();
    int sum = 0;
    for (auto i : v)
    {
        xgx << i << " --> ";
        int x = solve(i);
        xgx << " -  " << x << '\n';
        sum += x;
    }
    cout << (double)sum / v.size();
    return 0;
}