def read_file(file_name):
    """파일을 라인 단위로 읽는다."""
    fread = open(file_name, mode='r')
    data = [line for line in fread if line.startswith(">>")]
    return data


