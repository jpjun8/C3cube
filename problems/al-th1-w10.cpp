#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

struct Person
{
	int id;
	string name;
	int c;
	int a;
};

int main() {
	Person student[10000];
	int n;
	scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		int id, c, a;
		char name[21];
		scanf("%d %s %d %d", &id, name, &c, &a);
		student[i].id = id;
		student[i].name = name;
		student[i].c = c;
		student[i].a = a;
	}

	int m;
	string search[11];
	scanf("%d", &m);

	for(int i = 0; i < m; i++) {
		cin >> search[i];
	}

	// Loop through all students you want to find
	for(int i = 0; i < m; i++) {
		int check = 1;

		// Loop through all students appended
		for(int j = 0; j < n; j++) {
			// Check each student's name
			// If found, print id, c, a
			// and make check to 0
			if(search[i] == student[j].name) {
				printf("%d %d %d\n", student[j].id, student[j].c, student[j].a);
				check = 0;
			}
		}

		// if no student found
		if(check) {
			printf("-1\n");
		}

	}
	return 0;
}
