#include <bits/stdc++.h>
using namespace std;
vector<pair<string, string>> get_info()
{
    ifstream f("pipe.txt");
    vector<pair<string, string>> rez;
    bool ok = 0;
    string ax;
    for (string s; f >> s; ok ^= 1)
        if (!ok)
            ax = s;
        else
            rez.push_back({ax, s});
    return rez;
}
vector<string> get_all_words()
{
    ifstream f("all_words.txt");
    vector<string> rez;
    for (string s; f >> s;)
        rez.push_back(s);
    return rez;
}

bool check_in(const char &ch, const string &s)
{
    for (const char &i : s)
        if (i == ch)
            return true;
    return false;
}

bool okk(string sx1, pair<string, string> sx2)
{
    for (const int i : {0, 1, 2, 3, 4})
        if (sx2.first[i] == '2' && sx2.second[i] != sx1[i])
            return false;

    for (const int i : {0, 1, 2, 3, 4})
        if (sx2.first[i] == '1' && (sx2.second[i] == sx1[i] || !check_in(sx2.second[i], sx1)))
            return false;
    for (const int i : {0, 1, 2, 3, 4})
        if (sx2.first[i] == '0' && check_in(sx2.second[i], sx1))
            return false;
    return true;
}
bool okay(const string &s, const vector<pair<string, string>> &v)
{
    for (const pair<string, string> &i : v)
        if (!okk(s, i))
            return false;
    return true;
}
vector<string> refine_list(const vector<string> &allw)
{
    vector<string> rez;
    vector<pair<string, string>> t = get_info();
    if (t.size() == 1 && t[0].second == "TAREI")
    {
        ifstream f("precomputed.txt");
        string x;
        while (f >> x)
            if (x == t[0].first)
            {
                f >> x;
                return {x};
            }
    }
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
string encode(string st, string ans)
{
    string afis = "00000";
    for (const int i : {0, 1, 2, 3, 4})
        for (const int j : {0, 1, 2, 3, 4})
            if (st[i] == ans[j])
            {
                afis[i] = '1';
                break;
            }
    for (const int i : {0, 1, 2, 3, 4})
        if (ans[i] == st[i])
            afis[i] = '2';
    return afis;
}
double entropy(string st, vector<string> pos)
{
    map<string, int> ma;
    string axss;
    for (const string &i : pos)
    {
        axss = encode(st, i);
        ma[axss]++;
    }
    double rez = 0, prob;
    for (const pair<string, int> &i : ma)
    {
        prob = (double)i.second / pos.size();
        rez -= (double)prob * log2(prob);
    }
    return rez;
}
string prediction()
{
    vector<string> allw = get_all_words();
    vector<string> rfnd = refine_list(allw);
    if (rfnd.size() == 11454)
        return "TAREI";
    if (rfnd.size() < 4)
        return rfnd[0];
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
int main()
{
    ofstream g("write.txt");
    g << prediction();
    return 0;
}