from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # to find already checked people
    while search_queue:  # while queue is not empty
        person = search_queue.popleft()  # take out from queue first person
        if not person in searched:  # if person is not checked
            if person_is_seller(person):
                print(f"{person} is mango seller")
                return True
            else:
                search_queue += graph[person]  # if not - all his friends add to queue
                searched.append(person)  # checked person
    return False


search('you')
