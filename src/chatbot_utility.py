import os


working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

# Helper to get chapter list for a subject
def get_chapter_list(selected_subject):
    #update when adding other subjects
    if selected_subject == "Biology":
        subject_name = selected_subject.lower()
        # Get list of chapters from data directory
        chapters_dir = f"{parent_dir}/data/class12/{subject_name}"
        # List all files in the directory
        chapters_list = os.listdir(chapters_dir)
        # Remove file extensions and sort chapters based on chapter number
        chapters_list = [x[:-4] for x in chapters_list]
        # here what we are doing is we are splitting the chapter name by '.'
        # and converting the first part to int for sorting based on
        # chapter number
        chapters_list.sort(key=lambda x: int(x.split('.')[0]))
        return chapters_list


# chapters_list = get_chapter_list("Biology")
# print(chapters_list)