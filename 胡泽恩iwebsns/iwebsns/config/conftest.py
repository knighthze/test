import sys
sys.path.insert(0,"C:\\Users\\吾之梦\\PycharmProjects\\untitled1\\iwebsns")
project_file = sys.path[0]
url = "http://iwebsns.pansaifei.com/"
driver_path = project_file+r"\driver\geckodriver.exe"
login_path = project_file + r"\data\login.xlsx"
case_path = project_file+r"\testcases"
repo_path = project_file + r"\result\report"
log_path=project_file+r'\log\log.txt'