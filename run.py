import os

from os import system

import sys

from subprocess import call

from tabulate import tabulate

from Models.mfo import MFO

from Models.fitnessfunctions import FitnessFunctions


# Main function
def main():

    FitnessFunctions_object = FitnessFunctions()

    n_dimension = get_n_dimension_functions_name(FitnessFunctions_object)

    fitness_function_name = get_function_name(FitnessFunctions_object)

    max_iteration = get_max_iteration()

    number_of_moths = get_number_of_moths()

    if fitness_function_name in n_dimension :
            
                dimension = get_dimension()

                mfo_object = MFO(
                            max_iteration,
                            number_of_moths,
                            dimension = dimension,
                            fitnessfunction = fitness_function_name
                        )

    else:

        mfo_object = MFO(
                    max_iteration,
                    number_of_moths,
                    fitnessfunction = fitness_function_name
                )

    report_file_path, report_file_name = get_report_file_name()

    mfo_object.start()

    initial_position_of_moths = mfo_object.initial_position_of_moths

    clear()

    mfo_report_header, mfo_report = mfo_object.get_report()

    mfo_object.draw_the_plot(report_file_path, report_file_name)

    write_the_report(mfo_report_header, mfo_report, max_iteration, report_file_path, report_file_name, initial_position_of_moths)

    print('SUCCESSFUL! Please check the "Report Files\'s Outputs" directory for the created files')


def clear():

    # check and make call for specific operating system 
    _ = system('clear') if os.name == 'posix' else system('cls') 


def get_report_file_name():

    try:

        current_directory = os.getcwd() + '/Report Files\'s Outputs'

        filenames_in_current_directory = os.listdir(current_directory)
    
    except:

        os.mkdir(os.getcwd() + '/Report Files\'s Outputs')

        current_directory = os.getcwd() + '/Report Files\'s Outputs'

        filenames_in_current_directory = os.listdir(current_directory)

    report_file_name = input('Enter a name for report file: ')

    while report_file_name in filenames_in_current_directory : 

        report_file_name = input('This name is not available, Please enter another name: ')

    report_file_path = '{}/{}'.format(current_directory, report_file_name)

    os.mkdir(report_file_path)
    
    return report_file_path, report_file_name


def write_the_report(header, report, max_iteration, report_file_path, report_file_name, initial_position_of_moths):

    file = open('{}/{}.txt'.format(report_file_path, report_file_name), 'w')

    file.write('Initial Position of Moths:\n')

    file.write(
        tabulate(
            initial_position_of_moths
        )
    )

    file.write('\nBest moth\'s score and position in each iteration:\n')
    
    file.write(
        tabulate(
            report,
            headers = header,
            tablefmt = "fancy_grid",
            showindex = range(1, max_iteration + 1),
            colalign = ("center",) * (len(header) + 1),
        )
    )

    file.close()


def get_function_name(obj):

    names = [(i+1, name) for i, name in enumerate(obj.get_functions_name())]

    try:

        choice = int(
            input(' '.join(
                        map(
                            str,
                            [str(name[0])+'-{}\n'.format(name[1]) for name in names]
                        )
                    ) +\
                'Choose your fitness function iD: '
            )
        )

        if not choice in range(1, len(names)+1) : sys.exit('Not valid iD.Please enter valid iD')

        fitness_function_name = list(filter(lambda name: name[0] == choice, names))[0][1]

        return fitness_function_name

    except (ValueError, NameError, SyntaxError):               # raise error message if choice is not integer and exit

        sys.exit('Not an integer! Please enter an integer.')


def get_n_dimension_functions_name(obj):

    return obj.get_n_dimension_functions_name()


def get_max_iteration():

    try:

        return int(input('Enter the Max iteration: '))

    except (ValueError, NameError, SyntaxError):

        sys.exit('Not an integer! Please enter an integer Max iteration.')


def get_number_of_moths():

    try:

        return int(input('Enter the number of moths: '))

    except (ValueError, NameError, SyntaxError):
        
        sys.exit('Not an integer! Please enter an integer number of Moths.')


def get_dimension():

    try:

        dimension = int(input('Enter the dimension: '))

        if dimension < 1: sys.exit("Sorry, no numbers below one")

        return dimension

    except (ValueError, NameError, SyntaxError):

        sys.exit('Not an integer! Please enter an integer dimension.')


# Tell python to run main method
if __name__ == "__main__": main()