import glob
import xml.etree.ElementTree as ET

VERSION_TAGS     = {"**/*.Tc*": "ProductVersion"}
CORRECT_VERSIONS = {"**/*.Tc*": "3.1.4024.5"}


def check_versions():
    """
    Checks the Twincat version used to create a file.
    It assumes that the version is stored as an attribute on the top element of the file, the attribute names are
    listed in VERSION_TAGS.
    :return: A dictionary of incorrect files and their version numbers
    """
    incorrect_files_exp = dict()
    incorrect_files_act = dict()
    for file_path, version_attrib in VERSION_TAGS.items():
        correct_version = CORRECT_VERSIONS[file_path]
        found_files = glob.glob(file_path, recursive=True)
        if not found_files:
            raise IOError("ERROR: No files of type {} found".format(file_path))
        for file in found_files:
            tree = ET.parse(file)
            try:
                found_version = tree.getroot().attrib[version_attrib]
                if found_version != correct_version:
                    incorrect_files_exp[file] = correct_version
                    incorrect_files_act[file] = found_version
            except KeyError:
                print("WARNING: No version found for {}".format(file))
    return incorrect_files_exp, incorrect_files_act


if __name__ == "__main__":
    try:
        incorrect_files_exp, incorrect_files_act = check_versions()
        for file, version in incorrect_files_act.items():
            correct_version = incorrect_files_exp[file]
            print("ERROR: {} has incorrect version {}, expected version {}".format(file, version, correct_version))
        if incorrect_files_act:
            exit(1)
    except IOError as e:
        print(e)  # Likely no files found
        exit(2)
