#include <bits/stdc++.h>
#include "cpp_tools.hpp"
using namespace std;
vector<string> this_refine_list(const vector<string> &allw)
{
    vector<string> rez;
    vector<pair<string, string>> t = get_info();
    for (const string &i : allw)
    {
        for (const pair<string, string> &j : t)
            if (i == j.second)
                goto flag;
        if (okay(i, t))
            rez.push_back(i);
    flag:;
    }
    return rez;
}
vector<string> allw;
string this_prediction()
{
    vector<string> rfnd = this_refine_list(allw);
    if (rfnd.size() == 0)
        return "X";
    if (rfnd.size() < 4)
    {
        cout << "WON'T GET HERE\n";
        return rfnd[0];
    }
    string rez;
    double maxim = -1, ent;
    vector<pair<string, string>> axp = get_info();
    for (const string &i : allw)
    {
        ent = entropy(i, rfnd);
        for (const pair<string, string> &j : axp)
            if (i == j.second)
                goto flag2;
        if (ent > maxim)
            maxim = ent, rez = i;
    flag2:;
    }
    return rez;
}
ofstream gp("precomputed.txt");
int main()
{
    allw = get_all_words();
    for (char ch1 = '0'; ch1 <= '2'; ch1++)
        for (char ch2 = '0'; ch2 <= '2'; ch2++)
            for (char ch3 = '0'; ch3 <= '2'; ch3++)
                for (char ch4 = '0'; ch4 <= '2'; ch4++)
                    for (char ch5 = '0'; ch5 <= '2'; ch5++)
                    {
                        string s;
                        s += ch1, s += ch2, s += ch3, s += ch4, s += ch5;
                        if (s == "22222")
                            continue;
                        {
                            ofstream gg("pipe.txt");
                            gg << s << "\nTAREI";
                            gg.flush();
                        }
                        string ax = this_prediction();
                        if (ax.size() == 5)
                            gp << s << " " << ax << '\n', gp.flush();
                        cout << s << endl;
                    }
    return 0;
}
