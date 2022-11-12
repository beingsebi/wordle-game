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
        if (sx2.first[i] == '2')
        {
            if (sx2.second[i] != sx1[i])
                return false;
            sx1[i] = '~';
            sx2.second[i] = '`';
        }
    for (const int i : {0, 1, 2, 3, 4})
        if (sx2.first[i] == '1' && (sx2.second[i] == sx1[i] || !check_in(sx2.second[i], sx1)))
            return false;
        else if (sx2.first[i] == '1')
        {
            for (const int j : {0, 1, 2, 3, 4})
                if (sx1[j] == sx2.second[i])
                {
                    sx1[j] = '~';
                    break;
                }
            sx2.second[i] = '`';
        }
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
    if (t.size() == 1)
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
        if (ans[i] == st[i])
        {
            st[i] = '`';
            ans[i] = '~';
            afis[i] = '2';
        }

    for (const int i : {0, 1, 2, 3, 4})
        for (const int j : {0, 1, 2, 3, 4})
            if (st[i] == ans[j])
            {
                ans[j] = '~';
                st[i] = '`';
                afis[i] = '1';
                break;
            }
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
    if (rfnd.size() < 4) // here!!!!
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
        xgx << i << " ";
        int x = solve(i);
        xgx << "   -   " << x << '\n';
        sum += x;
    }
    cout << (double)sum / v.size();
    return 0;
}

// 4.0099528
// 1 - 1    -> 1
// 2 - 51   -> 102
// 3 - 2474 -> 7422
// 4 - 6557 -> 26228
// 5 - 2066 -> 10330
// 6 - 288  -> 1728
// 7 - 17   -> 119