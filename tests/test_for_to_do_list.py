from lib.to_do_list_class import *

def test_for_adding_task():
    task_list = ToDoList()
    task_list.to_do_list_add("clean up", "tidy the bedroom")
    return_list = task_list.to_do_list_return()
    assert return_list == {"clean up": "tidy the bedroom"}

def test_for_adding_multiple_tasks():
    task_list = ToDoList()
    task_list.to_do_list_add("world domination", "buy a raygun")
    task_list.to_do_list_add("doggo", "walk the dog")
    task_list.to_do_list_add("get fit", "go to the gym")
    task_list.to_do_list_add("coding", "attend makers")
    return_list = task_list.to_do_list_return()
    assert return_list == {'world domination': 'buy a raygun', 'doggo': 'walk the dog', 'get fit': 'go to the gym', 'coding': 'attend makers'} 

def test_for_removing_completed_taks():
    task_list = ToDoList()
    task_list.to_do_list_add("world domination", "buy a raygun")
    task_list.to_do_list_add("doggo", "walk the dog")
    task_list.to_do_list_remove("doggo")
    return_list = task_list.to_do_list_return()
    assert return_list == {'world domination': 'buy a raygun'}