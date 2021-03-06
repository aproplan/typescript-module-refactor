import os

# get the length of the file
def file_len(fname):
    with open(fname, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# read the first and last line of a file
def read_first_last_lines(fname):
    print("printing first and last line...")
    with open(fname, "r") as f:
        print("first line: '" + f.readline() + "'")
        print("last line: " + f.readlines()[-1] + "'")

# delete the first and last line of a file
def delete_first_last_lines(fname, length):
    print("deleting first and last line of " + fname +  "...")
    with open(fname,"r+") as f:
        d = f.readlines()
        f.seek(0)
        for x in range(1, length - 1):
            f.write(d[x].replace("\t", "", 1).replace("    ", "", 1))
        f.truncate()

# replace module path by imports
def use_imports(fname, path_name, tsconfig_name, tsconfig_alias):
    print("adding imports for " + tsconfig_name + " to " + fname +  "...")
    need_to_add_import = False;
    with open(fname,"r+") as f:
        d = f.readlines()
        f.seek(0)
		lines = []
        for i in d:
            if(i.find(path_name) > 0 and i.find(path_name+tsconfig_alias) > 0):
                need_to_add_import = True;
                lines.append(i.replace(path_name, ""))
            else:
                lines.append(i)
        
        if(need_to_add_import):
            f.seek(0)
            val = 'import { ' + tsconfig_alias + ' } from "@' + tsconfig_name + '/' + tsconfig_alias + '";' + '\r\n'
            lines.insert(0, val)
            f.writelines(lines);
            f.truncate()

print("Starting lines deletion...");
print()

# for all files recursively
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       file_name = os.path.join(root, name)
       print(file_name)
       use_imports(file_name, "ap.models.projects.", "models/projects", "NoteProjectStatus", "NoteProjectStatus")

# for files within a specific folder
# path = "components/treeList/";
# for filename in os.listdir(path):
#    if os.path.isfile(path + filename):
#        file_length = file_len(path + filename)
#        delete_first_last_lines(path + filename, file_length)
#        use_imports(path + filename, "ap.controllers.", "controllers", "ContactController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "AccessRightController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "AuthenticateController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "CompanyController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "ControllersManager")
#        use_imports(path + filename, "ap.controllers.", "controllers", "CustomViewController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "DashboardController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "DocumentController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "EntityUpdatedEvent")
#        use_imports(path + filename, "ap.controllers.", "controllers", "FormController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "ImportExcelController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "ListController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "MainController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "MassExportController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "MeetingController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "NoteController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "ProjectController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "ReportController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "StateParams")
#        use_imports(path + filename, "ap.controllers.", "controllers", "UIStateController")
#        use_imports(path + filename, "ap.controllers.", "controllers", "UserController")
