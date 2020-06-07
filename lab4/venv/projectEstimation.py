import math
import sys


class Task:
    def __init__(self, best_case_estimate, most_likely_estimate, worst_case_estimate):
        '''This class has 3 properties: best_case_estimate, most_likely_estimate, worst_case_estimate for our project'''
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate

    def estimation_calc(self):
        """This method calculates the estimate E for the given task."""
        return (self.best_case_estimate + 4 * self.most_likely_estimate + self.worst_case_estimate) / 6

    def standart_deviation_calc(self):
        """This method calculates the standard deviation SD for the given task."""
        return (self.worst_case_estimate - self.best_case_estimate) / 6


class Project:
    """
       This class has 2 properties that are: estimate and standard error for entire project.
       They are initialized with the help of Project methods 'total_project_estimate'
       and 'calculate_standard_error' correspondingly."""
    def __init__(self, estimated_tasks, standart_deviation_tasks):
        self.estimated_tasks = estimated_tasks
        self.standart_deviation_tasks = standart_deviation_tasks

    def exected_value_projects(self):
        """This method calculates the total estimate E for the entire project."""
        return sum(self.estimated_tasks)

    def standard_error_projects(self):
        """This method calculates the standard error SE for the entire project."""
        return math.sqrt(sum([math.pow(i, 2) for i in self.standart_deviation_tasks]))

    def confidence_interval(self):
        """This method calculates the 95% confidence interval for the project and returns the tuple with 2 min/max values"""
        min_ci = self.exected_value_projects() - 2 * self.standard_error_projects()
        max_ci = self.exected_value_projects() + 2 * self.standard_error_projects()
        return (f"Project's 95% confidence interval: {min_ci} ... {max_ci} points")


def input_values(): #func(str) ret int
    """In this function user input estimation values for project"""
    while(True):
        best_case_estimate = input('best-case estimate: ')
        most_likely_estimate = input('most-likely estimate: ')
        worst_case_estimate = input('worst-case estimate: ')
        if (best_case_estimate.isnumeric() and most_likely_estimate.isnumeric() and worst_case_estimate.isnumeric()):
            return int(best_case_estimate), int(most_likely_estimate), int(worst_case_estimate)
            break
        else: print("Enter correct values")


def main():
    estimated_tasks = []
    standard_deviation_tasks = []
    while (True):
        estimate_input = input_values()
        task = Task(*estimate_input)
        estimated_tasks.append(task.estimation_calc())
        standard_deviation_tasks.append(task.standart_deviation_calc())
        print(
            f"Estimate of the task = {task.estimation_calc()}\nStandart deviation of the task = {task.standart_deviation_calc()}")
        cont = input("Do you want to continue? (enter 'y' or 'Y') \n").lower()
        if cont != 'y':
            break
    project = Project(estimated_tasks, standard_deviation_tasks)
    print(project.confidence_interval())


if __name__ == '__main__':
    main()
