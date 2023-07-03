from unstructured.partition.html import partition_html

# test unstructured html reader
def html_file_reader(file_p):
    return partition_html(filename=file_p)
