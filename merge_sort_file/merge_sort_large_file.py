import split_file
import merge_files


if __name__ == "__main__":

    # enter your file to be sorted and lines_per_page
    large_file = "large_file.txt"
    lines_per_page = 250

    # perform splitting operation on the large_file into small sorted files
    # small_sorted_files : Stores the file names of all small sorted files
    small_sorted_files = split_file.file_splitter(large_file, lines_per_page)

    # final operation
    # merge your small chunks into final sorted file
    merge_files.merge_all(small_sorted_files)
