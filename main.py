from Service.task_service import Task_Service
from Service.user_service import User_Service


def main():
    print("Welcome to the Task Management System")
    print("=======================================")
    task_service = Task_Service()
    user_service = User_Service()


    user_service.add_user(123,"Hems","hems123@gmail.com")

    task_service.create_task(1,"DAS","Learn DSA")
    task_service.create_task(2,"GENAI","Learn GENAI")
    task_service.create_task(3,"AIAGENT","Learn AIAGENT from Scratch")

    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    # print(task_service.complete_task())


    print("Task History:")
    history  = task_service.get_task_history()
    print(history.pop().title)
    print(history.pop().title)
    print(history.pop().title)

if __name__ == "__main__":
    main()
