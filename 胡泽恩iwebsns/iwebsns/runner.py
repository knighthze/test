import pytest
import subprocess

pytest.main()

subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
subprocess.call('allure open -h 127.0.0.1 -p 8081 ./result/report',shell=True)