#!/usr/bin/env python

from collections import defaultdict
import collections

class Graph:
    def __init__(self) -> None:
        self.graph = collections.defaultdict(list)
        self.in_degree = collections.defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[u] = 0

    def topological_sort(self):
        queue = []
        course_order = []
        for i in self.graph:
            for j in self.graph[i]:
                self.in_degree[j] += 1
        for i in self.in_degree:
            if self.in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)
            course_order.append(course)
            for i in self.graph[course]:
                self.in_degree[i] -= 1
                if self.in_degree[i] == 0:
                    queue.append(i)
        
        print(course_order)
        if len(course_order)%2:
            print(course_order[len(course_order)//2])
        else:
            print(course_order[len(course_order)//2 - 1])
        
if __name__ == '__main__':
    courses = Graph()
    prereqs_courses= [
        ["Foundations of Computer Science", "Operating Systems"],
	    ["Data Structures", "Algorithms"], ["Computer Networks", "Computer Architecture"],
	    ["Algorithms", "Foundations of Computer Science"], 
        ["Computer Architecture", "Data Structures"], ["Software Design", "Computer Networks"]
    ]
    for course in prereqs_courses:
        courses.add_edge(course[0], course[1])
    courses.topological_sort()

    courses = Graph()
    prereqs_courses2 = [["Data Structures", "Algorithms"], ["Algorithms", "Foundations of Computer Science"],
	    ["Foundations of Computer Science", "Logic"]]
    for course in prereqs_courses2:
        courses.add_edge(course[0], course[1])
    courses.topological_sort()

    courses = Graph()
    prereqs_courses3 = [["Data Structures", "Algorithms"]]
    for course in prereqs_courses3:
        courses.add_edge(course[0], course[1])
    courses.topological_sort()
