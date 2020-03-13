# lines_per_page : max_lines set for small files into which large_file gets divided


def file_splitter(large_file, lines_per_page):

    """
    :param large_file: File to be sorted
    :param lines_per_page: Max number of lines in your file chunk
    :return: Names of small files
    """

    my_files = []

    with open(large_file, 'r') as lf:

        storage = []
        line_count = 0
        file_num = 0

        cur_line = lf.readline()

        while cur_line:
            line_count += 1
            storage.append(int(cur_line.strip()))

            # check if the line_count reached the lines_per_page
            if line_count == lines_per_page:
                # sort the storage
                storage = list(sorted(storage))

                # write the storage into a file with file_num
                my_files.append(write_into_file(storage, file_num))

                # reset necessary variables
                file_num += 1
                storage = []
                line_count = 0

            cur_line = lf.readline()

    # return the array containing the sorted_files names
    return my_files


def write_into_file(arr, f_num):
    my_file = "sorted_{}.txt".format(f_num)

    with open(my_file, 'w') as f:
        '''
           here, we are adding file num to each element
           
           Each line looks like: "20 0\n"
           
           20 is number, 0 is file_num            
        '''
        for ele in arr:
            f.write(str(ele) + ' ' + str(f_num) + '\n')

        return my_file


# file_splitter("test_file.txt", 5)
#
# file_names = file_splitter("test_file.txt", 5)
# print(file_names)
